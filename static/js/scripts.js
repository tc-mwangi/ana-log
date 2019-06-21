

$(document).ready(function(){
    // show/hide report
    $("#extra-content").hide();
    $("#toggle-content").click(function(){
        $("#extra-content").show();
        $("#toggle-content").hide();
    });

    //Django setup for accepting ajax requests.
    // Cookie obtainer for Django
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    // Setup ajax connections safetly
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //Django Ajax Call Setup
    $.ajax({
        url: '/my_ajax_request/',
        data: {
        'message': 'I want an AJAX response'
    },
        dataType: 'json',
        type: 'POST',
        success: function(data) {
        if (data.is_valid) {
            console.log(data.response);
        } else {
            console.log("You didn't message : I want an AJAX response");
        }
        }
    });

    // Render clock
    // Declare constants
    const HOURHAND = document.querySelector("#hour");
    const MINUTEHAND = document.querySelector("#minute");
    const SECONDHAND = document.querySelector("#second");
    const HOURMARKS = document.querySelector("#hour-marks")


    function run_the_clock(){
    var date = new Date();
    let hr = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();
    console.log("Hour: "+hr+ " Minute: "+ min + " Second: "+ sec);

    let hrPosition = hr*360/12 + ((min * 360/60)/12) ;
    let minPosition = (min * 360/60) + (sec* 360/60)/60;
    let secPosition = sec * 360/60;

    //Then we need to apply these numbers as degrees in the inline styles for transform on each of the objects.
    HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
    MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
    SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";
    }


    var interval = setInterval(run_the_clock, 1000);


// change background color of wall
// #43aa8b for start, #b2b09b for stop
$(function() {
    var colors = ["#43aa8b", "#b2b09b"];
     
    setInterval(function() { 
        var changewall = Math.floor(Math.random() * colors.length);
        var selectedcolor = colors[changewall];
        $(".clockbox").css("background",selectedcolor);
    }, 3000);
})

//  generate random number for start task
    function setRandom() {
        document.getElementById('start').innerHTML = Math.random() * 20 | 0;
    }
    setRandom();
    setInterval(setRandom, 30000); 


    //  generate random number for stop task
    function setRandom() {
        document.getElementById('stop').innerHTML = Math.random() * 5 | 0;
    }
    setRandom();
    setInterval(setRandom, 40000); 


});



















