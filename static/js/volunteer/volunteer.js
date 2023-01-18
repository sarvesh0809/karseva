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


$.ajax({
    url:  '/load_volunteer_data/0',
    success: function (data) {
        var json_data = JSON.parse(data)
        var data_length = json_data.length-1
        if(data_length>0){
        var temp_html = `<table class="table table-hover table-nowrap">
                        <thead class="thead-light">
                            <tr>
                                <th scope="col">Request No</th>
                                <th scope="col">User Name</th>
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
                    ${json_data[i].requestor? `${json_data[i].requestor['username']}` : 'N/A'} 
                </a>
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
                <a href="view_user_request_volunteer/${json_data[i].id}" class="btn btn-sm btn-neutral">View</a>
                
            </td>
        </tr>
        `
        temp_html+=temp_tr
        }
        var temp_end = `</tbody></table>`
        temp_html+=temp_end
        $('#volunteer_tasks_table').append(temp_html)
    }
    },
    error: function (xhr, errmsg, err) {
        console.log(xhr.status + ":" + xhr.responseText)
    }
})

var offset=0;
try{
var myDiv = document.getElementById("volunteer_tasks_table");
myDiv.addEventListener("scroll",function(e)
{
    e.preventDefault();
    
    if(myDiv.scrollTop+myDiv.clientHeight<=myDiv.scrollHeight){
        offset+=10

        $.ajax({
            url:  '/load_volunteer_data/'+offset,
            success: function (data) {
                var json_data = JSON.parse(data)
                var data_length = json_data.length-1
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
                            ${json_data[i].requestor? `${json_data[i].requestor['username']}` : 'N/A'} 
                        </a>
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
                        <a href="view_user_request_volunteer/${json_data[i].id}" class="btn btn-sm btn-neutral">View</a>
                        
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


$('#volunteer_view_request_submit_btn').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#view_request_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    formData.append('status', document.getElementById('status').value)
    
    try{
        console.log(document.getElementById('feedback').value)
        formData.append('volunteer_feedback',document.getElementById('feedback').value)
        formData.append('volunteer_rating',document.getElementById('rating').value)
    }
    catch(err){
        formData.append('volunteer_feedback','')
        formData.append('volunteer_rating','')
    }
    $.ajax({
        type: 'POST',
        url:  '/volunteer_view_request_submit/'+parseInt(window.location.pathname.split('/')[2]),
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
