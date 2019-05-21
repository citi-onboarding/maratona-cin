$('.carousel').slick({
  slidesToShow: 1,
  dots: true,
  autoplay: true,
  autoplaySpeed: 2000,
  customPaging: function (slider, i) {
    return '<div class="dot" id=' + i + "></div>";
  },
  arrows: false,
})

const slick = () => {
  let carousel = $('.carousel-cards');
  if (window.innerWidth <= 960) {
    carousel.slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      dots: true,
      arrows: false,
      customPaging: function (slider, i) {
        return '<div class="dot" id=' + i + "></div>";
      },
    });
  } else if (carousel.slick){
    carousel.slick('unslick');
  }
}

window.addEventListener('resize', slick);
window.addEventListener('load', slick);