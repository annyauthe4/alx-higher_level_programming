// Fetch character name from API

$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (res) {
        $("div#character").text(res.name);
    });
});
