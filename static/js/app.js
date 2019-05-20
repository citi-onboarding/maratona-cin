$('.carousel').slick({
  slidesToShow: 1,
  dots: true,
  // variableWidth: true,
  autoplay: true,
  autoplaySpeed: 2000,
  customPaging: function (slider, i) {
    return '<div class="dot" id=' + i + "></div>";
  },
  arrows: false,
})

$('.carousel-cards').slick({
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  autoplay: true,
  autoplaySpeed: 2000,
  responsive: [
    {
      breakpoint: 1008,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 600,
      settings: 'unslick',
    },
  ]
});

$(window).resize(() => {
  $('.js-slider').not('.slick-initialized').slick('resize');
});

$(window).on('orientationchange', () => {
  $('.js-slider').not('.slick-initialized').slick('resize');
});