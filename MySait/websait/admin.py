from django.contrib import admin
from .models import Webdev, Person
from django_summernote.admin import SummernoteModelAdmin


class WebdevText(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Webdev, WebdevText)
admin.site.register(Person)
