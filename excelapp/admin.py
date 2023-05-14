from django.contrib import admin
from .models import HeadCompany,SubCompany, ClientCompany, SplitCompnay
from import_export.admin import ImportExportModelAdmin

@admin.register(HeadCompany)
class HeadCompanyAdmin(ImportExportModelAdmin):
    pass

@admin.register(SubCompany)
class SubCompanyAdmin(ImportExportModelAdmin):
    pass

@admin.register(ClientCompany)
class ClientCompanyAdmin(ImportExportModelAdmin):
    pass

@admin.register(SplitCompnay)
class SplitCompnayAdmin(ImportExportModelAdmin):
    pass