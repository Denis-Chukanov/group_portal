from django import template
register = template.Library()

@register.inclusion_tag('forum/post_tree.html')
def render_post_tree(posts, parent=None, form=None):
    children = [p for p in posts if p.parent == parent]
    return {'posts': children, 'all_posts': posts, 'form': form}
