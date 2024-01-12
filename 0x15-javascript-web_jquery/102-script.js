// script that fetches & prints how to say "Hello" depending on the language.
$(document).ready(function () {
	// Add a click event handler to the button with id 'btn_translate'
	$("#btn_translate").click(function () {
		// Get the language code from the input with id 'language_code'
		var languageCode = $("#language_code").val();

		// Make an AJAX GET request to the API with the language code
		$.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
			// Display the translation of "Hello" in the div with id 'hello'
			$("#hello").text(data.hello);
		});
	});
});
