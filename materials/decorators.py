from django.core.exceptions import PermissionDenied
from materials import models


# Перевірка на автора коментаря
def is_comment_owner(func):
    def wrapper(request, *args, **kwargs):
        pk = kwargs["pk"]
        comment = models.Comment.objects.get(pk=pk)
        if request.user != comment.author:
            raise PermissionDenied
        return func(request, *args, **kwargs)

    return wrapper
