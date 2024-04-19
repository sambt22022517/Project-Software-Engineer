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
    element.addEventListener("input", function(event) {
        // Lấy giá trị của input
        var value = parseInt(element.value);
        
        // Nếu giá trị nhỏ hơn 0, đặt lại giá trị thành 0
        if (value < 0) {
            element.value = 0;
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
        sub_input_quantity.value += 1;
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
