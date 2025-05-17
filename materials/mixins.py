from django.core.exceptions import PermissionDenied


class UserIsSubjectOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.owner:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UserIsMaterialOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        owner = instance.subject.owner
        if self.request.user != owner:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
