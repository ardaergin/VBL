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


function updateAmount() {
    var ratePerMinute = 0.17; // Change the rate here
    var minutes = document.getElementById("timeSlider").value;
    document.getElementById("timeDisplay").textContent = minutes;
    var totalAmount = ratePerMinute * minutes;
    document.getElementById("totalAmount").textContent = `€${totalAmount.toFixed(2)}`;
}