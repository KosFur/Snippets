from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.profile_page, name='profile'),
    path('', views.index_page, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('snippets/my', views.my_snippets_page, name='my_snippets'),
    path('snippets/edit/<int:id>/', views.edit_snippet, name='edit_snippet'),
    path('snippets/delete/<int:id>/', views.delete_snippet, name='delete_snippet'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='list_snippets'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
