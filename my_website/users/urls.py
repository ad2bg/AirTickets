from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='users-register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    url(r'^profile/$', views.profile, name='users-profile'),

    url(r'^password-reset/$',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),

    url(r'^password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),

    url(r'^password-reset-complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
