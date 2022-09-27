const btn_signup = document.getElementById("btn_signup");
btn_signup.addEventListener('click', function () {
        document.getElementById('keyword1').value = document.getElementById('keyword1-option').value;
        document.getElementById('keyword2').value = document.getElementById('keyword2-option').value;
        document.getElementById('signupForm').submit();
    })

const btn_login = document.getElementById("btn_login");
btn_login.addEventListener('click', function () {
        document.getElementById('loginForm').submit();
    })