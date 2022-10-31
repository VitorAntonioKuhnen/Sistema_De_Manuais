from django.contrib import admin
from .models import Manuais
from django_summernote.admin import SummernoteModelAdmin


class ManuaisAdmin(SummernoteModelAdmin):
    list_display = ['titulo']
    list_display_links = ['titulo']
    search_fields = ['titulo', 'conteudo', 'tag']
    summernote_fields = ('conteudo')

admin.site.register(Manuais, ManuaisAdmin)    