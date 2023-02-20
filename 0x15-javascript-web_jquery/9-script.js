const _$ = window.$;

_$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  _$('div#hello').text(data.hello);
});
