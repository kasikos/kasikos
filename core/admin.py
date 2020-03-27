from django.contrib import admin
from .models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'cellphone_no',)

    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()
    upper_case_name.short_description = 'Name'

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)