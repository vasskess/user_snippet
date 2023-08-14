User Snippet is a simple Django project designed to provide a reusable code snippet for extending Django's AbstractBaseUser and creating a customizable user authentication system. It showcases how to seamlessly integrate a custom user model (AppUser) with an associated user profile (UserProfile) that automatically creates a profile for each user and generates a unique slug identifier.

Key Features
Custom User Model: Utilizes a custom user model (AppUser) to enhance user authentication and management.

Automatic Profile Creation: A UserProfile model is automatically created for each user upon registration, establishing a one-to-one relationship and avoiding hardcoded references. By avoiding hardcoded references to the 'UserProfile' model, you ensure flexibility in your codebase. This means you can change the name of your 'UserProfile' model in the future without triggering database-related issues or requiring extensive code modifications. This  enhances maintainability and allows for seamless adjustments as your project evolves.

Profile Slug Generation: The UserProfile includes an automatically generated unique slug based on the user's email address.

Django Admin Panel: The Django admin panel is customized to manage and display user instances, with a focus on fields like email, staff status, and superuser status.

REST API Endpoints: Provides REST API endpoints for listing users, retrieving a single user, and deleting users.

Optional API Documentation: Utilizes drf_spectacular to generate API documentation for endpoint testing, but functionality can be accessed and tested entirely through the Django admin panel.

Getting Started

Clone the repository.<br>
Install project dependencies.<br>
Customize the user model fields and profile as needed.<br>
Run migrations: python manage.py migrate<br>

Project Structure<br>

The project is organized as follows:<br>

accounts/: Contains the custom user model, profile model, serializers, and views.<br>
helpers/: Includes utility functions used across the project.
