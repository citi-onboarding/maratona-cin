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
    // console.log('===============****');
    [...card.childNodes].forEach(text => {
      if (text.clientHeight) {
        childrenHeight += text.clientHeight;
        // console.log(text);
        // console.log(`text height: ${text.clientHeight}`);
        // console.log(`childrenHeight: ${childrenHeight}`);
        // console.log('===================&&&&');
      }
    })
    // console.log('===============()()()');
    childrenHeight += 60;
    // console.log(`childrenHeight + 60: ${childrenHeight}`);
    
    if (childrenHeight >= maxHeight) {
      maxHeight = childrenHeight;
    }
    
  });
  [...document.querySelectorAll('.card')].forEach(card => {
    card.style.height = `${maxHeight}px`;
    // console.log('==============++++');
    // console.log(`maxHeight: ${maxHeight}`);
    // console.log(card);
    // console.log(`card height: ${card.clientHeight}`);
    // console.log('==============----');
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
$(document).ready(initCards);

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

let navbarAutoOpen = false;

const navbar = gel('nav');
let navbarHeight = getHeight('.navbar')

// Fix navbar to top of the page
document.addEventListener('scroll', () => {
  if (window.scrollY >= getHeight('.banner')) {
    if (navbar.className.indexOf('fixed') === -1) {
      gel('.navbar-ghost').style.height = getHeight('.navbar') + 'px';
      navbar.className += ' fixed';
    }
  } else {
    navbar.className = navbar.className.split('fixed').join('');
  }
  gel('.navbar-ghost').style.height = navbarHeight + 'px';
})

const menu = gel('.menu-container-side');

// Show menu animation
gel('.show-menu').addEventListener('click', () => {
  // If user is above navbar
  menu.style.transition = 'width 0.5s';
  if (window.scrollY < getHeight('.banner')) {
    window.scrollTo(0, getHeight('.banner'));
    navbarAutoOpen = true;
  } else {
    menu.style.marginTop = `${getHeight('.navbar')}px`;
    menu.style.width = menu.clientWidth === 0 ? '60%' : '0px';
  }
})

// Hide navbar if page is scrolled down
document.addEventListener('scroll', () => {
  if(menu.clientWidth > 0 && window.scrollY < getHeight('.banner')) {
    menu.style.transition = 'width 0s';
    menu.style.width = '0px';
    return;
  }
  if(navbarAutoOpen && window.scrollY === getHeight('.banner')) {
    gel('.show-menu').click();
    navbarAutoOpen = false;
  }
  if(menu.clientWidth > 0) {
    gel('.show-menu').click();
  }
});

// Navbar links


menu.addEventListener('click', event => {
  const heights = {
    banner: getHeight('.banner'),
    navbar: getHeight('.navbar-ghost'),
    about: getHeight('.about'),
    cards: getHeight('section.cards') + 70,
    team: getHeight('section.team'),
    schedule: getHeight('.schedule'),
  };

  let height = 0;
  let heightSum = 0;
  let eventClass = event.target.className;

  if(eventClass.split(' ')[0] !== 'menu') {
    Object.entries(heights).map( each => {
      each[0] === event.target.className ? heightSum = height : height += each[1];
      console.log(`${each[0]}: ${each[1]}`);
    });
    heightSum -= heights.navbar;
    window.scrollTo(0, heightSum);
    menu.style.width = '0px';
  }
})