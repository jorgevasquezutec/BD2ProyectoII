$(function () {
    
    var csrftoken = getCookie('csrftoken');
    request_data = {
        'searchTerms': document.getElementById("query").value,
        'csrfmiddlewaretoken': csrftoken
    }

    $('#search').click(function() {
        var query = $("#query").val();
        var makequery = JSON.stringify({
              "query":query
                });
        $.ajax({
              url: '/search',
              type: 'POST',
              contentType: 'application/json',
              data : makequery,
              dataType:'json',
              success: function(data){
                    console.log(data.msg)
              },   
              error: function(data){
                // $.growl.error({ message: data.msg});
                  console.log(data);
              }
            });
      });

});




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

