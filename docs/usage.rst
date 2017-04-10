.. _usage:

Usage
*****

Load the template tag in a template. Run the tag with an opening and closing tag.

.. code-block:: django

   {% extends "base.html" %}

   {% load smartspaceless_tags %}

   {% block content %}

       {% smartspaceless %}
       <p><a href="#">Link 1</a></p>
       <p><a href="#">Link 2</a> <a href="#">Link 3</a></p>
       {% endsmartspaceless %}

   {% endblock %}

Result:

.. code-block:: html

   <p><a href="#">Link 1</a></p><p><a href="#">Link 2</a> <a href="#">Link 3</a></p>
