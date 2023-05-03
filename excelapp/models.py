from django.db import models


class HeadCompany(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=40)
    line1 = models.CharField(max_length=150, null=True, blank=True, default="main")
    line2 = models.CharField(max_length=150, null=True, blank=True, default="main")
    line3 = models.CharField(max_length=150, null=True, blank=True, default="main")
    line4 = models.CharField(max_length=150, null=True, blank=True, default="main")
    description = models.CharField(max_length=200, null=True, blank=True, default="main")
    unit_price = models.IntegerField(null=True, blank=True, default=1)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.name
    
class SubCompany(models.Model):
    head_company = models.ForeignKey(HeadCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    line3 = models.CharField(max_length=150)
    line4 = models.CharField(max_length=150)
    weight = models.IntegerField(null=True, blank=True)
    Invoicenumber = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    invoicedate = models.DateField(null=True, blank=True)
    rangemin = models.FloatField(null=True, blank=True)
    rangemax = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

class ClientCompany(models.Model):
    head_company = models.ForeignKey(HeadCompany, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    line3 = models.CharField(max_length=150)
    line4 = models.CharField(max_length=150)
    weight = models.IntegerField(null=True, blank=True)
    Invoicenumber = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    invoicedate = models.DateField(null=True, blank=True)
    rangemin = models.FloatField(null=True, blank=True)
    rangemax = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class SplitCompnay(models.Model):
    sub_company = models.ForeignKey(SubCompany, on_delete=models.CASCADE)
    date_time = models.DateField(null=True, blank=True)
    drop_time = models.TimeField(null=True, blank=True)
    vehicle = models.CharField(max_length=100)
    drop = models.IntegerField()
    weight = models.FloatField()
    status = models.BooleanField(max_length=100, default=False)