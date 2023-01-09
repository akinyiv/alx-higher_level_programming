const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  for (const i of data.results) {
    const name = i.title;
    $('#list_movies').append('<li>' + name + '<li/>');
  }
});
