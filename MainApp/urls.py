from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippets'),
    path('snippets/my', views.my_snippets_page, name='my_snippets'),
    path('snippets/edit/<int:id>/', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>/', views.delete_snippet, name='delete_snippet'),
    path('signup/', views.signup, name='signup'),
]
