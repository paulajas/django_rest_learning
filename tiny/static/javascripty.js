function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function call_receipe(idik){

    const csrftoken = getCookie('csrftoken');
    console.log(idik);
    url_tmp = "/receipe/" + idik
    console.log((url_tmp));
    $.ajax({
        type: "GET",
        url: url_tmp,
        withCredentials: true,
        dataType: "json",
        headers: {'X-CSRFToken': csrftoken},
        })
}
