from django.urls import path
from .views import *

urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('headcompany/', HeadCompanyView.as_view(), name="headcompany"),
    
    path('subcompanyupdate/<int:id>/<int:id2>/', SubcompanyUpdateView.as_view(), name="subcompanyupdate"),

    path('previoussubcom/<int:id>/', PreviousSubCom.as_view(), name="previoussubcom"),
    path('previousdelete/<int:id>/', PreviousSubComDelete.as_view(), name="previousdelete"),

    path('previoussubclient/<int:id>/', PreviousSubClient.as_view(), name="previoussubclient"),
    path('previousdelete_client/<int:id>/', PreviousSubClientDelete.as_view(), name="previousdelete_client"),


    path('subcompanydelete/<int:id>/<int:id2>/', SubcompanyDeleteView.as_view(), name="subcompanydelete"),
    path('clientcompanyupdate/<int:id>/<int:id2>/', ClientcompanyUpdateView.as_view(), name="clientcompanyupdate"),
    path('clientcompanydelete/<int:id>/<int:id2>/', ClientcompanyDeleteView.as_view(), name="clientcompanydelete"),

    path('edithead/<int:id>/', EditHeadCompany.as_view(), name="edithead"),
    path('deletehead/<int:id>/', DeleteHeadCompany.as_view(), name="deletehead"),

    path('createpdfsub/<int:id>/', render_pdf_view_s_anda_s_management, name="createpdfsub"),
    path('createpdfsub_one/<int:id>/', render_pdf_view_wp, name="createpdfsub_one"),
    path('createpdfsub_two/<int:id>/', render_pdf_view_bina, name="createpdfsub_two"),
    path('createpdfsub_three/<int:id>/', render_pdf_view_ds, name="createpdfsub_three"),
    path('createpdfsub_four/<int:id>/', render_pdf_view_klp, name="createpdfsub_four"),
    path('createpdfsub_five/<int:id>/', render_pdf_view_kt, name="createpdfsub_five"),
    path('createpdfsub_six/<int:id>/', render_pdf_view_Revolution, name="createpdfsub_six"),
    path('createpdfsub_seven/<int:id>/', render_pdf_view_PWR, name="createpdfsub_seven"),
    path('createpdfsub_eight/<int:id>/', render_pdf_view_B9, name="createpdfsub_eight"),

    path('createpdfclient/<int:id>/', render_pdf_view_clientcompany, name="createpdfclient"),

    path('exportcompany/', export_data_to_excel_headcompany, name="exportcompany"),
    path('exportsubcompany/', export_data_to_excel_subcompany, name="exportsubcompany"),
    path('exportclientcompany/', export_data_to_excel_clientcompany, name="exportclientcompany"),
    path('exportsplitcompany/<int:id>/', export_data_to_excel_splitcompany, name="exportsplitcompany"),
    path('exportsubcompanyhead/<int:id>/', export_data_to_excel_subcompany_head, name="exportsubcompanyhead"),
    path('updatesub/<int:id>/', updatesubview, name="updatesub"),
    path('updateclient/<int:id>/', updateclientview, name="updateclient"),

    path('subcompanyone/<int:id>/', SubCompanyOneView.as_view(), name="subcompanyone"),
    path('clientcompanyone/<int:id>/', ClientCompanyOneView.as_view(), name="clientcompanyone"),

    path('updateinvoicce_date', InvoiceDateUpdateView.as_view(), name="updateinvoicce_date"),
    path('updateinvoicce_number', InvoiceNumberUpdateView.as_view(), name="updateinvoicce_number"),

    path('subcompnaysplit/<int:id>/', SubCompanySplit.as_view(), name="subcompnaysplit"),
    path('clientcompnaysplit/<int:id>/', ClientCompanySplit.as_view(), name="clientcompnaysplit"),

    path('updatemyclientweight/', UpdateClinetViewWeight.as_view(), name="updatemyclientweight"),
    path('updatemyclientinvoice/', UpdateClinetViewInvoice.as_view(), name="updatemyclientinvoice"),
    path('updatemyclientinvoicedate/', UpdateClinetViewDate.as_view(), name="updatemyclientinvoicedate"),

    path('import_subcompany/', import_excel, name='import-excel-subcompany'),

]
