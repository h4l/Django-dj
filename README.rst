Django-dj
=========

Django-dj is a console command which removes the need to use Django's 
``manage.py`` script.

Old way
-------

::

  $ django-project> python manage.py runserver/syncdb/etc

::

  $ django-project/some/dir> python ../../manage.py runserver/syncdb/etc

New Way
-------

::

  $ django-project> dj runserver/syncdb/etc

::

  $ django-project/some/dir> dj runserver/syncdb/etc

Instead of carefully referencing ``manage.py`` from whichever directory you
happen to be in, ``dj`` works anywhere in or under your Django project 
directory. You can even completely remove your ``manage.py`` file if you wish.

``dj`` identifies Django projects by looking for directories which are Python
packages containing ``settings`` and ``urls`` submodules.

Installing
----------

With ``pip``, run the command::

  sudo pip install django-dj

Or with ``easy_install`` run::

  sudo easy_install django-dj

Alternatively, you can manually install by copying the ``dj`` file to somewhere
on your ``$PATH``, perhaps ``~/bin/``.

How ``dj`` finds Django projects
----------------------------

As mentioned above, ``dj`` identifys Django projects by looking for directories
which are Python packages (e.g. contain an ``__init__.py[oc]`` file) containing
the following submodules:

* ``settings``
* ``urls``

If a package directory contains both submodules then ``dj`` takes it to be a
Django project and tries to run Django's management tool on it.

Python modules/packages are identified by looking for ``.py``/``.pyc``/``.pyo``
files of the correct name, or directories of the correct name containing a
``__init__.py``/``.pyc``/``.pyo`` file. For performance and security reasons
Python's own import functionality is not used (no Python modules are executed
while searching for Django projects).

Search Strategy
+++++++++++++++

The directories ``dj`` looks in are chosen as follows. The search starts in the
working directory this script is executed from and moves upwards to the parent
directory, and then the parent's parent directory and so forth until either a
Django project is found, or the root of the filesystem is reached.

If a file named ``.djangoproject`` is encountered during the search, a complete
search of the subtree at the directory holding the ``.djangoproject`` file is 
triggered.

Invoking ``dj`` from sibling directories of a Django project
------------------------------------------------------------

The strategy of looking through the parent directories works well so long
as long as ``dj`` is executed from a child directory of the Django project. 
Consider the following project structure::

  myproject/
  |-- staticfiles/
      |-- somefile.jpg
      |-- somefile.png
      |-- somefile.gif
  |-- django-project/
      |-- urls.py
      |-- settings.py
      |-- __init__.py

If you run ``dj`` from inside ``staticfiles``, it won't find ``django-project``
because it will just check parents of ``staticfiles``, and ``django-project`` is
not a parent of ``staticfiles``. You can make ``dj`` find ``django-project`` by
creating an empty file called ``.djangoproject`` in in a common parent of 
``staticfiles`` and ``django-project``. In this case creating it in 
``myproject`` would work. This will tell dj to do a full search of all
directories under ``myproject``  rather than just its parents.