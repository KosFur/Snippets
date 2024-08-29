import pygments
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='syntax_highlight')
def syntax_highlight(code, language):
    try:
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter()
        result = highlight(code, lexer, formatter)
        return mark_safe(result)
    except Exception as e:
        return code

