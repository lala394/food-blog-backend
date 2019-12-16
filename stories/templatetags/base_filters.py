from django import template
from string import capwords
from stories.models import NavLinks, Category

register = template.Library()

@register.simple_tag(name='get_nav_links')
def get_nav_links():
    return NavLinks.objects.filter(active=True)

@register.filter
def custom_capitalize(value):
    return capwords(value)
    # return value.upper()

@register.filter
def custom_text_edit (value, mode):
    if mode=="upper":
        return value.upper()
    elif mode=="lower":
        return value.lower()

@register.simple_tag
def get_categories():
    return Category.objects.all()

