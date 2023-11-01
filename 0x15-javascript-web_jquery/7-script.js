function func1 (data) {
  $('DIV#character').text(data.name);
}
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', func1);
