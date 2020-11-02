"""glasmart URL Configuration """

# Django imports
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from django.contrib.auth import views as auth_view
from login import views as login_views


urlpatterns = [
    # Django views
    path('admin/', admin.site.urls),

    # Login Views
    path('', login_views.index, name='index'),
    path('login/', login_views.login_view, name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('signin/', login_views.signin, name='signin'),
    path('about/', login_views.about_view, name='about'),
    path('shop/', login_views.shop_view, name='shop'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
