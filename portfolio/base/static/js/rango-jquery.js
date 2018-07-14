
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$(document).ready(function() {
    $("#snd-msg").click(function() {
		message = prompt("Please enter a message to send");
		number = prompt("Please enter a number to send it to");
		carrier= prompt("Please enter the carrier (e.g. Verizon)");
		from_number = "4152094084";
		token = getCookie('csrftoken');
		
		$.ajax({
				"type": "POST",
				"dataType": "json",
				"url": '/send_message',
				"data": {'message': message, 'to_number': number, 'from_number': from_number, 'carrier': carrier, 'csrfmiddlewaretoken': token},
				"success": function(response) {
					if(response.code == 'success') { 
						alert('Your message has been sent'); 
					}	
					else { 
						alert('Message failed to send'); 
					}
				},
				"error": function(response) {
					alert ('Message failed to send');
				},
		});
	});
});