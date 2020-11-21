"""glasmart URL Configuration """

# Django imports
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from django.contrib.auth import views as auth_view
from login import views as login_views
from dashboard import views as dashboards_views


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

    path('reset/restore_password/', login_views.restore_password, name='restore'),
    path('reset/email_sended/', login_views.email_sended, name='email_sended'),
    path('reset/pasword_reset_done', login_views.pasword_reset, name='pasword_reset'),
    path('reset/(?P<uidb64[0-9A-Za-z_\-]+)/(?P<token>.+))')

    # Dashboard views
    path('dashboard/home/', dashboards_views.home, name='home'),
    path('dashboard/turn_card/', dashboards_views.turn_card, name='turn_card'),
    path('dashboard/first_cards', dashboards_views.create_first_cards, name="first_cards")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
