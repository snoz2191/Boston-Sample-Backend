from django.contrib import admin

from .models import Task, Execution

# Register your models here.
admin.site.register(Task)
admin.site.register(Execution)
