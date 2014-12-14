from django.contrib import admin

# Register your models here.
from base.models import ApplicationUser, Score


admin.site.register(ApplicationUser)
admin.site.register(Score)