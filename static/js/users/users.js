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

function checkCategory(resp){
    // console.log(resp.value)
    if(resp.value==''){
        return false
    }
    fetch('/category_data_api')
    .then((resp) => resp.json())
    .then(function (data) {
        const result = Object.keys(data[0]).reduce((obj, key) => {
            obj[key] = data.map(_ => _[key]);
            return obj;
        }, {});
    var subCategoryName = result.subCategoryName
    if(! subCategoryName.includes(resp.value)){
        alert('Please select the category from options')
        resp.value=''
    }
    
    })
}

function fecthCategory(){
    $('#category_list').empty()
    var datalist = $('#category_list')
    fetch('/category_data_api')
    .then((resp) => resp.json())
    .then(function (data) {
        const result = Object.keys(data[0]).reduce((obj, key) => {
            obj[key] = data.map(_ => _[key]);
            return obj;
        }, {});
        // var subCategoryName = [...new Set(result.subCategoryName)]
    
        var subCategoryName = result.subCategoryName
        var serviceCategory = result.serviceCategory
        for(var i = 0;i<subCategoryName.length;i++){
            var element = document.createElement("option");
            element.innerText = serviceCategory[i];
            element.setAttribute('value',subCategoryName[i])
            datalist.append(element);
        }
    })
}

function fetchVolunteer(resp){
    if(resp.value==''){
        $('#volunteer_table').html('');

        return false
    }
    fetch('/category_data_api')
    .then((resp) => resp.json())
    .then(function (data) {
        const result = Object.keys(data[0]).reduce((obj, key) => {
            obj[key] = data.map(_ => _[key]);
            return obj;
        }, {});
    var subCategoryName = result.subCategoryName
    if(subCategoryName.includes(resp.value)){
        $('#volunteer_table').html('');
        fetch('/volunteer/category/'+resp.value)
        .then((resp) => resp.json())
        .then(function (data) {
            // console.log(data)
            const result_child_1 = Object.keys(data[0]).reduce((obj, key) => {
                obj[key] = data.map(_ => _[key]);
                return obj;
            }, {});
            var username = result_child_1.username
            var id = result_child_1.id
            var phone_number = result_child_1.phone_number
            var ratings = result_child_1.ratings
            var is_active = result_child_1.is_active
            var temp_html=`<div class="card-header" style="display: flex;justify-content: space-between;align-items: center;">
                    <h5 class="mb-0">Volunteer's</h5>
                    <form class="form-inline">
                        <input class="form-control" type="search" placeholder="Search Volunteer" aria-label="Search" id="search" style="background: aliceblue;border: 1px solid;">
                    </form>
                    </div><div class="table-responsive">
                    <table class="table table-hover table-nowrap">
                        <thead class="thead-light">
                            <tr>
                                <th scope="col">Name</th>
                                <th scope="col">Ratings</th>
                                <th scope="col">Status</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody id="tbody">`
            
            for(var i=0;i<=username.length-1;i++){
                var temp_tr = `<tr class="tr">
                <td>
                    <img alt="..." src="https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3&w=256&h=256&q=80" class="avatar avatar-sm rounded-circle me-2">
                    <a class="text-heading font-semibold" href="#">
                        ${username[i]}
                    </a>
                </td><td>
                    <div class="star-ratings">
                    <div class="fill-ratings" style="width: ${(ratings[i]*100)/5}%;">
                    <span>🟊🟊🟊🟊🟊</span>
                    </div>
                    <div class="empty-ratings">
                    <span>🟊🟊🟊🟊🟊</span>
                    </div>
                </div>
                    
                </td><td>
                    <span class="badge badge-lg badge-dot">
                        <i class="bg-success"></i>Scheduled
                    </span>
                </td> <td class="text-end">
                    <button type="button" id=${id[i]} class="btn btn-sm btn-neutral volt-btn" onclick="volunteerSelect(this)">Select
                    </button>
                </td>`
                temp_html+=temp_tr
            }
            temp_end=`</tbody></table></div>`
            temp_html+=temp_end
            $('#volunteer_table').append(temp_html)
        })
       
    }
    else{
        $('#volunteer_table').html('');

    }   
    })
}

