Django Smart Spaceless
**********************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-smartspaceless.svg
.. _PyPI version: https://pypi.python.org/pypi/django-smartspaceless

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-smartspaceless.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-smartspaceless

**Django Smart Spaceless** is a `Django template tag <https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/>`_ application for minifying block-level HTML elements only.

It's just like |spaceless|_, but preserves white space between inline HTML elements. Useful for HTML where spaces directly between ``<a>``, ``<strong>``, and other inline elements is likely desired to be preserved. Packages the `django-htmlmin <https://github.com/cobrateam/django-htmlmin>`_ project to be used as a template tag.

.. |spaceless| replace:: ``spaceless``
.. _spaceless: https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#spaceless

* `Package distribution <https://pypi.python.org/pypi/django-smartspaceless>`_
* `Code repository <https://github.com/richardcornish/django-smartspaceless>`_
* `Documentation <https://django-smartspaceless.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-smartspaceless>`_

Install
=======

.. code-block:: bash

   $ pip install django-smartspaceless

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'smartspaceless',
   ]

Usage
=====

.. code-block:: html

   {% load smartspaceless_tags %}

   {% smartspaceless %}
   <p><a href="#">Link 1</a></p>
   <p><a href="#">Link 2</a> <a href="#">Link 3</a></p>
   {% endsmartspaceless %}

Result:

.. code-block:: html

   <p><a href="#">Link 1</a></p><p><a href="#">Link 2</a> <a href="#">Link 3</a></p>

Note that the space between ``<a href="#">Link 2</a>`` and ``<a href="#">Link 2</a>`` is preserved. Removing that space would be bad.