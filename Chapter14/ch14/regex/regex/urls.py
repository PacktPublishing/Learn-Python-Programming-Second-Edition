"""regex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from entries.views import HomeView, EntryListView, EntryFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('entries/', EntryListView.as_view(), name='entries'),
    path('entries/insert',
        EntryFormView.as_view(),
        name='insert'),

    path('login/',
        auth_views.login,
        kwargs={'template_name': 'admin/login.html'},
        name='login'),
    path('logout/',
        auth_views.logout,
        kwargs={'next_page': reverse_lazy('home')},
        name='logout'),

    path('', HomeView.as_view(), name='home'),
]
