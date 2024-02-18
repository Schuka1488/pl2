const goTopBtn = document.querySelector(".go-top");

goTopBtn.addEventListener("click", goTop);

function goTop() {
    if(window.pageYOffset > 0) {
     window.scrollTo({ top: 0, behavior: 'instant' });
     setTimeout(goTop, 0);
    }
}