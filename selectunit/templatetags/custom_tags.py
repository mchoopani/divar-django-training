from django import template
import markdown

register = template.Library()


@register.simple_tag
def get_gender(ch):
    if ch == 'F':
        return 'زن'
    if ch == 'M':
        return 'مرد'
    return 'هیچ کدام'


@register.simple_tag
def markdownify(text):
    return markdown.markdown(text).strip()


