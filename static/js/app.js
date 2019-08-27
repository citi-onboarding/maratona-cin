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
    [...card.childNodes].forEach(text => {
      if (text.clientHeight) {
        childrenHeight += text.clientHeight;
      }
    })
    childrenHeight += 60;
    if (childrenHeight >= maxHeight) {
      maxHeight = childrenHeight;
    }
  });
  [...document.querySelectorAll('.card')].forEach(card => {
    card.style.height = `${maxHeight}px`;
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
    try { carousel.slick('unslick'); } catch (err) { return; };
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

[...gel('.participant-container').parentElement.childNodes].forEach(slide => {
  if (slide.hasChildNodes()) {
    [...slide.childNodes].forEach(participant => {
      if (participant.className === 'participant') {
        let img = participant.querySelector('img');
        setTimeout(() => {
          if (img) {
            img.className = img.clientHeight >= img.clientWidth ? 'portrait' : 'landscape';
          };
        }, 500);
      };
    });
  };
});

// =================================////=====================================//
// Navbar

let navbarAutoOpen = false;

const navbar = gel('.navbar-container');
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
  if (menu.clientWidth > 0 && window.scrollY < getHeight('.banner')) {
    menu.style.transition = 'width 0s';
    menu.style.width = '0px';
    return;
  }
  if (navbarAutoOpen && window.scrollY === getHeight('.banner')) {
    gel('.show-menu').click();
    navbarAutoOpen = false;
  }
  if (menu.clientWidth > 0) {
    gel('.show-menu').click();
  }
});

// Navbar links

[...document.querySelectorAll('section')].forEach(section => {
  $(() => {
    $(`.${section.className}`).not(gel('.navbar')).not(gel('.banner')).not(gel('.about')).css('padding-top', getHeight('.navbar-ghost'));
  });
})

const menus = [...document.querySelectorAll('.menu')]

menus.forEach(navMenu => {
  navMenu.addEventListener('click', event => {
    if (event.target.className && event.target.className !== 'menu') {
      const scrollToView = (eventTarget, callback) => {
        gel(`.${eventTarget.className.split('-link').join('')}`).scrollIntoView(true);
        // callback();
      }
      scrollToView(event.target, () => {
        window.scrollBy(0, -30);
      })
    }
  })
})

// =================================////=====================================//
// Schedule section

let prevEach = '';
let i = 1;
let titleBlue = false;
[...gel('.schedule').childNodes].map(each => {
  if (each.className === 'title-wrapper') {
    let eachTitle = [...each.childNodes][1].innerText;
    if (eachTitle === prevEach) {
      each.style.display = 'none';
      each.className += ' displayNone'
    }
    prevEach = eachTitle;
  }
  if (each.className && each.className.indexOf('displayNone') === -1) {
    if (each.className === 'title-wrapper') {
      if (i % 2 === 0) {
        each.className += ' title-blue';
        titleBlue = true;
      } else titleBlue = false;
      i++;
    }
    if (each.className === 'text-container' && titleBlue) {
      each.className += ' text-blue';
    }
  }
});

$('.schedule-detail-carousel').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  arrows: false,
  fade: true,
  swipe: false,
});

const handleScheduleClick = (target) => {
  gel('.schedule-detail-carousel').querySelectorAll('.slick-slide').forEach((slide, i) => {
    if (slide.getAttribute('data-slide') === target.getAttribute('data-slide')) {
      $('.schedule-detail-carousel').slick('slickGoTo', i);
    }
  })
}

// =================================////=====================================//
// Journey section
let lastestEvent;
let firstFlag = true;
[...gel('.info').childNodes].forEach(year => {
  [...year.childNodes].forEach(eventContainer => {
    if (eventContainer.className === 'event-container' && firstFlag) {
      let eventList = [...eventContainer.childNodes]
      lastestEvent = eventList[1];
      firstFlag = false;
    }
  })
})

$('.carousel-journey').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  arrows: false,
  accessibility: false,
});

$('.carousel-journey').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
  slideIndex = nextSlide + 1;
  $(`div[data-slide=${slideIndex}]`)[0].click();
});

let dataSlideCounter = 1;
[...gel('.info').childNodes].forEach(yearContainer => {
  if (yearContainer.className === 'year-container') {
    let year = yearContainer.querySelector('.event-container').id;
    let yearElement = yearContainer.querySelector('.year');
    let yearColor = window.getComputedStyle(yearElement, null).getPropertyValue("background-color");

    [...document.querySelectorAll('.event')].forEach((event) => {
      if (event.className.indexOf(year) !== -1) {
        event.style.borderColor = yearColor;
      }
    });

    [...yearContainer.querySelector('.event-container').childNodes].forEach((event) => {
      if (event.className && event.className.indexOf('event-dot') !== -1) {
        event.setAttribute('data-slide', dataSlideCounter);
        dataSlideCounter++;
      }
    })
  }
});

$('div[data-slide]').click(function (e) {
  e.preventDefault();
  var slideno = $(this).data('slide');
  $('.carousel-journey').slick('slickGoTo', slideno - 1);
});


[...document.querySelectorAll('div.event-dot')].forEach(eventDot => {
  eventDot.addEventListener('click', () => {
    [...document.querySelectorAll('div.event-dot')].forEach(dot => {
      if (dot.className.indexOf('active')) {
        dot.className = dot.className.split('active').join('');
      }
    })
    eventDot.className += ' active';
  })
})


