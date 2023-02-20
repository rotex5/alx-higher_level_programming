const _$ = window.$;

_$('div#add_item').click(function () {
  const newItem = document.createElement('li');
  newItem.innerHTML = 'Item';

  _$('ul.my_list').append(newItem);
});
