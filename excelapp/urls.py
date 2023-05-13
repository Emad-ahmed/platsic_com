
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('headcompany/', HeadCompanyView.as_view(), name="headcompany"),
    path('subcompany/', SubCompanyView.as_view(), name="subcompany"),
    path('clientcompany/', ClientCompanyView.as_view(), name="clientcompany"),
    
    path('subcompanyupdate/<int:id>/<int:id2>/', SubcompanyUpdateView.as_view(), name="subcompanyupdate"),
    path('clientcompanyupdate/<int:id>/<int:id2>/', ClientcompanyUpdateView.as_view(), name="clientcompanyupdate"),
    path('edithead/<int:id>/', EditHeadCompany.as_view(), name="edithead"),

    path('createpdfsub/<int:id>/', render_pdf_view_s_anda_s_management, name="createpdfsub"),
    path('createpdfsub_one/<int:id>/', render_pdf_view_wp, name="createpdfsub_one"),
    path('createpdfsub_two/<int:id>/', render_pdf_view_bina, name="createpdfsub_two"),
    path('createpdfsub_three/<int:id>/', render_pdf_view_ds, name="createpdfsub_three"),
    path('createpdfsub_four/<int:id>/', render_pdf_view_klp, name="createpdfsub_four"),
    path('createpdfsub_five/<int:id>/', render_pdf_view_kt, name="createpdfsub_five"),
    path('createpdfsub_six/<int:id>/', render_pdf_view_Revolution, name="createpdfsub_six"),
    path('createpdfsub_seven/<int:id>/', render_pdf_view_PWR, name="createpdfsub_seven"),


    path('createpdfclient/<int:id>/', render_pdf_view_clientcompany, name="createpdfclient"),
    path('createpdfclient_one/<int:id>/', render_pdf_view_clientcompany, name="createpdfclient_one"),

    path('exportcompany/', export_data_to_excel_headcompany, name="exportcompany"),
    path('exportsubcompany/', export_data_to_excel_subcompany, name="exportsubcompany"),
    path('exportclientcompany/', export_data_to_excel_clientcompany, name="exportclientcompany"),
    path('exportsplitcompany/<int:id>/', export_data_to_excel_splitcompany, name="exportsplitcompany"),
    path('exportsubcompanyhead/<int:id>/', export_data_to_excel_subcompany_head, name="exportsubcompanyhead"),

    path('updatesub/<int:id>/', updatesubview, name="updatesub"),
    path('updateclient/<int:id>/', updateclientview, name="updateclient"),

    path('subcompanyone/<int:id>/', SubCompanyOneView.as_view(), name="subcompanyone"),
    path('clientcompanyone/<int:id>/', ClientCompanyOneView.as_view(), name="clientcompanyone"),
    
    path('subcompnaysplit/<int:id>/', SubCompanySplit.as_view(), name="subcompnaysplit"),
    path('clientcompnaysplit/<int:id>/', ClientCompanySplit.as_view(), name="clientcompnaysplit"),

    
]
