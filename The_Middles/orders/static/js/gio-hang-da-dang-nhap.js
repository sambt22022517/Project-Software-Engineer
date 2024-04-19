console.log("đã gọi file javascript");
const select_all_product = document.getElementsByClassName("gio-hang-da-dang-nhap-checkbox"); // chỉ có 1 phần tử
const select_each_product = document.getElementsByClassName("gio-hang-da-dang-nhap-checkbox-chon-sp"); //có thể có nhiều phần tử
const click_button_search = document.getElementsByClassName("gio-hang-da-dang-nhap-button button"); //chỉ có 1 phần tử
const click_button_checkout = document.getElementsByClassName("gio-hang-da-dang-nhap-button-mua-hang button"); //chỉ có 1 phần tử 
const click_button_increase_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-tang-sl button"); //có thể có nhiều phần tử
const click_button_decrease_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-giam-sl button"); //có thể có nhiều phần tử
const input_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-input-sl input"); // có thể có nhiều phần tử
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



// nhấn button + sẽ tự động tăng giá trị của input_quantity
Array.from(click_button_increase_quantity).forEach(element => {
    element.addEventListener('click', function(event) {
        // lấy phần tử cha của button +
        var parent_button_increase = element.parentNode;
        // lấy phần tử input sl
        var sub_input_quantity = parent_button_increase.getElementsByClassName("gio-hang-da-dang-nhap-input-sl input");
        // tăng số lượng lên 1
        value = parseInt(sub_input_quantity.value) + 1;
        sub_input_quantity.value = value;
        console.log("đã thực hiện nhấn button + sẽ tự động tăng giá trị của input_quantity")
    });
});

// nhấn button - sẽ tự động giảm giá trị của input_quantity
Array.from(click_button_decrease_quantity).forEach(element => {
    element.addEventListener('click', function(event) {
        // lấy phần tử cha của button +
        var parent_button_increase = element.parentNode;
        // lấy phần tử input sl
        var sub_input_quantity = parent_button_increase.getElementsByClassName("gio-hang-da-dang-nhap-input-sl input");
        // giảm số lượng đi 1
        sub_input_quantity.value -= 1;
    });
});

// 
