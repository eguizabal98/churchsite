// PAGE LOADER ======================================= // 
window.addEventListener("load", function () {

  const loader = document.querySelector(".page-loader");

  if (loader) {

    loader.classList.add("slide-off");

    setTimeout(function () {
      loader.classList.add("is-loading-finish");
      loader.remove();
    }, 2000)

  }

});


// HEADER ====================================== // 
// Mini plugin for the header
const headers = document.querySelectorAll(".header");

headers.forEach(function (current) {

  let originalClasses = current.className, // Classes to be added on scroll
    scrollClasses = current.getAttribute("data-onscroll-classes"), // Classes to be added on scroll
    scrollLogo = current.getAttribute("data-onscroll-logo"), // Logo to show on scroll
    brandLogo = current.querySelector(".header__logo img"), // Gets the current logo img tag
    brandLogoUrl = current.querySelector(".header__logo img").getAttribute("src"), // Gets the current logo src
    menuToggle = current.querySelector("[data-toggle]"), // Gets the element to toggle the naviagtion on mobile devices
    menuMobile, // Gets the menu for the mobile or submenu
    dropdownLink = current.querySelectorAll(".dropdown-link"), // Gets the dropdown links
    searchToggle = current.querySelector("[data-search]"), // Gets the element to toggle the search form
    searchForm, // Gets the search form
    scrollAmount = 100; // how far down (in px) 


  // Preventing the link default action
  for (let i = 0; i < dropdownLink.length; i++) {
    dropdownLink[i].addEventListener("click", function (e) {
      e.preventDefault();
    })
  }


  // Opening the mobile menu
  if (menuToggle) menuToggle.addEventListener("click", openMenu);
  // Adds classes on scroll
  if (scrollClasses) addClasses();
  // Changes logo on scroll
  if (scrollLogo) changeLogo();


  // FUNCTIONS ======================== // 
  function openMenu() { // opens mobile menu


    let menuToggleTarget = menuToggle.getAttribute("data-toggle");

    const open = JSON.parse(menuToggle.getAttribute("aria-expanded")); // converts to boolean and returns true or false
    menuToggle.setAttribute("aria-expanded", !open);

    menuMobile = current.querySelector("#" + menuToggleTarget); // Gets the menu that needs to be display
    menuMobile.classList.toggle("active"); // shows and hides the menu
    menuToggle.classList.toggle("rotate"); // little animation for the hamburger icon

    document.body.classList.toggle("overflow-hidden"); // prevent scrolling on the page while the menu is being shown
  };


  function scrollEvents(type) {

    let scrolled = window.scrollY;

    if (scrolled > scrollAmount) {
      if (type === "class") {
        current.className = originalClasses + " " + scrollClasses;
      } else {
        brandLogo.setAttribute("src", scrollLogo);
      }
    }

    else {
      if (type === "class") {
        current.className = "";
        current.className = originalClasses
      } else {
        brandLogo.setAttribute("src", "");
        brandLogo.setAttribute("src", brandLogoUrl);
      }

    }

  }


  function addClasses() { window.addEventListener("scroll", function () { scrollEvents("class") }); };

  function changeLogo() { window.addEventListener("scroll", function () { scrollEvents("logo") }); };

});


// CAROUSELS ================================ // 
// Using Owl Carousel plugin

// Hero carousel - Homepage 1
$('#hero-carousel').owlCarousel({
  items: 1, // how many slide to show on screen
  autoplay: true, // true or false
  autoplayTimeout: 4000, // how long before the next slide come on the screen in milliseconds (ex: 1000ms = 1s)
  autoplaySpeed: 450, //how long it take for a slide to fully come on screen
  slideTransition: "cubic-bezier(.1,.75,.67,.88)", // transition-timing-function (linear, ease-in, ease-in-out, etc...)
  loop: true, // true or false - whether the slideshow repeat or not
  mouseDrag: false, // true or false - laptop & desktop (any non-touch device)
  touchDrag: false, // true or false - mobile (or any touch-friendly device)
  dots: true, // true or false - show dots navigation
  nav: true, // true or false - show 'next' or 'prev' buttons
  autoplayHoverPause: true, // true or false - stop autoplay on hover
  responsiveClass: true, // true or false
});


