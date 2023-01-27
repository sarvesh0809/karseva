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

function volunteerName_list(){
    $('#volunteerName_list').empty() // To empty datalist
    var datalist = $('#volunteerName_list')
    fetch('/volunteerName_category')
    .then((resp) => resp.json())
    .then(function (data) {
        const result = Object.keys(data[0]).reduce((obj, key) => {
            obj[key] = data.map(_ => _[key]);
            return obj;
        }, {});
        var volunteeruserName = result.username
        var volunteerphno = result.primaryphonenumber
        var volunteerName = result.first_name

        for(var i = 0;i<volunteeruserName.length-1;i++){
            var element = document.createElement("option");
            element.innerText = volunteerName[i]+' '+volunteerphno[i];
            element.setAttribute('value',volunteeruserName[i])
            datalist.append(element);
        }
    })
}


$('#coordinator_form_submit').click(function (e) {
    e.preventDefault();

    if($('#pincode').val()==''){
        alert("Please Enter Pincode")
        return false
    }
    if($('#volunteerName').val()==''){
        alert("Please select value from drop down")
        return false
    }
    
    var c = getCookie('csrftoken');
    var formData = new FormData($('#coordinator_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    
    $.ajax({
        type: 'POST',
        url:  '/task_edit_submit',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if (json.message==200){
                alert('Request has been submitted successfully')
                window.location.reload()
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


