const _$ = window.$;

_$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const values = data.results;

  for (let i = 0; i < values.length; i++) {
    const newItem = document.createElement('li');
    newItem.innerHTML = values[i].title;
    _$('ul#list_movies').append(newItem);
  }
});
