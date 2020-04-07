

$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/stock/",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            var table = '<thead><tr><td>ID</td><td>Tracelet</td>' +
            '<td>open</td><td>close</td><td>volume</td></tr></thead><tbody>';
                // loop each record
                for (var i = 0; i < data.length; i++) {
                    table += '<tr><td>' +  data[i].id  + '</td>' +
                             '<td>' +  data[i].tracelet  + '</td>' +
                             '<td>' +  data[i].open +  '</td>' +
                              '<td>' +  data[i].close +  '</td><td>' + data[i].volume + '</td></tr>';
                                                      }
                table += '</tbody>';
               $('#example').html(table).dataTable();
       
        }, //End of AJAX Success function

        failure: function (data) {
            alert(data.responseText);
        }, //End of AJAX failure function
        error: function (data) {
            alert(data.responseText);
        } //End of AJAX error function

    });

});