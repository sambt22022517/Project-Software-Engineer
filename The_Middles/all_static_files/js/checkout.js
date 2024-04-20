const confirmation = document.querySelector(".thanh-toan-button-xac-nhan-thanh-toan");
const ispayment = document.querySelector(".hoi-thanh-toan-container");
const degree_payment = document.querySelector(".hoi-thanh-toan-button-degree");
const refuse_payment = document.querySelector(".hoi-thanh-toan-button-refuse");
const suscess_payment = document.querySelector(".giao-dich-thanh-cong-container");
const button_change = document.querySelector(".thanh-toan-button-thay-doi");
const sub_button_change = document.querySelectorAll(".thay-doi-dia-chi-button");
const container_change_location = document.querySelector(".thay-doi-dia-chi-container");
const close_container_change_location = document.querySelector(".thay-doi-dia-chi-button2");
const confirm_change_location = document.querySelector(".thay-doi-dia-chi-button3");
const adjust_location = document.querySelector(".them-dia-chi-moi-capnhat-container");
const confirm_adjust_location = document.querySelector(".them-dia-chi-moi-capnhat-button1");
const refuse_adjust_location = document.querySelector(".them-dia-chi-moi-capnhat-button");

confirmation.addEventListener('click', function(event){
    ispayment.style.display = "flex";
});

degree_payment.addEventListener('click', function(event){
    suscess_payment.style.display = "flex";
    ispayment.style.display = "none";
});

refuse_payment.addEventListener('click', function(event){
    ispayment.style.display = "none";
});

suscess_payment.addEventListener('click', function(event){
    suscess_payment.style.display = "none";
});

button_change.addEventListener('click', function(event){
    container_change_location.style.display = "flex";
});

close_container_change_location.addEventListener('click', function(event){
    container_change_location.style.display = "none";
});

confirm_change_location.addEventListener('click', function(event){
    container_change_location.style.display = "none";
});

sub_button_change.forEach(element =>{
    element.addEventListener('click', function(event){
        adjust_location.style.display = "flex";
    });
});

confirm_adjust_location.addEventListener('click', function(event){
    adjust_location.style.display = "none";
});

refuse_adjust_location.addEventListener('click', function(event){
    adjust_location.style.display = "none";
});





