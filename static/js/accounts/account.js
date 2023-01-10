function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({       
    headers: { "X-CSRFToken": getCookie("csrftoken") }

});

$('.signupform').submit(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData(this);
    formData.append('csrfmiddlewaretoken', c)
    formData.append('userType',$('.active-case').html().toUpperCase())
    $.ajax({
        type: 'POST',
        url:  '/userSignup/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            alert(json.message)
        },   
        error: function (xhr, errmsg, err) {
            
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})


$('.loginform').submit(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData(this);
    formData.append('csrfmiddlewaretoken', c)
    $.ajax({
        type: 'POST',
        url:  '/userLogin/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if (json.message==200){
                window.location='/dashboard'
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})