$(document).ready(() => {
  lastestEvent.click();
})

// =================================////=====================================//
// Testimonials section

$('.carousel-testimonials').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  vertical: true,
  swipe: false,
  dots: false,
  arrows: false,
  autoplay: true,
  autoplaySpeed: 3000,
  pauseOnFocus: false,
  pauseOnHover: false,
});

// Organize by colors

const invert = subj => {
  subj.className.indexOf('invert') === -1 ? subj.className += ' invert' : subj.className.split('invert').join('');
}
let prevSlide;
let firstClone = false;
let j = 0;
[...gel('.carousel-testimonials').querySelector('.slick-list').querySelector('.slick-track').childNodes].forEach(each => {
  if (each.className.indexOf('cloned') !== -1 && prevSlide === 'real') {
    firstClone = true;
  }
  if (each.className.indexOf('cloned') === -1 || firstClone) {
    if (j % 2 !== 0) {
      invert(each);
    }
    if (j % 3 === 1) {
      each.className += ' blue-message';
    }
    if (j % 3 === 2) {
      each.className += ' red-message';
    }
    if (j % 3 === 0) {
      each.className += ' yellow-message';
    }
    prevSlide = 'real';
    j++;
  } else {
    prevSlide = 'cloned';
    firstClone = false;
  }
})

// =================================////=====================================//
// News Section

$('.carousel-news').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: true,
  customPaging: (slider, i) => `<div class="dot" id=${i}></div>`,
  arrows: false,
});

// Getting favicon.ico from pages

const logoUrls = {
  'www.youtube.com': 'http://assets.stickpng.com/thumbs/580b57fcd9996e24bc43c545.png',
  'medium.com': 'http://www.stickpng.com/assets/images/5841c47ba6515b1e0ad75aa3.png',
  'pt-br.facebook.com': 'http://www.stickpng.com/assets/images/584ac2d03ac3a570f94a666d.png',
  'www.instagram.com': 'http://pluspng.com/img-png/instagram-png-instagram-png-logo-1455.png',
  'twitter.com': 'http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c53e.png',
  'br.pinsterest.com': 'http://www.stickpng.com/assets/images/580b57fcd9996e24bc43c52e.png',
  'www.ufpe.br': 'https://www3.ufpe.br/ufpenova/images/brasao/logoufpe.jpg',
  'www2.cin.ufpe.br': 'https://www2.cin.ufpe.br/site/uploads/arquivos/18/20120530161145_marca_cin_2012_producao.jpg',
  'veja.abril.com.br':'https://seeklogo.com/images/E/Editora_Abril-logo-D63B707335-seeklogo.com.png',
};

[...gel('.new-container').parentElement.childNodes].map(slide => {
  [...slide.childNodes].map(news => {
    if (news.href) {
      const siteName = news.href.split('/')[2];
      const siteHome = news.href.split('/').slice(0, 3).join('/');
      if (siteName in logoUrls) {
          news.querySelector('img').src = logoUrls[siteName];
      } else news.querySelector('img').src = `${siteHome}/favicon.ico`;
    }
  })
})

// =================================////=====================================//
// Hall of Fame section

$('.carousel-fame').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  dots: false,
  prevArrow: '<a class="prev arrow fa fa-angle-left"></a>',
  nextArrow: '<a class="next arrow fa fa-angle-right"></a>',
});

[...gel('.famous-container').parentElement.childNodes].forEach(slide => {
  if (slide.hasChildNodes()) {
    [...slide.childNodes].forEach(famous => {
      if (famous.className === 'famous') {
        let img = famous.querySelector('img');
        setTimeout(() => {
          if (img) {
            img.className = img.clientHeight >= img.clientWidth ? 'portrait' : 'landscape';
          };
        }, 500);
      };
    });
  };
});

// =================================////=====================================//
// Paretners Section
$('.carousel-partners').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  initialSlide: 1,
  swipe: false,
  accessibility: false,
  centerMode: true,
  centerPadding: 0,
  dots: false,
  infinite: false,
  prevArrow: '<a class="prev arrow fa fa-angle-left"></a>',
  nextArrow: '<a class="next arrow fa fa-angle-right"></a>',
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        centerMode: false,
      }
    },
  ],
});

// Add class by resolution
[...gel('.partner-container').parentElement.childNodes].forEach(slide => {
  let img = slide.querySelector('.image-container').querySelector('img');
  img.clientHeight >= img.clientWidth ? img.className += ' portrait' : img.className += ' landscape'
});

// =================================////=====================================//
// Study Section

[...gel('.link-wrapper').childNodes].forEach(container => {
  [...container.childNodes].forEach(table => {
    if (table.className && table.className.indexOf('study-table') !== -1) {
      const img = table.querySelector('.image-container').querySelector('img');
      const link = table.querySelector('a').href;
      if (link) {
        const siteName = link.split('/')[2];
        const siteHome = link.split('/').slice(0, 3).join('/');
        if (siteName in logoUrls) {
            img.src = logoUrls[siteName];
        } else img.src = `${siteHome}/favicon.ico`;
      }
    }
  })
})