from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from urus_sosh1.models import *
from import_export.admin import ImportExportModelAdmin
from urus_sosh1.models import ucheniki

@admin.register(ucheniki)
class uchenikiAdmin(ImportExportModelAdmin):
    list_display =  ('fio','data','snils','adres','fio_ot','tel_ot','mesto_rab_ot','fio_mat','tel_mat','mesto_rab_mat', 'status', 'foto', 'uch')
    pass


admin.site.register(Pedagog)
admin.site.register(Category)

admin.site.register(cat_uch)
admin.site.register(doc)
admin.site.register(adminis)

