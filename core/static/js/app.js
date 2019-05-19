$(document).ready(() => {
  $('.carousel').slick({
    slidesToShow: 1,
    dots: true,
    // variableWidth: true,
    autoplay: true,
    autoplaySpeed: 2000,
    customPaging: function (slider, i) {
      return '<div class="dot" id=' + i + "></div>";
    },
    // arrows : false,
  });
});