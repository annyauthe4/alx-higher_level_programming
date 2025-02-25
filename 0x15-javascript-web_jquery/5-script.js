// Add element to a list on click

$(document).ready(function () {
    $("div#add_item").click(function () {
        $("ul.my_list").append("<li>Item</li>");
    });
});
