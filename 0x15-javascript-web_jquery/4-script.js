const _$ = window.$;

_$('div#toggle_header').click(function () {
  if (_$('header').hasClass('red')) {
    _$('header').removeClass('red');
    _$('header').addClass('green');
  } else {
    _$('header').removeClass('green');
    _$('header').addClass('red');
  }
});
