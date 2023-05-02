from import_export import resources
from .models import HeadCompany, SubCompany, ClientCompany, SplitCompnay

class HeadCompanyModelResource(resources.ModelResource):
    class Meta:
        model = HeadCompany




class SubCompanyModelResource(resources.ModelResource):
    class Meta:
        model = SubCompany


class ClientCompanyModelResource(resources.ModelResource):
    class Meta:
        model = ClientCompany


class SplitCompanyModelResource(resources.ModelResource):
    class Meta:
        model = SplitCompnay