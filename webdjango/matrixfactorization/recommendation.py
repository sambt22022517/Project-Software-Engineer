from django.contrib.auth.models import User
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np

from .models import Review, Cluster


def update_clusters(is_new_user):
    num_reviews = Review.objects.count()
    print(num_reviews)
    # update_step = ((num_reviews/100)+1) * 5
    update_step = 6
    print(update_step)
    if num_reviews % update_step == 0 or is_new_user:
        # Create a sparse matrix from user reviews
        all_user_names = list(map(lambda x: x.username, User.objects.only("username")))
        all_product_ids = set(map(lambda x: x.product.id, Review.objects.only("product")))
        num_users = len(all_user_names)
        ratings_m = dok_matrix((num_users, max(all_product_ids) + 1), dtype=np.float32)
        for i in range(num_users):  # each user corresponds to a row, in the order of all_user_names
            user_reviews = Review.objects.filter(user_name=all_user_names[i])
            for user_review in user_reviews:
                ratings_m[i, user_review.product.id] = user_review.rating

        # Perform kmeans clustering
        k = int(num_users / 10) + 2
        kmeans = KMeans(n_clusters=k)
        clustering = kmeans.fit(ratings_m.tocsr())

        # Update clusters
        Cluster.objects.all().delete()
        new_clusters = {i: Cluster(name=i) for i in range(k)}
        for cluster in new_clusters.values():  # clusters need to be saved before referring to users
            cluster.save()
        for i, cluster_label in enumerate(clustering.labels_):
            new_clusters[cluster_label].users.add(User.objects.get(username=all_user_names[i]))

        print(new_clusters)

def Myrecommend():
    def normalizeRatings(myY, myR):
        # The mean is only counting movies that were rated
        Ymean = np.sum(myY, axis=1) / np.sum(myR, axis=1)
        Ymean = Ymean.reshape((Ymean.shape[0], -1))
        return myY - Ymean, Ymean

    def flattenParams(myX, myTheta):
        return np.concatenate((myX.flatten(), myTheta.flatten()))

    def reshapeParams(flattened_XandTheta, mynm, mynu, mynf):
        assert flattened_XandTheta.shape[0] == int(mynm * mynf + mynu * mynf)
        reX = flattened_XandTheta[: int(mynm * mynf)].reshape((mynm, mynf))
        reTheta = flattened_XandTheta[int(mynm * mynf) :].reshape((mynu, mynf))
        return reX, reTheta

    def cofiCostFunc(myparams, myY, myR, mynu, mynm, mynf, mylambda=0.0):
        myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
        term1 = myX.dot(myTheta.T)
        term1 = np.multiply(term1, myR)
        cost = 0.5 * np.sum(np.square(term1 - myY))
        # for regularization
        cost += (mylambda / 2.0) * np.sum(np.square(myTheta))
        cost += (mylambda / 2.0) * np.sum(np.square(myX))
        return cost

    def cofiGrad(myparams, myY, myR, mynu, mynm, mynf, mylambda=0.0):
        myX, myTheta = reshapeParams(myparams, mynm, mynu, mynf)
        term1 = myX.dot(myTheta.T)
        term1 = np.multiply(term1, myR)
        term1 -= myY
        Xgrad = term1.dot(myTheta)
        Thetagrad = term1.T.dot(myX)
        # Adding Regularization
        Xgrad += mylambda * myX
        Thetagrad += mylambda * myTheta
        return flattenParams(Xgrad, Thetagrad)

    df = pd.DataFrame(list(Review.objects.all().values()))
    print(df)
    mynu = df.user_name.unique().shape[0]
    mynm = df.product_id.unique().shape[0]
    mynf = 10
    Y = np.zeros((mynm, mynu))


    print(R)
    Ynorm, Ymean = normalizeRatings(Y, R)
    X = np.random.rand(mynm, mynf)
    Theta = np.random.rand(mynu, mynf)
    myflat = flattenParams(X, Theta)

    # mylambda = 12.2
    # result = scipy.optimize.fmin_cg(cofiCostFunc, x0=myflat, fprime=cofiGrad, args=(Y, R, mynu, mynm, mynf, mylambda),
    #                                 maxiter=40, disp=True, full_output=True)
    # resX, resTheta = reshapeParams(result[0], mynm, mynu, mynf)
    # prediction_matrix = resX.dot(resTheta.T)
    # print(prediction_matrix)
    # return prediction_matrix, Ymean ,product_to_row ,user_to_column
    result = scipy.optimize.minimize(
        fun=cofiCostFunc,
        x0=myflat,
        args=(Ynorm, R, mynu, mynm, mynf, 12.2),
        method="TNC",
        jac=cofiGrad,
        options={"maxiter": 100},
    )

    resX, resTheta = reshapeParams(result.x, mynm, mynu, mynf)
    prediction_matrix = resX.dot(resTheta.T)
    print(prediction_matrix)
    return prediction_matrix, Ymean, product_to_row, user_to_column


class uuCF(object):
    def __init__(self, Y_data, k, sim_func=cosine_similarity):
        self.Y_data = Y_data  # a 2d array of shape (n_users, 3)
        self.Y_data = np.array(Y_data)
        # each row of Y_data has form [user_id, item_id, rating]
        self.k = k  # number of neighborhood
        # similarity function, default: cosine_similarity
        self.sim_func = sim_func
    

    def fit(self):
        # normalized Y_data -> Ybar
        users = self.Y_data[:, 0]  # all users - first column of Y_data
        self.Ybar = self.Y_data.copy()
        self.mu = np.zeros((self.n_users,))
        for n in range(self.n_users):
            # row indices of ratings made by user n
            ids = np.where(users == n)[0].astype(np.int32)
            ratings = self.Y_data[ids, 3]
            # avoid zero division
            self.mu[n] = np.mean(ratings) if ids.size > 0 else 0
            self.Ybar[ids, 3] = ratings - self.mu[n]
        # form the rating matrix as a sparse matrix.
        # see more: https://goo.gl/i2mmT2
        self.Ybar = sparse.coo_matrix(
            (self.Ybar[:, 2], (self.Ybar[:, 1], self.Ybar[:, 0])), (self.n_items, self.n_users)
        ).tocsr()
        self.S = self.sim_func(self.Ybar.T, self.Ybar.T)

    def pred(self, u, i):
        """predict the rating of user u for item i"""
        # find item i
        ids = np.where(self.Y_data[:, 1] == i)[0].astype(np.int32)
        # all users who rated i
        users_rated_i = (self.Y_data[ids, 0]).astype(np.int32)
        sim = self.S[u, users_rated_i]  # sim. of u and those users
        nns = np.argsort(sim)[-self.k :]  # most k similar users
        nearest_s = sim[nns]  # and the corresponding similarities
        r = self.Ybar[i, users_rated_i[nns]]  # the corresponding ratings
        eps = 1e-8  # a small number to avoid zero division
        return (r * nearest_s).sum() / (np.abs(nearest_s).sum() + eps) + self.mu[u]