function volunteerSelect(resp){
    $('.volt-btn').html('Select')
    $('.volt-btn').removeClass('activated')
    $('.volt-btn').css("background-color", "#fff")
    $(resp).html('Selected')
    $(resp).css("background-color", "yellow")
    $(resp).addClass("activated")
}




$('#user_submit_request_btn').click(function (e) {
    e.preventDefault();
    // console.log($('#category').val())
    if($('#pincode').val()==''){
        alert("Please Enter Pincode")
        return false
    }
    if($('#category').val()==''){
        alert("Please select value from drop down")
        return false
    }
    
    var c = getCookie('csrftoken');
    var formData = new FormData($('#service_request_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    try{
        formData.append('volunteer', $('.activated').attr('id'))
    }
    catch(err) {
        formData.append('volunteer','')
    }
    $.ajax({
        type: 'POST',
        url:  '/user_request_submit',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if (json.message==200){
                alert('Request has been submitted successfully')
                window.location='/dashboard'
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


// Load first 5 data

$.ajax({
    url:  '/load_request_data/0',
    success: function (data) {
        var json_data = JSON.parse(data)
        
        var data_length = json_data.length
        if(data_length>0){
        var temp_html = `<table class="table table-hover table-nowrap">
                        <thead class="thead-light">
                            <tr>
                                <th scope="col">Request No</th>
                                <th scope="col">Volunteer Name</th>
                                <th scope="col">Otp</th>
                                <th scope="col">Requested Date</th>
                                <th scope="col">Service</th>
                                <th scope="col">Status</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody id="data_body">`
        for(var i=0;i<=data_length-1;i++){
            
            // console.log(`{{${json_data[i].volunteer}|volunteerCheck}}`)
            if(json_data[i].requestStatus){
                if(json_data[i].requestStatus['statusName']=='NEW'){
                    var status = `<button type="button" class="btn btn-success btn-sm" disabled>NEW</button>`
                }
                else if(json_data[i].requestStatus['statusName']=='ASSIGNED'){
                    var status = `<button type="button" class="btn btn-primary btn-sm" disabled>ASSIGNED</button>`

                }
                else if(json_data[i].requestStatus['statusName']=='INPROGRESS'){
                    var status = `<button type="button" class="btn btn-info btn-sm" disabled>INPROGRESS</button>`

                }
                else if(json_data[i].requestStatus['statusName']=='PENDING'){
                    var status = `<button type="button" class="btn btn-warning btn-sm" disabled>PENDING</button>`

                }
                else if(json_data[i].requestStatus['statusName']=='RESOLVED'){
                    var status = `<button type="button" class="btn btn-danger btn-sm" disabled>RESOLVED</button>`

                }
                else if(json_data[i].requestStatus['statusName']=='CLOSED'){
                    var status = `<button type="button" class="btn btn-secondary btn-sm" disabled>CLOSED</button>`

                }
            }
            else{
                var status = `N/A`

            }
            var temp_tr = `<tr>
            <td>
            <b>${json_data[i].unique_no}</b> 

            </td>
            <td>
                <img alt="..." src="https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3&w=256&h=256&q=80" class="avatar avatar-sm rounded-circle me-2">
                <a class="text-heading font-semibold" href="#">
                    ${json_data[i].volunteer? `${json_data[i].volunteer['username']}` : 'N/A'} 
                </a>
            </td>
            <td>
                ${json_data[i].taskOtp? `Start: <b style="color:purple;">${json_data[i].taskOtp['start_otp']}</b> <br>End: <b style="color:purple;">${json_data[i].taskOtp['end_otp']!=null ? json_data[i].taskOtp['end_otp'] :''} </b> ` : 'N/A' } 
                
            </td>
            <td>
                ${json_data[i].requestCreatedOn}

            </td>
            <td>
                ${json_data[i].subCategory.subCategoryName}

            </td>
            <td>
            ${status} 

            </td>
            <td class="text-end">
                <a href="view_user_request/${json_data[i].id}" class="btn btn-sm btn-neutral">View</a>
                
            </td>
        </tr>
        `
        temp_html+=temp_tr
        }
        var temp_end = `</tbody></table>`
        temp_html+=temp_end
        $('#user_request_table').append(temp_html)
    }
    },
    error: function (xhr, errmsg, err) {
        console.log(xhr.status + ":" + xhr.responseText)
    }
})

var offset=0;
try{
var myDiv = document.getElementById("user_request_table");
myDiv.addEventListener("scroll",function(e)
{
    e.preventDefault();
    
    if(myDiv.scrollTop+myDiv.clientHeight<=myDiv.scrollHeight){
        offset+=10

        $.ajax({
            url:  '/load_request_data/'+offset,
            success: function (data) {
                var json_data = JSON.parse(data)
                var data_length = json_data.length
                for(var i=0;i<=data_length-1;i++){
                    if(json_data[i].requestStatus){
                        if(json_data[i].requestStatus['statusName']=='NEW'){
                            var status = `<button type="button" class="btn btn-success btn-sm" disabled>NEW</button>`
                        }
                        else if(json_data[i].requestStatus['statusName']=='ASSIGNED'){
                            var status = `<button type="button" class="btn btn-primary btn-sm" disabled>ASSIGNED</button>`
        
                        }
                        else if(json_data[i].requestStatus['statusName']=='INPROGRESS'){
                            var status = `<button type="button" class="btn btn-info btn-sm" disabled>INPROGRESS</button>`
        
                        }
                        else if(json_data[i].requestStatus['statusName']=='PENDING'){
                            var status = `<button type="button" class="btn btn-warning btn-sm" disabled>PENDING</button>`
        
                        }
                        else if(json_data[i].requestStatus['statusName']=='RESOLVED'){
                            var status = `<button type="button" class="btn btn-danger btn-sm" disabled>RESOLVED</button>`
        
                        }
                        else if(json_data[i].requestStatus['statusName']=='CLOSED'){
                            var status = `<button type="button" class="btn btn-secondary btn-sm" disabled>CLOSED</button>`
        
                        }
                    }
                    else{
                        var status = `N/A`
        
                    }
                    var temp_tr = `<tr>
                    <td>
                        <b>${json_data[i].unique_no}</b> 
                    </td>
                    <td>
                        <img alt="..." src="https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=3&w=256&h=256&q=80" class="avatar avatar-sm rounded-circle me-2">
                        <a class="text-heading font-semibold" href="#">
                            ${json_data[i].volunteer? `${json_data[i].volunteer['username']}` : 'N/A'} 
                        </a>
                    </td>
                    <td>
                        ${json_data[i].taskOtp? `Start: <b style="color:purple;">${json_data[i].taskOtp['start_otp']}</b> <br>End: <b style="color:purple;">${json_data[i].taskOtp['end_otp']!=null ? json_data[i].taskOtp['end_otp'] :''} </b> ` : 'N/A' } 
                    </td>
                    <td>
                        ${json_data[i].requestCreatedOn}
                    </td>
                    <td>
                    ${json_data[i].subCategory.subCategoryName}

                    
                    </td>
                    <td>
                        ${status} 
                    </td>
                    <td class="text-end">
                        <a href="view_user_request/${json_data[i].id}" class="btn btn-sm btn-neutral">View</a>
                        
                    </td>
                </tr>
                `
                $('#data_body').append(temp_tr)
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ":" + xhr.responseText)
            }
        })
    }
});

}
catch(err){

}

$('#user_view_request_submit_btn').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#view_request_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    formData.append('status', document.getElementById('status').value)
    
    try{
        console.log(document.getElementById('feedback').value)
        formData.append('user_feedback',document.getElementById('feedback').value)
        formData.append('user_rating',document.getElementById('rating').value)
    }
    catch(err){
        formData.append('user_feedback','')
        formData.append('user_rating','')
    }
    $.ajax({
        type: 'POST',
        url:  '/user_view_request_submit/'+parseInt(window.location.pathname.split('/')[2]),
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




$('#profile_save_btn').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#profile_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    
    $.ajax({
        type: 'POST',
        url:  '/user_profile_submit',
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
