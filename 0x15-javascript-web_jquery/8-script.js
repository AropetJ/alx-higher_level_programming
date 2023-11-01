function func1 (data) {
    $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
}
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', func1);
