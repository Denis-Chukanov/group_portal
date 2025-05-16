from django.contrib import admin
from materials.models import Investment, Subject, Material, Comment


# Register your models here.
admin.site.register(Subject)
admin.site.register(Material)
admin.site.register(Investment)
admin.site.register(Comment)
