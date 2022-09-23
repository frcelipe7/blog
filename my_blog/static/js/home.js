document.addEventListener("DOMContentLoaded", () => {
    var header = document.getElementById("header_homepage");
    document.addEventListener("scroll", () => {
        header.style.backgroundPosition = `0px -${window.scrollY * 0.2}px`;
    })
})