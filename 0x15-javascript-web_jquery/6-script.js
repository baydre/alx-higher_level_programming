// script that updates the text of the header.
$(document).ready(function(){
	// id 'update_header' handler
	$("#update_header").click(function () {
		// Select the 'header' element and update its text
		$("header").text("New Header!!!");
	});
});
