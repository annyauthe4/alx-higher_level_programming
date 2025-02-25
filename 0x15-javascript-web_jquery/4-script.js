/*
oggles the class of the <header> element when the user clicks on the tag
DIV#toggle_header.
The <header> element must always have one class: red or green, never both
in the same time and never empty.
*/


$(document).ready(function () {
    $("div#toggle_header").click(function () {
        if ($("header").hasClass("red") {
            $("header").removeClass("red").addClass("green");
	} else {
            $("header").removeClass("green").addClass("red");
        }
    });
});
