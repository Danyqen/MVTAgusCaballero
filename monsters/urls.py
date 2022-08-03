from django.urls import path
from . import views


urlpatterns = [
    path('monsters/', views.ListMonster.as_view(), name='list_monster'),
    path('create-monster/', views.CreateMonster.as_view(), name='create_monster'),
    path('edit-monster/<int:pk>', views.EditMonster.as_view(), name='edit_monster'),
    path('delete-monster/<int:pk>', views.DeleteMonster.as_view(), name='delete_monster'),
    path('show-monster/<int:pk>', views.ShowMonster.as_view(), name='show_monster'),
]