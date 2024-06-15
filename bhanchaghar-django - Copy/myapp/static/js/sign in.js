// sign in.js
document.addEventListener('DOMContentLoaded', function () {
    const loginBtn = document.getElementById('login');
    const registerBtn = document.getElementById('register');
    const loginForm = document.querySelector('.login-form');
    const registerForm = document.querySelector('.register-form');

    loginBtn.addEventListener('click', function () {
        loginBtn.style.backgroundColor = "#21264D";
        registerBtn.style.backgroundColor = "rgba(255, 255, 255, 0.2)";

        loginForm.style.left = "50%";
        registerForm.style.left = "-50%";

        loginForm.style.opacity = 1;
        registerForm.style.opacity = 0;

        document.querySelector(".col-1").style.borderRadius = "0 30% 20% 0";
    });

    registerBtn.addEventListener('click', function () {
        loginBtn.style.backgroundColor = "rgba(255, 255, 255, 0.2)";
        registerBtn.style.backgroundColor = "#21264D";

        loginForm.style.left = "150%";
        registerForm.style.left = "50%";

        loginForm.style.opacity = 0;
        registerForm.style.opacity = 1;

        document.querySelector(".col-1").style.borderRadius = "0 20% 30% 0";
    });

    // Default to showing the correct form based on the form_type context variable
    if (document.querySelector('.register-form').style.display === 'block') {
        registerBtn.click();
    } else {
        loginBtn.click();
    }
});
