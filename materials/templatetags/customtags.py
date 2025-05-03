from django import template


register = template.Library()


@register.filter(name="endswith")
def endswith(value, arg):
    value.lower().endswith(arg.lower())
