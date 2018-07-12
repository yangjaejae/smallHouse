=====
smallHouse
=====

smallHouse is a simple Django app to conduct Web-based smallHouse. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "smallHouse" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'smallHouse',
    ]

2. Include the smallHouse URLconf in your project urls.py like this::

    path('', include('smallHouse.urls')),

3. Run `python manage.py migrate` to create the smallHouse models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a smallHouse (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/main/ to participate in the poll.