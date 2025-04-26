from django.core.exceptions import PermissionDenied


def decorator_body(request, func, permission, *args):
    if request.user.portfolio.permission != permission:
        raise PermissionDenied
    return func(request, *args)


def is_administrator(func):
    def wrapper(request, *args):
        return decorator_body(request, func, "ADMIN", *args)

    return wrapper


def is_moderator(func):
    def wrapper(request, *args):
        decorator_body(request, func, "MODER", *args)

    return wrapper


def is_student(func):
    def wrapper(request, *args):
        decorator_body(request, func, "STUDENT", *args)

    return wrapper
