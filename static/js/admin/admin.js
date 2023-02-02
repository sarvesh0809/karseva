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

// user profil page udate and save
$('#userprofile_edit').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#profile_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    $.ajax({
        type: 'POST',
        url:  '/user_profile_edit',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if (json.message==200){
                alert('Saved Successfully')
                location.reload();
            }
            else{
                alert('It Seems some error has occured')
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})


// volunteer profile page udate and save
$('#volunteerprofile_edit').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#profile_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    $.ajax({
        type: 'POST',
        url:  '/volunteer_profile_edit',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if (json.message==200){
                alert('Saved Successfully')
                location.reload();
            }
            else{
                alert('It Seems some error has occured')
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})
