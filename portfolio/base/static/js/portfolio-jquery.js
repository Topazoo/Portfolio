
function getCookie(name) {
    /* Get a cookie */

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
    /* Set CSRF token */

    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$(document).ready(function() {
    /* POST to smartwatch messaging server */

    $("#snd-msg").click(function() {
		token = String(getCookie('csrftoken'));
		message = String($('#message').val());
		number = String($('#phone').val());
		carrier = String($('#carrier').val());
		from_number = "4152094084";
        
        /* Send AJAX POST request */
		$.ajax({
				"type": "POST",
				"dataType": "json",
				"url": '/send_message',
				"data": {'message': message, 'to_number': number, 'from_number': from_number, 'carrier': carrier, 'csrfmiddlewaretoken': token},
                /* Message on success */
                "success": function(response) {
					alert('Your message has been sent'); 
                },
                /* Message on failure */
				"error": function(response) {
					alert('Failed to send message'); 
				},
		});
    });
    
    var slideIndex = 1;
    showSlides(slideIndex);

    // Next/previous controls
    function plusSlides(n) {
    showSlides(slideIndex += n);
    }

    // Thumbnail image controls
    function currentSlide(n) {
    showSlides(slideIndex = n);
    }

    function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slides");
    if (n > slides.length) 
        {slideIndex = 1} 
    if (n < 1) 
        {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    if(slides)
        slides[slideIndex-1].style.display = "block"; 
    }
});

