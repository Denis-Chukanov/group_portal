from django.contrib import admin
from .models import Survey, SurveyComment

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    list_filter = ('created_by',)

@admin.register(SurveyComment)
class SurveyCommentAdmin(admin.ModelAdmin):
    list_display = ('survey', 'user', 'created_at')
