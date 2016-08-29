from __future__ import unicode_literals

from django import template

from htmlmin.minify import html_minify

register = template.Library()


class SmartSpacelessNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return html_minify(output, parser='html.parser')


@register.tag
def smartspaceless(parser, token):
    """
    Minifies HTML between ``{% smartspaceless %}`` and
    ``{% endsmartspaceless %}``.
    """
    nodelist = parser.parse(('endsmartspaceless',))
    parser.delete_first_token()
    return SmartSpacelessNode(nodelist)
