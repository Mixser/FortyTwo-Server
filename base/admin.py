from django.contrib import admin

# Register your models here.
from base.models import ApplicationUser, Score


admin.site.register(ApplicationUser)
#score to admin
admin.site.register(Score)