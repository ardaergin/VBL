function toggleVisibility(id) {
    var content = document.getElementById(id);
    var button = content.previousElementSibling;

    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        button.setAttribute('aria-expanded', 'true');
        content.style.maxHeight = content.scrollHeight + "px";
    } else {
        content.style.maxHeight = "0";
        button.setAttribute('aria-expanded', 'false');
        // Wait for the transition to finish, then hide the element to avoid extra space
        setTimeout(function() {
            content.style.display = "none";
        }, 300); // This should match the CSS transition duration
    }
}
