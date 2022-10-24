from django.contrib import admin
from .models import Manuais
from django_summernote.admin import SummernoteModelAdmin


class ManuaisAdmin(SummernoteModelAdmin):
    list_display = ['titulo', 'conteudo']
    list_display_links = ['titulo', 'conteudo']
    search_fields = ['titulo', 'conteudo']
    summernote_fields = ('conteudo',)

admin.site.register(Manuais, ManuaisAdmin)    