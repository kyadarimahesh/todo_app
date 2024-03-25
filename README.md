Django Todo Application

The Django Todo Application is a web-based task management application that allows authenticated users to create, view, update, and delete their personal todo items.

Features

User Authentication
Users can sign up for a new account by providing a username and password.
Existing users can log in to their accounts using their credentials.
Logged-in users can log out of the application.
Todo Management
Authenticated users can create new todo items by providing a title, status (completed or pending), and priority (low, medium, or high).
Users can view a list of their todo items, which are displayed with the following information:
Title
Status (completed or pending)
Priority (low, medium, or high)
Checkbox to mark the todo as completed or pending
Action links to delete the todo or change its status
Todo items are ordered by priority in the list.
Todo Filtering
Users can filter the todo list based on priority using a dropdown menu.
The available filter options are:
All (displays all todo items)
Low (displays only low-priority todo items)
Medium (displays only medium-priority todo items)
High (displays only high-priority todo items)
Todo Actions
Users can delete a todo item from their list.
Users can mark a todo item as completed or pending by clicking the corresponding action link.
Technologies Used

Python
Django (Web Framework)
HTML
CSS
Bootstrap (CSS Framework)
JavaScript
Installation and Setup

Clone the repository or download the source code.
Install the required Python packages by running pip install -r requirements.txt.
Configure the Django project settings as per your environment.
Run the Django development server using python manage.py runserver.
Access the application in your web browser at the provided URL (e.g., http://localhost:8000).
Usage

Navigate to the application URL.
If you are a new user, click on the "Sign Up" link and create a new account.
If you already have an account, click on the "Login" link and enter your credentials.
After logging in, you will be redirected to the home page, where you can:
Add a new todo item by filling out the form and clicking "Add Todo".
View your existing todo items in the list.
Filter the todo list by priority using the dropdown menu.
Mark a todo item as completed or pending by clicking the corresponding action link.
Delete a todo item by clicking the delete action link.
When you are done, click the "Logout" link to log out of the application.
Please note that this document provides a general overview of the application's functionality. For more detailed information, refer to the codebase and any additional documentation provided.
