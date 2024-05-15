document.addEventListener("DOMContentLoaded", function() {
    let loginLink = document.getElementById("loginLink");

    loginLink.addEventListener("click", function() {

        let navLinks = document.querySelectorAll(".nav-link");
        navLinks.forEach(function(link) {
            link.classList.remove("active");

        });
        loginLink.classList.add("active");
        alert("hello")
    });
});
