"""myblog_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from myblog import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'register/$', user_views.register, name='register'),
    url(r'user_profile/$', user_views.user_profile, name='user_profile'),
    url(r'blogger_profile/(?P<pk>\d+)/$', user_views.blogger_profile, name='blogger_profile'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # url(r'^profile/$', views.profile, name='profile'),
    url(r'', include('myblog.urls')),
    #url('^accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
