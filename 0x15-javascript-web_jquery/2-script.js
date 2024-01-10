// script that updates the text color of an element when the user clicks on the tag.
$(document).ready(function(){
	// div tag red_header handler
	$("#red_header").click(function(){
		// select & updates header color
		$("header").css("color", "#FF0000")
	});
});
