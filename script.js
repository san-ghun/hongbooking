document.addEventListener('DOMContentLoaded', function () {
    console.log('Website loaded successfully.');

    // Get the base URL dynamically
    var baseURL = 'https://HONGBAEKIM.github.io/eval_booker';

    // Log the dynamically generated URL to the console
    console.log('Website URL:', baseURL);

    // Your API endpoint on the Heroku backend
    var apiEndpoint = 'https://your-heroku-app.herokuapp.com/api';

    // Sample data to send in the POST request
    var postData = {
        user_id: 'user_id_from_app',
        password: 'password_from_app',
        project_name: 'project_name',
        evaluation_day: 'evaluation_day',
        start_time: 'start_time',
        end_time: 'end_time',
        // Add other data as needed
    };

    // Make a POST request to the Heroku backend
    fetch(apiEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData),
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
