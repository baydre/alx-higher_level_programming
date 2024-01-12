// script that adds a <li> element to a list when clicked by user.
$(document).ready(function(){
	// #add_item handler
	$("#add_item").click(function(){
		// adds new <li> element
		var newListItem = $("<li>Item</li>");
		// append newly added <li> to UL.my_list
		$("ul.my_list").append(newListItem);
	});
});
