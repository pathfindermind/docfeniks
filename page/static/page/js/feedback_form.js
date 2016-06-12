$('.js-form').on('submit', 'form', function (event) {
  event.preventDefault();
  var $this = $(this);
  $.ajax({
    url: $this.attr('action'),
    type: $this.attr('method'),
    data: $this.serialize(),
    success: function (new_html) {
      $this.closest('.js-form').html(new_html);
    },
    error: function () {
      alert('Произошла ошибка, попробуйте позже.');
    }
  })
})
