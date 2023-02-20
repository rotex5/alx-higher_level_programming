const _$ = window.$;

window.onload = function () {
  _$('input#btn_translate').on('click', function () {
    const value = _$('input#language_code').val();
    _$.get('https://fourtonfish.com/hellosalut/?lang=' + value, function (data) {
      _$('div#hello').text(data.hello);
    });
  });
};
