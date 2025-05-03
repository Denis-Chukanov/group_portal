from django.core.exceptions import PermissionDenied


# Не для використання
def conditional(request, permission):
    return request.user.portfolio.permission != permission


# Не для використання
def decorator_body(request, func, conditional, *args, **kwargs):
    if conditional:
        raise PermissionDenied
    return func(request, *args, **kwargs)


# Перевірка на адміністратора
def is_administrator(func):
    def wrapper(request, *args, **kwargs):
        admin_conditional = conditional(request, "ADMIN")
        return decorator_body(request, func, admin_conditional,
                              *args, **kwargs)

    return wrapper


# Перевірка на можератора
def is_moderator(func):
    def wrapper(request, *args):
        moder_conditional = (conditional(request, "MODER")
                             and conditional(request, "ADMIN"))
        return decorator_body(request, func, moder_conditional, *args)

    return wrapper


# Перевірка на учня
def is_student(func):
    def wrapper(request, *args):
        student_conditional = (conditional(request, "STUDENT")
                               and conditional(request, "MODER")
                               and conditional(request, "ADMIN"))
        decorator_body(request, func, student_conditional, *args)

    return wrapper
