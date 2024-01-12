// script that toggles the class of an element when clicked
$(document).ready(function(){
	// div tag toggle_header handler
	$("#toggle_header").click(function(){
		// select & toggles header color
		$("header").toggleClass("red green");
	});
});
