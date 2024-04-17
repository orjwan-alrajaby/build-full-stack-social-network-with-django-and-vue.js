***Important Note:** This project was built after I first learned Vue.js &
Django, and while the project isn't complete features-wise and isn’t polished,
it has served its primary purpose for me: as a means of further learning,
practicing, and evolving as a developer.*

-------------------------------

# Table Of Contents:

1. [Summary & Project Description](#summary--project-description)
2. [Technical Specifications & Features](#technical-specifications--features)
   - 2.1. [Technologies](#technologies)
   - 2.2. [App Features](#app-features)
      - 2.2.1. [Authentication](#authentication)
      - 2.2.2. [Users](#users)
      - 2.2.3. [Posts](#posts)
      - 2.2.4. [Likes](#likes)
      - 2.2.5. [Comments](#comments)
      - 2.2.6. [Friendships](#friendships)
      - 2.2.7. [Messaging](#messaging)
3. [How To Run The Project Locally](#how-to-run-the-project-locally)

## Summary & Project Description:

**Chatter:** 

Developed with Vue.js, Pinia.vue and Vue composables for the frontend, and
Django.py with Django Rest Framework for the backend, and leveraged Django's
Sqlite for efficient data storage and retrieval.

Features include: authentication, user profiles, posts, likes, comments,
friendships, and messaging.

### Technical Specifications & Features:

#### Technologies:
  - Vue.js
  - Pinia.vue
  - Vue.js composables
  - Django
  - Django rest_framework
  - Django’s Sqlite

#### App Features:

  - ##### Authentication:
    - Sign up for a new user.
    - Login with an existing user.

  - ##### Users:
    - View the user's own profile and posts.
    - Search for other users.
    - View another user’s profile and posts.
    - Show if logged-in user is friends with another user.

  - ##### Posts:
    - Create a post.
    - Delete a post.
    - View posts of friends.
    - View a single post’s details.
    - Search for posts of my friends and other users.

  - ##### Likes:
    - Like a post.
    - Unlike a post.
    - Show if the user liked a post or not.
    - Show if the user liked a comment or not.

  - ##### Comments:
    - Comment on a post.
    - Like a comment on a post.
    - View/hide comments on a post.

  - ##### Friendships:
    - Send a friendship request to a user.
    - Accept or reject a received friendship request.
    - Cancel sent request.
    - Show the user's own friends.
    - Show if a friendship request has already been sent to a user.

  - ##### Messaging:
    - Send a message to another user.
    - Retrieve all logged-in user’s conversations.
    - Retrieve logged-in user’s message history with another user.

## How To Run The Project Locally:

### Perquisites: 

To run a Python Django project with a Vue.js frontend locally, you'll need to
ensure that you have the necessary tools and packages installed. Here's a list
of what you will need:

1. **Python3**: You can download and install Python version 3 from the official
   Python website.

2. **pip**: Pip is the package installer for Python. It usually comes bundled
   with Python, but you might need to upgrade it to the latest version. You can
   do this by running `pip install --upgrade pip`.

3. **Node.js and npm**: You can download and install Node.js from the official
   website, and npm comes bundled in with the installation.

8. **Vue.js dependencies**: Navigate to your Vue.js frontend directory and run
   `npm install` to install all the dependencies specified in your
   `package.json` file.

Once you have all the necessary tools and packages installed, you'll need to
follow these steps to run the project locally:

1. **Backend Setup**:
   - Navigate to the Django project directory.
   - If you're using a virtual environment, activate it.
   - Run `python manage.py migrate` to apply migrations.
   - Run `python manage.py runserver` to start the Django development server.

2. **Frontend Setup**:
   - Navigate to the Vue.js project directory.
   - Run `npm run serve` to start the Vue development server.

3. **Accessing the Application**: Once both servers are running, you can access
   the application by visiting `http://localhost:8000` for the Django backend
   and `http://localhost:8080` (or another port depending on your Vue.js
   configuration) for the Vue.js frontend in your web browser.


### Step one: clone the repository.

Clone this project by executing the following command:

```bash
git clone https://github.com/orjwan-alrajaby/build-full-stack-social-network-with-django-and-vue.js.git
```

### Step two: install dependencies for the backend.

Now that you're in the root directory, enter the `chatter_backend` folder by
executing the following command:

```bash
cd chatter_backend
```

Once you're inside, install the `chatter_backend`'s dependencies by executing
the following command:

```bash
pip install -r requirements.txt
```

This command will install all dependencies listed in the
`chatter_backend/requirements.txt` file.

### Step three: apply migrations, then run the server. 

Since you're already inside `chatter_backend`, run the following commands:
- Run `python manage.py migrate` to apply migrations, and create the database.
- Run `python manage.py runserver` to start the Django development server.

Now if you see the following output, it means the server has ran successfully!

```
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  April 17, 2024 - 14:29:56
  Django version 5.0.1, using settings 'chatter_backend.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
```

### Step Four: install dependencies for the frontend.

Now that our backend is running successfully, we can move on to the frontend. So
navigate into the root directory (if you're still inside `chatter_backend`) by
executing the following command:

```bash
cd ..
```

This command will make you exit the current directory, and go back one step,
into the root directory. 

Next, navigate into the `chatter_frontend` directory by executing the following
command: 

```bash
cd chatter_frontend
```

Once you're inside `chatter_frontend`, install dependencies by executing `yarn
install` if you're using yarn, or `npm install` if you're using npm.

### Step Four: Running the Vue.js app

Now that you've installed the dependencies needed to run the app, just go ahead
and run `yarn run serve` or `npm run serve`.
