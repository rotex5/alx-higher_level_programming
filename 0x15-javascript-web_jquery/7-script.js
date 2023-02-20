const _$ = window.$;

_$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  _$('div#character').html(data.name);
});
