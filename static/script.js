document.addEventListener('DOMContentLoaded', function () {
    console.log('Website loaded successfully.');

    // Your Flask backend URL
    var flaskEndpoint = 'http://127.0.0.1:5000/';

    document.getElementById('bookingForm').addEventListener('submit', function (event) {
        event.preventDefault();

        // Collect form data
        var formData = {
            user_id: document.getElementsByName('user_id')[0].value,
            password: document.getElementsByName('password')[0].value,
            project_name: document.getElementsByName('project_name')[0].value,
            evaluation_day: document.getElementsByName('evaluation_day')[0].value,
            start_time: document.getElementsByName('start_time')[0].value,
            end_time: document.getElementsByName('end_time')[0].value,
            // Add other form data as needed
        };

        // Make a POST request to the Flask backend
        fetch(flaskEndpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log('Response from server:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});