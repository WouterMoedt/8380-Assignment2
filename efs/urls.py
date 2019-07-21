from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Admin
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password Reset
    path('password_reset/',	auth_views.PasswordResetView.as_view(),	name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),	name='password_reset_done'),
    path('reset/<uidb64>/<token>/',	auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',	auth_views.PasswordResetCompleteView.as_view(),	name='password_reset_complete'),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]