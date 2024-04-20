console.log("đã gọi file javascript");
const select_all_product = document.querySelector(".gio-hang-da-dang-nhap-checkbox"); // chỉ có 1 phần tử
const select_each_product = document.querySelectorAll(".gio-hang-da-dang-nhap-checkbox-chon-sp"); //có thể có nhiều phần tử
const click_button_checkout = document.querySelector(".gio-hang-da-dang-nhap-button-mua-hang"); //chỉ có 1 phần tử 
const not_selected_product = document.querySelector(".chua-chon-san-pham-root-class-name2");
const close_notice_not_selected_product = document.querySelector(".chua-chon-san-pham-button");

const click_button_search = document.getElementsByClassName("gio-hang-da-dang-nhap-button button"); //chỉ có 1 phần tử
const click_button_increase_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-tang-sl button"); //có thể có nhiều phần tử
const click_button_decrease_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-button-giam-sl button"); //có thể có nhiều phần tử
const input_quantity = document.getElementsByClassName("gio-hang-da-dang-nhap-input-sl input"); // có thể có nhiều phần tử

const container_sls = document.querySelectorAll(".gio-hang-da-dang-nhap-container-sl")


// các hàm được định nghĩa ở đây
function compute_expression(element, event){

    // check sự kiện có phù hợp với hàm
    var valid = false;
    if (event.type === "blur"){
        valid = true;
    }

    if (event.type === "keydown"){
        if (event.key === "Enter"){
            valid = true;
        }
    }

    if (valid){
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
        result = result >= 0 ? result : 0;

        element.value = result;

        element.blur();
    }
}

// khống chế đầu vào input từ bàn phím không thể < 0, tính toán giá trị biểu thức.
Array.from(input_quantity).forEach(element => {
    element.addEventListener("keydown", function(event) {
        compute_expression(element, event);
    });
    element.addEventListener("blur", function(event) {
        compute_expression(element, event);
    });
});

// button + - , tăng giảm giá trị input
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
        
        newvalue = parseInt(input.value) - 1
        
        input.value = newvalue >= 0 ? newvalue : 0
    });

});

// select all
select_all_product.addEventListener('change', function(event){
    var isChecked = event.target.checked;
    console.log('select all được nhấn');
    if (isChecked){
        select_each_product.forEach(element => {
            element.checked = true
        })
    }else{
        select_each_product.forEach(element => {
            element.checked = false
        })
    }
});

// Trước khi mua hàng, phải kiểm tra xem có sản phẩm nào được chọn chưa
click_button_checkout.addEventListener('click', function(event){
    var count_checked = 0;
    select_each_product.forEach(element => {
        if (element.checked){
            count_checked ++;
        }
    })
    if (count_checked === 0){
        console.log("chưa có sản phẩm nào được chọn");
        not_selected_product.style.display = "flex";
    }else{

    }
})

// đóng thông báo chưa chọn sp
close_notice_not_selected_product.addEventListener('click', function(event){
    not_selected_product.style.display = "none";
});



