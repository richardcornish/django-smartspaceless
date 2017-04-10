.. _index:
.. module:: smartspaceless

Django Smart Spaceless
**********************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-smartspaceless.svg
.. _PyPI version: https://pypi.python.org/pypi/django-smartspaceless

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-smartspaceless.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-smartspaceless

**Django Smart Spaceless** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/>`_ application for minifying block-level HTML elements only.

It's just like |spaceless|_, but preserves white space between inline HTML elements. Useful for HTML where spaces directly between ``<a>``, ``<strong>``, and other inline elements is likely desired to be preserved. Packages the `django-htmlmin <https://github.com/cobrateam/django-htmlmin>`_ project to be used as a template tag.

.. |spaceless| replace:: ``spaceless``
.. _spaceless: https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#spaceless

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

.. code-block:: django

   {% load smartspaceless_tags %}

   {% smartspaceless %}
   <p><a href="#">Link 1</a></p>
   <p><a href="#">Link 2</a> <a href="#">Link 3</a></p>
   {% endsmartspaceless %}

Result:

.. code-block:: html

   <p><a href="#">Link 1</a></p><p><a href="#">Link 2</a> <a href="#">Link 3</a></p>

The space between ``<a href="#">Link 2</a>`` and ``<a href="#">Link 3</a>`` is preserved. Removing that space would be bad.

Note
====

Please note that `django-htmlmin <https://github.com/cobrateam/django-htmlmin>`_ by default uses the `html5lib <https://github.com/html5lib/html5lib-python>`_ parser, which prepends possibly missing ``<html><head></head><body>`` and appends possibly missing ``</body></html>`` tags in an effort to create valid HTML. The template tag changes this default behavior to use `html.parser <https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser>`_, the HTML parser in Python's standard library, which does not alter HTML fragments.

Contents
========

.. toctree::
   :maxdepth: 2

   install
   usage
   documentation
   tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
