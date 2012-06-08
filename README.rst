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

``dj`` identifies Django projects by looking for directories containing 
``__init__.py``, ``settings.py`` and ``urls.py``.

Installing
----------

With ``pip``, run the command::

  sudo pip install django-dj

Or with ``easy_install`` run::

  sudo easy_install django-dj

Alternatively, you can manually install by copying the ``dj`` file to somewhere
on your ``$PATH``, perhaps ``~/bin/``.