// ANIMATE ON SCROLL ================================= // 
// Using Animate On Scroll (AOS) plugin
AOS.init({
  once: true, // whether animation should happen only once - while scrolling down
});



// SCROLL BACK TO TOP ================================ // 
let scrollTopEl = document.querySelector(".scroll-to-top");

if (scrollTopEl) window.addEventListener("scroll", scrollToTop);

function scrollToTop() {

  const scrollable = document.documentElement.scrollHeight - window.innerHeight; // entire scrollabe space - the window's height = gives how much you can scroll

  let scrolled = window.scrollY; // how far down user has scrolled

  let scrolledPerc = Math.floor((scrollable * 50) / 100); // how far down user has scrolled in percentage - in this example 30% of the scrollable

  if (scrolled >= scrolledPerc) {
    scrollTopEl.classList.add("active");
  } else {
    scrollTopEl.classList.remove("active");
  }

}

function smoothScroll() {

  if (!scrollTopEl) return;

  scrollTopEl.addEventListener("click", function () {

    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "smooth"
    });

  });

}

smoothScroll();


// DONATION PAGE ============================ // 

// We will remove any amount selected (radio button) so the custom (input text) will be the active one
function customAmount() {
  const customAmountField = document.querySelector(".donations__form .donations__amount #custom"); // gets the input text

  // if there is no input text accepting the custom value, then the code following the below code won't be executed
  if (!customAmountField) return;

  customAmountField.addEventListener("focus", function () {

    // Getting all amount (radio buttons)
    const currentAmount = document.querySelectorAll(".donations__form .donations__amount input[type='radio']");

    for (var i = 0; i < currentAmount.length; i++) {
      if (currentAmount[i].checked) {
        // Remove the current checked
        currentAmount[i].checked = false;
      }
    }

  })
}
customAmount();

// Showing the credit card form
function showCardForm() {
  // Button for the credit card
  const creditCardSelector = document.querySelectorAll(".donations__form .donations__payment input[type='radio']");
  // Form for the credit card
  const creditCardForm = document.querySelector(".donations__form .credit-card-payment-form");
  // PayPal link
  const paypalLink = document.querySelector(".donations__form .paypal-link");
  // Credit card image (jQuery card plugin)
  const creditCardImage = document.querySelector(".donations .card-wrapper");

  for (var i = 0; i < creditCardSelector.length; i++) {

    creditCardSelector[i].addEventListener("click", function () {
      var values = this.id; // credit-card or paypal

      if (values === "credit-card") {
        creditCardForm.classList.add("active"); // shows donation form
        creditCardImage.classList.add("active"); // shows a credit card image generate by the JQuery card plugin (does not show on smaller devices such as phone and tablet in portrait mode)

        paypalLink.classList.remove("active"); // hides the PayPal option

      } else {
        creditCardForm.classList.remove("active"); // hides donation form
        creditCardImage.classList.remove("active"); // hides the credit card image generate by the JQuery card plugin

        paypalLink.classList.add("active"); // shows the PayPal option
      }
    })
  }

}
showCardForm();

// Credit card - Donation page
// Using JQuery Card plugin

var donations = new Card({
  // a selector or DOM element for the form where users will
  // be entering their information
  form: '.donations__form', // *required*
  // a selector or DOM element for the container
  // where you want the card to appear
  container: '.card-wrapper', // *required*

  formSelectors: {
    numberInput: 'input#card-number-payment', // optional — default input[name="number"]
    expiryInput: 'input#card-expiration-payment', // optional — default input[name="expiry"]
    cvcInput: 'input#card-ccv-payment', // optional — default input[name="cvc"]
    nameInput: 'input#name-on-card' // optional - defaults input[name="name"]
  },

  width: 200, // optional — default 350px
  formatting: true, // optional - default true

  // Strings for translation - optional
  messages: {
    validDate: 'valid\ndate', // optional - default 'valid\nthru'
    monthYear: 'mm/yyyy', // optional - default 'month/year'
  },

  // Default placeholders for rendered fields - optional
  placeholders: {
    number: '•••• •••• •••• ••••',
    name: 'Full Name',
    expiry: '••/••',
    cvc: '•••'
  },

  masks: {
    cardNumber: '•' // optional - mask card number
  },
});

