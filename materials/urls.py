from django.urls import path
from materials import views


urlpatterns = [
    path("investment/<int:pk>/", views.investment_details,
         name="investment_details"),
    path("subjects/", views.SubjectList.as_view(),
         name="subject_list"),
    path("subject/<int:pk>/", views.MaterialList.as_view(),
         name="material_list"),
    path("<int:pk>/", views.material_details,
         name="material_details"),
    path("comment/update/<int:pk>/", views.comment_update,
         name="comment_update"),
    path("comment/delete/<int:pk>/", views.comment_delete,
         name="comment_delete"),
    path("subject/update/<int:pk>/", views.SubjectUpdateForm.as_view(),
         name="subject_update"),
    path("subject/create/", views.SubjectCreateForm.as_view(),
         name="subject_create"),
    path("create/", views.material_create, name="material_create"),
]
