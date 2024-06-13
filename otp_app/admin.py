from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser , OtpToken
from django.contrib.auth.admin import UserAdmin
from .models import Category ,Product ,Order


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )


class OtpTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "otp_code")


admin.site.register(OtpToken, OtpTokenAdmin)
admin.site.register(CustomUser, CustomUserAdmin)





admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)


# admin.site.register(CustomUser)