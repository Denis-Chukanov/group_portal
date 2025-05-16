from django.core.exceptions import PermissionDenied


# Не для використання
class UserIsPermission():
    def dispatch(self, request, *args, **kwargs):
        self._set_conditional(request)
        if self.conditional:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# Перевірка на адміністратора
class UserIsAdminMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN")


# Перевірка на модератора
class UserIsModeratorMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN" and
                            request.user.portfolio.permission !=
                            "MODER")


# Перевірка на учня
class UserIsStudentMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN" and
                            request.user.portfolio.permission !=
                            "MODER" and
                            request.user.portfolio.permission !=
                            "STUDENT")
