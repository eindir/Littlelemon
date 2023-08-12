Hello Peer reviewer,
Thanks for reviewing the project. Here are some notes to help you quickly do the review.

1. Virtual environment
I used pipenv (not venv). This was the recommended way to create a virtual enviroment in
prior courses and I stuck with that. You likely already have that installed but if not
the command is
pip install pipenv --user

You follow with 
pipenv shell
pipenv sync
... now you are ready to start testing.

2. Does the web application use Django to serve static HTML content?
My route for a static home page is:
        localhost:8000/restaurant

3. Does the application connect the backend to a MySQL database?
My settings.py has these DB credentials set to my instance of MySQL
        'USER': 'admindjango',
        'PASSWORD': 'employee@123!',
Please set to your MySQL server's credentials

4. Are the menu and table booking APIs implemented?
The route for menu APIs:
        http://localhost:8000/restaurant/menu
The route for booking APIs:
        http://localhost:8000/restaurant/booking/tables

5. Is the application set up with user registration and authentication?
All djoser functionality is available at:
        http://localhost:8000/auth/

6. Does the application contain unit tests?
One model and two view test cases created within the Restaurant app.

7. Can the API be tested with the Insomnia REST client?
If you saved your Insomnia collection of API calls they should work pretty much as is.

Thanks again,
-Eric