$(document).ready(function(){
    $('[data-toggle="popover"]').popover({
        placement: 'right',
        trigger: 'hover',
        html: true,
        content: function () {
            // Fetch content dynamically if needed
            return '<img src="path-to-image-preview" />';
        }
    });
});

