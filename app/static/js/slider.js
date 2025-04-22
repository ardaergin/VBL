function updateAmount() {
    var onlineRatePerMinute = 10 / 60; // 10 € per hour converted to per minute
    var physicalRatePerMinute = 12.5 / 60; // 12.50 € per hour converted to per minute

    var minutes = document.getElementById("timeSlider").value;
    document.getElementById("timeDisplay").textContent = minutes;

    var onlineAmount = onlineRatePerMinute * minutes;
    var physicalAmount = physicalRatePerMinute * minutes;

    document.getElementById("onlineAmount").textContent = `€${onlineAmount.toFixed(2)}`;
    document.getElementById("physicalAmount").textContent = `€${physicalAmount.toFixed(2)}`;
}
