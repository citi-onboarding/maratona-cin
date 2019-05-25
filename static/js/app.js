const gel = element => document.querySelector(element);
const getHeight = element => gel(element).clientHeight;

// =================================////=====================================//
// About section

$('.carousel-about').slick({
  slidesToShow: 1,
  dots: true,
  autoplay: true,
  autoplaySpeed: 2000,
  customPaging: (slider, i) => `<div class="dot" id=${i}></div>`,
  arrows: false,
});

// =================================////=====================================//
// Cards section

const initCards = () => { 

  let maxHeight = 0;
  
  [...document.querySelectorAll('.card')].forEach(card => {
    let childrenHeight = 0;
    console.log('===============****');
    [...card.childNodes].forEach(text => {
      if (text.clientHeight) {
        childrenHeight += text.clientHeight;
        console.log(text.clientHeight);
      }
    })
    console.log('===============()()()');
    console.log(childrenHeight);
    childrenHeight += 60;
    console.log(childrenHeight);
    
    if (childrenHeight >= maxHeight) {
      maxHeight = childrenHeight;
    }
    
    [...document.querySelectorAll('.card')].forEach(card => {
      // gel('.carousel-cards').style.height = `${maxHeight}px`
      card.style.minHeight = `${maxHeight}px`;
      card.style.maxHeight = `${maxHeight}px`;
      console.log('==============++++');
      console.log(maxHeight);
      console.log(card.clientHeight);
      console.log('==============----');
    });
  });

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
  } else if (carousel.slick) {
    try {carousel.slick('unslick');} catch(err) {return;};
  }
};

window.addEventListener('resize', initCards);
window.addEventListener('load', initCards);

// =================================////=====================================//
// Team section

$('.carousel-team').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  prevArrow: '<a class="prev arrow fa fa-angle-left"></a>',
  nextArrow: '<a class="next arrow fa fa-angle-right"></a>',
});

// =================================////=====================================//
// Navbar

let heights = {
  navbar: getHeight('.navbar'),
  banner: getHeight('.banner'),
  about: getHeight('.about'),
  cards: getHeight('#cards'),
  team: getHeight('#team'),
}

const navbar = gel('nav');
const menu = gel('.menu-container');

// Show menu animation
gel('.show-menu').addEventListener('click', () => {
  menu.clientHeight === 0 ? menu.style.height = '200px' : menu.style.height = '0px';
})

// Fix navbar to top of the page
document.addEventListener('scroll', () => {
  if (window.scrollY >= getHeight('.banner')) {
    if (navbar.className.indexOf('fixed') == -1) {
      gel('.navbar-ghost').style.height = getHeight('.navbar') + 'px';
      navbar.className += ' fixed';
    }
  } else {
    navbar.className = navbar.className.split('fixed').join('');
  }
  gel('.navbar-ghost').style.height = heights.navbar + 'px';
})

// Hide navbar if page is scrolled down
let lastScrollTop = 0;
document.addEventListener('scroll', () => {
  let st = $(this).scrollTop();
  if (st > lastScrollTop && gel('nav').clientHeight > 200) {
    gel('.show-menu').click();
  }
  lastScrollTop = st;
});