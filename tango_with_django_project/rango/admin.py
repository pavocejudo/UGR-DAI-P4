from django.contrib import admin
from rango.models import Bar,Tapas, UserProfile
# Register your models here.

class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

admin.site.register(Bar, BarAdmin)
admin.site.register(Tapas)
admin.site.register(UserProfile)
