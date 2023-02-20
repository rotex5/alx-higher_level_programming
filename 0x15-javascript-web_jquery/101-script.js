const _$ = window.$;

  window.onload = function () {
  _$('div#add_item').click(function () {
    const newItem = document.createElement('li');
    newItem.innerHTML = 'Item';

    _$('ul.my_list').append(newItem);
  });

  _$('div#remove_item').on('click', function () {
    _$('ul.my_list li:last-child').remove();
  });

  _$('div#clear_list').click(function () {
    _$('ul.my_list').empty();
  });
};
