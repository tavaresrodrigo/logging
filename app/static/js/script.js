$(document).ready(function() {
    $('#json-button').click(function(event) {
        event.preventDefault(); 
        $.ajax({
        url: '/json',
        type: 'GET',
        success: function(response) {
            console.log(response)
            var output = "";
            for (var i = 0; i < response.length; i++) {
                output += JSON.stringify(response[i]) + "<br>" ;
                }
            // var output = JSON.stringify(response);
            $('#terminal-body').append(output);
        },
        error: function(xhr, status, error) {
          console.log(error);
        }
      });
    });
  });
  