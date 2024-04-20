console.log("đã gọi file javascript");
const select_all_product = document.getElementsByClassName("gio-hang-da-dang-nhap-checkbox"); // chỉ có 1 phần tử
const select_each_product = document.getElementsByClassName("gio-hang-da-dang-nhap-checkbox-chon-sp"); //có thể có nhiều phần tử
const click_button_search = document.getElementsByClassName("gio-hang-da-dang-nhap-button button"); //chỉ có 1 phần tử
const click_button_checkout = document.getElementsByClassName("gio-hang-da-dang-nhap-button-mua-hang button"); //chỉ có 1 phần tử 
const click_button_increase_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-tang-sl button"); //có thể có nhiều phần tử
const click_button_decrease_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-giam-sl button"); //có thể có nhiều phần tử
const input_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-input-sl input"); // có thể có nhiều phần tử

const container_sls = document.querySelectorAll(".gio-hang-da-dang-nhap-container-sl")

// khống chế đầu vào input từ bàn phím không thể < 0
Array.from(input_quantity).forEach(element => {
    element.addEventListener("keydown", function(event) {
        if (event.key === "Enter"){
            // Chuỗi biểu thức toán học
            // Giai đoạn 1: lọc số, dấu +,-
            var oldexpression = element.value;
            var expression = '';
            for (var i = 0; i < oldexpression.length; i++){
                if ((oldexpression[i] >= '0' && oldexpression[i] <= '9') || oldexpression[i] == '+' || oldexpression[i] == '-'){
                    expression += oldexpression[i];
                }
            }

            // Giai đoạn 2: tính toán
            // Phân tích chuỗi thành mảng các số và toán tử
            var tokens = expression.split(/([+-])/).map(function(token) {
                return token.trim();
            });

            console.log(tokens)

            var current_operator = 0;
            var result = 0;
            for(var i = 0; i < tokens.length; i++){
                if(tokens[i] === '-'){
                    current_operator += 1;

                }else if(tokens[i] === '+'){
                    
                }
                else if (tokens[i] != ''){
                    
                    if (current_operator === 1){
                        result -= parseInt(tokens[i]);
                    }else{
                        result += parseInt(tokens[i]);
                    }
                    current_operator = 0;
                }
                if (current_operator === 2){
                    current_operator = 0;
                }
            }
            // console.log('Kết quả: ' + result);
            
            // Nếu giá trị nhỏ hơn 0, đặt lại giá trị thành 0
            if (result < 0) {
                result = 0;
            }

            element.value = result;
        }
    });
});

container_sls.forEach(function(container_sl) {
    // Lấy input và button trong từng khối A
    var input = container_sl.querySelector('.gio-hang-da-dang-nhap-input-sl');
    var button_increase = container_sl.querySelector('.gio-hang-da-dang-nhap-button-tang-sl');
    var button_decrease = container_sl.querySelector('.gio-hang-da-dang-nhap-button-giam-sl');
    
    // Thêm sự kiện click cho button
    button_increase.addEventListener('click', function() {
        // Tăng giá trị của input
        
        input.value = parseInt(input.value) + 1;
        
    });
    
    button_decrease.addEventListener('click', function() {
        // Tăng giá trị của input
        
        input.value = parseInt(input.value) - 1;
        
    });

});

// 
