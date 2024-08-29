from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin  
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('snippets/my', views.my_snippets_page, name='my_snippets'),
    path('snippets/edit/<int:id>/', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>/', views.delete_snippet, name='delete_snippet'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippets'),
    path('', views.index_page, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
