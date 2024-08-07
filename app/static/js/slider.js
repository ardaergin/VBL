function updateAmount() {
    var onlineRatePerMinute = 7.5 / 60; // 7 € per hour converted to per minute
    var physicalRatePerMinute = 10 / 60; // 10 € per hour converted to per minute

    var minutes = document.getElementById("timeSlider").value;
    document.getElementById("timeDisplay").textContent = minutes;

    var onlineAmount = onlineRatePerMinute * minutes;
    var physicalAmount = physicalRatePerMinute * minutes;

    document.getElementById("onlineAmount").textContent = `€${onlineAmount.toFixed(2)}`;
    document.getElementById("physicalAmount").textContent = `€${physicalAmount.toFixed(2)}`;
}
