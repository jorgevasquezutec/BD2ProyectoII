$(function () {
    
   
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
                results = document.getElementById("results");
                results.innerHTML = "";

                  for (tweet of data) {
                    twttr.widgets.createTweet(tweet, results);
                  }
              },   
              error: function(data){
                // $.growl.error({ message: data.msg});
                  console.log(data);
              }
            });
      });

});
