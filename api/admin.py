from django.contrib import admin
from api.models import User, Profile, Note, Lecturer, Course

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'first_name', 'middle_name', 'last_name', 'verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Note)