from django.contrib import admin
from mainapp.models import CheckList,CheckListItem
# Register your models here.
admin.site.register(CheckList),
admin.site.register(CheckListItem)