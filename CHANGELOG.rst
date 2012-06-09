``dj`` Changelog
================

0.2.0 - 2012-06-09
------------------

Added support for finding Django projects from sibling directories. If dj finds
a .djangoproject file while searching parent directories it performs a full
search of the subtree.  

0.1.0 - 2012-06-08
------------------

No longer uses manage.py, dj finds Django projects, sets up the PYTHONPATH and
DJANGO_SETTINGS_MODULE envar and runs the Django manage tool directly.

0.0.0 - 2012-06-06
------------------

Initial (unreleased) version, just a way to run manage.py without explicitly
referencing it.
