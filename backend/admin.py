from django.contrib import admin
from models import *


# Register your models here.
class MySideBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'entry_name')


class MyTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_level', 'second_level')


class MyPapersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'authors', 'institutions', 'abstract', 'notes')


class MyNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'name', 'type', 'content', 'state', 'tag')

admin.site.register(MySideBar, MySideBarAdmin)
admin.site.register(MyTags, MyTagsAdmin)
admin.site.register(MyPapers, MyPapersAdmin)
admin.site.register(MyNotes, MyNotesAdmin)