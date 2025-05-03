from django.core.exceptions import PermissionDenied


class UserIsPermission():
    def dispatch(self, request, *args, **kwargs):
        self._set_conditional(request)
        if self.conditional:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UserIsAdminMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN")


class UserIsModeratorMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN" and
                            request.user.portfolio.permission !=
                            "MODER")


class UserIsStudentMixin(UserIsPermission):
    def _set_conditional(self, request):
        self.conditional = (request.user.portfolio.permission
                            != "ADMIN" and
                            request.user.portfolio.permission !=
                            "MODER" and
                            request.user.portfolio.permission !=
                            "STUDENT")
