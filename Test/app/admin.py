from django.contrib import admin

from app.models import Tasks


# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display =('user','title','description','completed')
admin.site.register(Tasks,AdminTask)