from django.core.exceptions import PermissionDenied


def conditional(request, permission):
    return request.user.portfolio.permission != permission


def decorator_body(request, func, conditional, *args, **kwargs):
    if conditional:
        raise PermissionDenied
    return func(request, *args, **kwargs)


def is_administrator(func):
    def wrapper(request, *args, **kwargs):
        admin_conditional = conditional(request, "ADMIN")
        return decorator_body(request, func, admin_conditional,
                              *args, **kwargs)

    return wrapper


def is_moderator(func):
    def wrapper(request, *args):
        moder_conditional = (conditional(request, "MODER")
                             and conditional(request, "ADMIN"))
        return decorator_body(request, func, moder_conditional, *args)

    return wrapper


def is_student(func):
    def wrapper(request, *args):
        student_conditional = (conditional(request, "STUDENT")
                               and conditional(request, "MODER")
                               and conditional(request, "ADMIN"))
        decorator_body(request, func, student_conditional, *args)

    return wrapper
