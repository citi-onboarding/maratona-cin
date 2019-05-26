// About section
$('.carousel-about').slick({
  slidesToShow: 1,
  dots: true,
  autoplay: true,
  autoplaySpeed: 2000,
  customPaging: (slider, i) => `<div class="dot" id=${i}></div>`,
  arrows: false,
});

// Cards section
const addSlick = () => {
  let carousel = $('.carousel-cards');
  if (window.innerWidth < 960) {
    carousel.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      centerMode: true,
      customPaging: (slider, i) => `<div class="dot" id=${i}></div>`,
      arrows: false,
    });
  } else if (carousel.slick){
    carousel.slick('unslick');
  }
};

window.addEventListener('resize', addSlick);
window.addEventListener('load', addSlick);

// Team section
$('.carousel-team').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  prevArrow: '<a class="prev arrow fa fa-angle-left"></a>',
  nextArrow: '<a class="next arrow fa fa-angle-right"></a>',
});

// Navbar

const gel = element => document.querySelector(element);
const getHeight = element => gel(element).clientHeight;

let heights = {
  navbar: getHeight('.navbar'),
  banner: getHeight('.banner'),
  about: getHeight('.about'),
  cards: getHeight('#cards'),
  team: getHeight('#team'),
}

const navbar =gel('nav');
const menu = gel('.menu-container');

// Show menu animation
gel('.show-menu').addEventListener('click', () => {
  menu.clientHeight === 0 ?  menu.style.height = '200px' : menu.style.height = '0px' ;
  gel('.navbar-ghost').style.height = heights.navbar + 'px';
})

// Fix navbar to top of the page
document.addEventListener('scroll', event => {
  if (window.scrollY >= heights.banner) {
    if (navbar.className.indexOf('fixed') == -1) {
      gel('.navbar-ghost').style.height = getHeight('.navbar') + 'px';
      navbar.className += ' fixed';
    }
  } else {
    navbar.className = navbar.className.split('fixed').join('');
  }
  
})

var lastScrollTop = 0;
$(window).scroll(function(event){
   var st = $(this).scrollTop();
   if (st > lastScrollTop && gel('nav').clientHeight > 200){
      gel('.show-menu').click();
   } 
   lastScrollTop = st;
});

// Schedule section


let prevEach = '';
[...gel('.schedule').childNodes].map(each => {
  if (each.className === 'title-wrapper') {
    let eachTitle = [...each.childNodes][1].innerText;
    if (eachTitle === prevEach) {
      each.style.display = 'none';
    }
    prevEach = eachTitle;
  }
})

