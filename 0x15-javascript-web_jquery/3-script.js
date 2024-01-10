// script that adds class red to an when clicked by the user.
$(document).ready(function(){
	// div tag red_header handler
	$("#red_header").click(function(){
		// select & updates header color 
		$("header").addClass("red");
	});
});
