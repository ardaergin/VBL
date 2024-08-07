$(document).ready(function() {
    $(".tiptext").hover(
        function() {
            var iframe = $(this).children(".description");
            iframe.attr("src", iframe.data("src")); // Set the iframe src on hover
            iframe.show();
        },
        function() {
            $(this).children(".description").hide();
        }
    );
});
