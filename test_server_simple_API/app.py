# The user submits a form on your webpage (/handle_form) with their input, 
# such as the selected project, evaluation day, etc.

# Instead of directly handling the form data, 
# you initiate the OAuth2 authentication process with the 42 API. 
# The redirect function is used to send a redirection response to the user's browser.

# The browser is redirected to the 42 API authorization endpoint (AUTH_URL) 
# with specific parameters, including your application's client_id, redirect_uri, response_type 
# (which is set to 'code' to indicate that you're expecting an authorization code in response), 
#  and the requested scope (in this case, 'public forum').

# The user interacts with the 42 API authorization page. 
# If they approve your application's request for access, 
# the 42 API will redirect the user back to 
# your specified redirect_uri with an authorization code appended as a query parameter.

# Your Flask application handles the subsequent redirection 
# from the 42 API at the /callback route (or another specified route 
# for handling the callback).





# Remember to replace placeholder values such as USER_INFO_URL 
# and others with the actual values from the 42 API documentation. 
# Additionally, ensure that the /redirect endpoint is correctly set up 
# in your Flask application and registered as the redirect_uri 
# in your 42 API application settings.










from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import secrets

app = Flask(__name__)

# Replace these values with your 42 API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://your_redirect_uri'  # Replace with your actual redirect URI
AUTH_URL = 'https://api.intra.42.fr/oauth/authorize'
TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
USER_INFO_URL = 'https://api.intra.42.fr/v2/me'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    # Process form data
    user_id_from_app = request.form.get('user_id')
    # ... (other form data)

    # Redirect to 42 API for authentication
    return redirect(f'{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=public forum')

@app.route('/callback')
def callback():
    # Handle callback from 42 API after authentication
    code = request.args.get('code')
    if code:
        access_token = exchange_code_for_token(code)
        if access_token:
            # Store the access token for future use (e.g., in session)
            # For simplicity, we'll just print it to the console
            print(f"Access token: {access_token}")

            # Use the access token to get user information from 42 API
            headers = {'Authorization': f'Bearer {access_token}'}
            response = requests.get(USER_INFO_URL, headers=headers)

            if response.status_code == 200:
                user_data = response.json()
                # Process user data as needed
                return render_template('success.html', user_data=user_data)
            else:
                return 'Failed to get user data from 42 API'
        else:
            return 'Failed to exchange code for access token'
    else:
        return 'Authentication failed'

def exchange_code_for_token(code):
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        return access_token
    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)













# from flask import Flask, render_template, request, url_for, redirect
# import subprocess

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/handle_form', methods=['POST'])
# def handle_form():
#     #user_id_from_app = request.form.get('user_id')
#     #password_from_app = request.form.get('password')
#     project_name_from_app = request.form.get('project_name')
#     evaluation_day_from_app = request.form.get('evaluation_day')
#     print("first: ", evaluation_day_from_app)

#     start_time_from_app = request.form.get('start_time')
#     end_time_from_app = request.form.get('end_time')

#     # Process the form data as needed
#     # For example, print the data to the console
#     #print(f'User ID: {user_id_from_app}')
#     #print(f'User password: {password_from_app}')
#     print(f'Project Name: {project_name_from_app}')
#     print(f'Evaluation Day: {evaluation_day_from_app}')
#     print(f'Start Time: {start_time_from_app}')
#     print(f'End Time: {end_time_from_app}')

#     #after clicking last step of booking icon, I should check if evaluation slot is booked

#     #connected to my webpage
#     return "Form submitted successfully"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)