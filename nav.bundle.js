/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
const createNav = () => {
    let nav = document.querySelector('.navbar');

    let title = document.querySelector('.title-cr');

    let titleName = title.getAttribute('navName')

    nav.innerHTML = `
    <header class="header transparent fixed light-text" data-onscroll-classes="dark-text white-bg"
        data-onscroll-logo="images/logo-dark-cr.svg">

    <div class="container">
        <nav class="header__nav bottom-nav">

            <div class="header__logo brand--logo">
                <br>
                <a href="index.html"><img src="images/logo-light-cr.svg" alt="Greater Love Church"></a>
            </div>

            <div class="header__mobile--opener hide-on-lg">
                <button class="header__mobile--icon" aria-expanded="false" aria-controls="mobile-menu" data-toggle="mobile-menu">
                    <span class="line"></span>
                    <span class="line"></span>
                    <span class="line"></span>
                </button>
            </div>

            <ul class="header__navitems show-on-lg" id="mobile-menu">

                <!-- Contains donation button for mobile and tablet devices -->
                <li class="header__extra">
                    <div class="cta">
                        <a href="donations.html" class="button button-block-sm">Donación</a>
                    </div>
                </li><!-- .header__extra ends -->

                <li class = "header__list ${(titleName === "HOME") ? "active" : ""}"><a href="index.html">Home</a></li>
                <!-- .header__list ends -->

                <li class="header__list ${(titleName === "CONOCENOS") ? "active" : ""}"><a href="about.html">Conocenos</a></li><!-- .header__list ends -->

                <li class="header__list ${(titleName === "SERMONES") ? "active" : ""}"><a href="sermons.html">Sermones</a></li><!-- .header__list ends -->

<!--                <li class="header__list">-->
<!--                    <a href="" class="dropdown-link">Sermones</a>-->

<!--                    <div class="header__submenu">-->
<!--                        <ul>-->

<!--                            <li class="header__list"><a href="sermons.html">Sermones</a></li>-->
<!--                            <li class="header__list"><a href="sermons-single.html">Sermones individuales</a></li>-->

<!--                        </ul>-->

<!--                    </div>&lt;!&ndash; .header__submenu ends &ndash;&gt;-->
<!--                </li>&lt;!&ndash; .header__list ends &ndash;&gt;-->

                <li class="header__list ${(titleName  === "MINISTERIOS") ? "active" : ""}"><a href="ministries.html">Ministerios</a></li><!-- .header__list ends -->

<!--                <li class="header__list">-->
<!--                    <a href="" class="dropdown-link">Ministerios</a>-->

<!--                    <div class="header__submenu">-->
<!--                        <ul>-->

<!--                            <li class="header__list"><a href="ministries.html">Ministerios</a></li>-->
<!--                            <li class="header__list"><a href="ministries-single.html">Detalle de Ministerios</a></li>-->

<!--                        </ul>-->
<!--                    </div>&lt;!&ndash; .header__submenu ends &ndash;&gt;-->
<!--                </li>&lt;!&ndash; .header__list ends &ndash;&gt;-->

<!--                <li class="header__list">-->
<!--                    <a href="" class="dropdown-link">Eventos</a>-->

<!--                    <div class="header__submenu">-->
<!--                        <ul>-->

<!--                            <li class="header__list"><a href="events.html">Eventos</a></li>-->
<!--                            <li class="header__list"><a href="events-single.html">Eventos individuales</a></li>-->

<!--                        </ul>-->
<!--                    </div>&lt;!&ndash; .header__submenu ends &ndash;&gt;-->
<!--                </li>&lt;!&ndash; .header__list ends &ndash;&gt;-->

<!--                <li class="header__list">-->
<!--                    <a href="" class="dropdown-link">Paginas</a>-->

<!--                    <div class="header__submenu">-->
<!--                        <ul>-->

<!--                            <li class="header__list"><a href="donations.html">Donaciones</a></li>-->
<!--                            <li class="header__list"><a href="staffs-single.html">Lideres</a></li>-->
<!--                            &lt;!&ndash;                  <li class="header__list"><a href="elements.html">Elements</a></li>&ndash;&gt;-->

<!--                        </ul>-->
<!--                    </div>&lt;!&ndash; .header__submenu ends &ndash;&gt;-->
<!--                </li>&lt;!&ndash; .header__list ends &ndash;&gt;-->

                <!--            <li class="header__list">-->
                <!--              <a href="" class="dropdown-link">Blog</a>-->

                <!--              <div class="header__submenu">-->
                <!--                <ul>-->

                <!--                  <li class="header__list"><a href="blog.html">Blog list</a></li>-->
                <!--                  <li class="header__list"><a href="blog-single.html">Blog single</a></li>-->

                <!--                </ul>-->
                <!--              </div>&lt;!&ndash; .header__submenu ends &ndash;&gt;-->
                <!--            </li>&lt;!&ndash; .header__list ends &ndash;&gt;-->

                <li class="header__list ${(titleName === "CONTACTO") ? "active" : ""}"><a href="contact.html">Contacto</a></li>
                <!-- .header__list ends -->

            </ul><!-- .header__navitems ends -->

            <!-- Contains Shopping cart and donation button -->
            <div class="header__extra desktop-version">
                <div class="cta hide-on-sm show-on-lg">
                    <a href="donations.html" class="button">Donación</a>
                </div>
            </div><!-- .header__extra ends -->

        </nav><!-- .header__nav ends -->
    </div><!-- .container ends -->

</header><!-- .header ends -->
    `;
}

createNav();

$(function () {
    if (document.documentElement.scrollTop > 200) {
        $('.brand--logo img').attr('src', 'images/logo-dark-cr.svg');
        const headers = document.querySelectorAll(".header");
        headers.forEach(function (current) {
            current.className = "header transparent fixed light-text dark-text white-bg";
        });
    }
})

$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.brand--logo img').attr('src', 'images/logo-dark-cr.svg');
            const headers = document.querySelectorAll(".header");
            headers.forEach(function (current) {
                current.className = "header transparent fixed light-text dark-text white-bg";
            });
        }
        if ($(this).scrollTop() < 200) {
            $('.brand--logo img').attr('src', 'images/logo-light-cr.svg');
            const headers = document.querySelectorAll(".header");
            headers.forEach(function (current) {
                current.className = "header transparent fixed light-text";
            });
        }
    })
});

const mobileAction = () => {
    const headers = document.querySelectorAll(".header");
    headers.forEach(function (current) {
        let menuToggle = current.querySelector("[data-toggle]");
        menuToggle.addEventListener("click", openMenu);
        let menuMobile;

        function openMenu() { // opens mobile menu

            let menuToggleTarget = menuToggle.getAttribute("data-toggle");

            const open = JSON.parse(menuToggle.getAttribute("aria-expanded")); // converts to boolean and returns true or false
            menuToggle.setAttribute("aria-expanded", !open);

            menuMobile = current.querySelector("#" + menuToggleTarget); // Gets the menu that needs to be display
            menuMobile.classList.toggle("active"); // shows and hides the menu
            menuToggle.classList.toggle("rotate"); // little animation for the hamburger icon

            document.body.classList.toggle("overflow-hidden"); // prevent scrolling on the page while the menu is being shown
        }
    })
}

mobileAction()

/******/ })()
;