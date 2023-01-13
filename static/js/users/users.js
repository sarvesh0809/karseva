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

function fetchVolunteer(){
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
    if(subCategoryName.includes(resp.value)){
        fetch('/category_data_api')
        .then((resp) => resp.json())
        .then(function (data) {
            const result = Object.keys(data[0]).reduce((obj, key) => {
                obj[key] = data.map(_ => _[key]);
                return obj;
            }, {});
            
        })
       
    }   
    })
}