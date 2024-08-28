from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('snippets/edit/<int:id>/', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>/', views.delete_snippet, name='delete_snippet'),
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippets'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
