document.addEventListener("DOMContentLoaded", () => {
    var header = document.getElementById("header_homepage");
    var h1 = document.querySelector("#header_homepage h1");
    var buttons = document.querySelectorAll(".top .menu a .menu_button");
    document.addEventListener("scroll", () => {
        header.style.backgroundPosition = `0px -${window.scrollY * 0.2}px`;
        h1.style.marginBottom = `-${window.scrollY}px`;

        if (window.scrollY > 350) {
            document.querySelector(".top").style.height = '70px';
            buttons.forEach(button => {
                button.style.marginTop = "0px";
                button.style.opacity = "1";
            })
        } else {
            document.querySelector(".top").style.height = '45px';
            buttons.forEach(button => {
                button.style.marginTop = "-20px";
                button.style.opacity = "0";
            })
        }
    })
})