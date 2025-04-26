from django.core.exceptions import PermissionDenied


class UserIsPermission():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.portfolio.permission != self.permission:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UserIsAdminMixin(UserIsPermission):
    permission = "ADMIN"


class UserIsModeratorMixin(UserIsPermission):
    permission = "MODER"


class UserIsStudentMixin(UserIsPermission):
    permission = "STUDENT"
