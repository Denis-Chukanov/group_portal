from django import template

register = template.Library()


@register.filter(name="endswith")
def endswith(value, arg):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(arg.lower())


@register.filter(name="is_image")
def is_image(value):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))


@register.filter(name="is_video")
def is_video(value):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(('.mp4', '.webm', '.ogg'))


@register.filter(name="is_audio")
def is_audio(value):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(('.mp3', '.wav', '.ogg', '.aac'))


@register.filter(name="is_document")
def is_document(value):
    if not isinstance(value, str):
        return False
    return value.lower().endswith(('.pdf', '.htm', '.html', '.txt'))
