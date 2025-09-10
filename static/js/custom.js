// simple script for back-to-top-btn just for using javascript in this project aswell //
// get button element from the html //
let mybutton = document.getElementById("back-to-top-btn");

// run the ScrollFunction //
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    // if the user has scrolled down for abit //
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        // the button shows //
        mybutton.style.display = "block";
    } else {
        // otherwise hide the button //
        mybutton.style.display = "none";

    }
    }

    // creates what happens when you press the button //
    mybutton.addEventListener("click", function() {
        // scroll smoothly //
        window.scrollTo({top: 0, behhavior: 'smooth'});
    });