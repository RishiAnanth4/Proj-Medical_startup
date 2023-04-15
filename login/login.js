const loginForm = document.getElementsByClassName("form__input");
const loginButton = document.getElementsByClassName("form__button");
const loginErrorMsg = document.getElementsByClassName("form__input-error-message")
console.log("in JS");

('#bttn').on('click',() => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in");
        location.reload();
    }else{
        loginErrorMsg.style.opacity = 1;
    }
})
