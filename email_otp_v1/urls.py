
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth.views import  PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

from api.views import send_dictionary

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("otp_app.urls")),
    path("api/", include("api.urls")),

    

    path('reset_password/',PasswordResetView.as_view(template_name='password_reset.html') , name="reset_password"),
    path('reset_password_sent/',PasswordResetDoneView.as_view(template_name='password_reset_done.html') , name="password_reset_done"),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html') , name="password_reset_confirm"),
    path('reset_password_success/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html') , name="password_reset_complete")

] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
