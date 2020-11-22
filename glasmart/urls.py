"""glasmart URL Configuration """

# Django imports
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Views
from django.contrib.auth import views as auth_views
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

    # Dashboard views
    path('dashboard/home/', dashboards_views.home, name='home'),
    path('dashboard/turn_card/', dashboards_views.turn_card, name='turn_card'),
    path('dashboard/first_cards', dashboards_views.create_first_cards, name="first_cards"),

    # Reset passwords
     path(
        'reset/password_reset', 
        auth_views.PasswordResetView.as_view(
             template_name='restore/password_reset_form.html', 
             email_template_name='restore/password_reset_email.html'
        ), 
        name="password_reset"
    ),
    path(
        'reset/password_reset_done', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='restore/password_reset_done.html'
        ), 
        name="password_reset_done"
    ),
    path(
        'reset/password_reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='restore/password_reset_confirm.html'
        ), 
        name='password_reset_confirm'
    ),
    path(
        'reset/password_reset/done', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='restore/password_reset_complete.html'
        ), 
        name='password_reset_complete'
        ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
