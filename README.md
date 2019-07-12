# Python-Techdegree-Project-9 Improve a Django Project
We spent a weekend doing a hackathon a year or so ago and someone built this project. It's...not the best. It runs kind of slow and has been a real pain to debug and add onto. We need you to go through the project, find where it's inefficient, and fix it. Check the templates for bad inheritance and extra database calls. Check the views for extra views or extra database calls. Check the models to make sure they're using the best fields. Check the forms for proper validation and fields. Basically just check the whole thing over. Oh, and it doesn't have any tests, so please get test coverage up to at least 75%.

To complete this project, follow the instructions below:
1. Use the provided requirements.txt to install needed packages for the project.
2. Use django-debug-toolbar to find places where database queries run too long or hit the database too many times.
3. Use django-debug-toolbar to find places where templates aren't properly using inheritance.
4. Check that models are using appropriate fields for the type of data they store. If not, correct them and create migrations to handle the data.
5. Check that forms are using the correct fields and validation. If not, fix.
6. Use coverage.py to check the code coverage amount. Write tests to increase test coverage to at least 75%.
