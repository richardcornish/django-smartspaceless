.. _install:

Install
*******

Install with the `pip <https://pip.pypa.io/en/stable/>`_ package manager.

.. code-block:: bash

   $ mkvirtualenv myvenv -p python3
   $ pip install django
   $ pip install django-smartspaceless

After `creating a project <https://docs.djangoproject.com/en/1.10/intro/tutorial01/>`_, add ``smartspaceless`` to ``INSTALLED_APPS`` in ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'smartspaceless',
   ]

Remember to update your ``requirements.txt`` file. In your project directory:

.. code-block:: bash

   $ pip freeze > requirements.txt
