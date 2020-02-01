const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


$( function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
} );



$(document).ready(function() {
    $("#sortable").sortable({
        connectWith: ".connectedSortable",

        update: function(event, ui) {
        var serial = $('#sortable').sortable('serialize');
        $.ajax({
            url: "{% url 'index' %}",
            type: "post",
            data: { 'content': serial, 'csrfmiddlewaretoken' : '{{ csrf_token }}' } 
        });
        },

    }).disableSelection();

    });