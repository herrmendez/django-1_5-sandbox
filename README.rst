=============================
 Django project sandbox (1.5)
=============================

This is just some sandbox to avoid the boilerplate needed to start each new Django project.


Installing it
=============

If you want to install from it's source:

 $ git clone https://github.com/herrmendez/django-1_5-sandbox.git

and after creating virtualenv...

 $ cd django-1_5-sandbox

 $ pip install -r config/requirements.txt

After this, you can modify the settings at your liking. All the setting files are at PROJECT_FOLDER/config/settings, and they are split into:

- defaults.py: settings common to development and production
- dev.py: development specific settings
- production.py: production specific settings
- testing.py: the settings used when you run "$ fab test_project" (testing db, etc)

Batteries included
==================

- Django extensions: https://github.com/django-extensions/django-extensions
- Django debug toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
- Django discover runner: https://github.com/jezdez/django-discover-runner
- Werkzeug: https://github.com/mitsuhiko/werkzeug
- Fabric: https://github.com/fabric/fabric
- Twitter bootstrap: https://github.com/twitter/bootstrap
- South: https://bitbucket.org/andrewgodwin/south/
- Backbone Tastypie: https://github.com/PaulUithol/backbone-tastypie
- Backbone.js: https://github.com/documentcloud/backbone/

