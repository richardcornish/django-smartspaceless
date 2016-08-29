from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class SmartSpacelessTestCase(TestCase):
    def test_a(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<a href="#">1</a>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<a href="#">1</a>')

    def test_aa(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<a href="#">1</a><a href="#">2</a>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<a href="#">1</a><a href="#">2</a>')

    def test_a_a(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<a href="#">1</a> <a href="#">2</a>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<a href="#">1</a> <a href="#">2</a>')

    def test_a_a_a(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<a href="#">1</a> <a href="#">2</a> <a href="#">3</a>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<a href="#">1</a> <a href="#">2</a> <a href="#">3</a>')

    def test_a_strong(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<a href="#">1</a> <strong>2</strong>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<a href="#">1</a> <strong>2</strong>')

    def test_p_a_a_p(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<p><a href="#">1</a> <a href="#">2</a></p> <p>3</p>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<p><a href="#">1</a> <a href="#">2</a></p><p>3</p>')

    def test_p_a_a_p_a(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<p><a href="#">1</a> <a href="#">2</a></p> <p> <a href="#"> 3 4 </a> </p>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<p><a href="#">1</a> <a href="#">2</a></p><p><a href="#">3 4</a></p>')

    def test_p_a_p_a_a(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<p><a href="#">Link 1</a></p>\n<p><a href="#">Link 2</a> <a href="#">Link 3</a></p>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<p><a href="#">Link 1</a></p><p><a href="#">Link 2</a> <a href="#">Link 3</a></p>')

    def test_html_basic(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<html>\n    <head></head>\n    <body>\n<p> <a href="#"> 1 </a> </p>\n</body>\n</html>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<html><head></head><body><p><a href="#">1</a></p></body></html>')

    def test_html_doctype(self):
        out = Template(
            "{% load smartspaceless_tags %}"
            "{% smartspaceless %}"
            '<!DOCTYPE html>\n\n<html lang="en">\n    <head>\n        <title> 0 </title>\n    </head>\n    <body>\n        <p> <a href="#"> 1   </a>     </p>\n    </body>\n</html>'
            "{% endsmartspaceless %}"
        ).render(Context())
        self.assertEqual(out, '<!DOCTYPE html><html lang="en"><head><title>0</title></head><body><p><a href="#">1</a></p></body></html>')
