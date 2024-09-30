function performSearch() {
    const query = document.getElementById('search-query').value;
    console.log('Search function triggered with query: ' + query);
    fetch("{{ url_for('search.search') }}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "{{ url_for('search.results_page') }}";
        } else {
            response.json().then(data => {
                const container = document.getElementById('search-results-container');
                container.innerHTML = `<p>${data.error}</p>`;
            });
        }
    })
    .catch(error => console.error('Error:', error));
}
