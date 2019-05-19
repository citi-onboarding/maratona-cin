$(document).ready(() => {
  $('.carousel').slick({
    slidesToShow: 1,
    dots: true,
    customPaging: function (slider, i) {
      return '<div class="dot" id=' + i + "></div>";
    },
    arrows : false,
  });
});