const _$ = window.$;

window.onload = function () {
  _$('input#btn_translate').on('click', function () {
    hello();
  });
  _$('input#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      hello();
    }
  });
};

function hello () {
  const value = _$('input#language_code').val();
  _$.get('https://fourtonfish.com/hellosalut/?lang=' + value, function (data) {
    _$('div#hello').text(data.hello);
  });
}
