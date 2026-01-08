from django.contrib import admin
from studentapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    search_fields = ('cName',)
    list_filter = ('cName',)
    ordering = ('id',)

admin.site.register(Student, StudentAdmin)


