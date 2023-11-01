function func1 (data) {
  $('DIV#hello').text(data.hello);
}

function func2 () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', func1);
}

$('document').ready(func2);
