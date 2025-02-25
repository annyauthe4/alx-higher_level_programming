// Lists movie title in an API

$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
        $.each(data.results, function (index, movie) {
            $("ul#list_movies").append("<li>" + movie.title + "</li>";
        });
    });
});
