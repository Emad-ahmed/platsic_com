from django.shortcuts import render, redirect
from django.views import View
from excelapp.models import HeadCompany, SubCompany, ClientCompany, SplitCompnay, PreviousDataSubCompany, PreviousDataClientCompany
import zipfile
from django.http import HttpResponse
from .resources import HeadCompanyModelResource, SubCompanyModelResource, ClientCompanyModelResource, SplitCompanyModelResource
from .forms import HeadForm, SubcompanyForm, ClientCompanyForm, SubcompanyUpdateForm, ClientcompanyUpdateForm
from django.shortcuts import  redirect
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.utils.decorators import method_decorator
import random
from datetime import date
from django.utils import timezone
from math import floor
from datetime import datetime, timedelta
import xlwt
from django.conf import settings
from django.contrib import messages
import pandas as pd
import zipfile


def add_pdf_to_zip(pdf_path, zip_file, zip_filename):
    zip_file.write(pdf_path, zip_filename)

class HomeView(View):
    def get(self, request):
        headcom = HeadCompany.objects.all()
        return render(request, "index.html", {'head' : headcom})

class HeadCompanyView(View):
    def get(self, request):
        headform  = HeadForm()
        HeadCompanyview = HeadCompany.objects.filter()
        return render(request, "company.html", {'head' : HeadCompanyview, 'form' : headform})

    def post(self, request):
        form = HeadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('headcompany')
        else:
            return redirect('headcompany')


class DeleteHeadCompany(View):
    def get(self, request, id):
        pi = HeadCompany.objects.get(id=id)
        pi.delete()
        messages.error(request, "Deleted Successfully")
        return redirect('/headcompany')

def export_data_to_excel_headcompany(request):
    your_model_resource = HeadCompanyModelResource()
    dataset = your_model_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="headcompany.xls"'
    return response


class EditHeadCompany(View):
    def get(self, request, id):
        pi = HeadCompany.objects.get(id=id)
        form = HeadForm(instance=pi)
        return render(request, 'update_headcompany.html', {'form': form})
    
    def post(self, request, id):
        pi = HeadCompany.objects.get(id=id)
        form = HeadForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect(f'/headcompany')
            

def export_data_to_excel_subcompany(request):
    your_model_resource = SubCompanyModelResource()
    dataset = your_model_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subcompany.xls"'
    return response


def render_pdf_view_s_anda_s_management(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'S&S_managemnet.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def render_pdf_view_wp(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'wp.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_bina(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'bina.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_ds(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'ds.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
   
    return response


def render_pdf_view_klp(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'klp.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_kt(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'kt.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_Revolution(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'Revolution.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view_PWR(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'pwr.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view_B9(request, id):
    subcompany = SubCompany.objects.get(id=id)
    name = subcompany.name
    template_path = 'b9.html'
    context = {'subcompany': subcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    # zip_filename = f'{name}.zip'
    # with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    #     zip_file.writestr(f'{name}.pdf', response.content)

    # with open(zip_filename, 'rb') as zip_file:
    #     response = HttpResponse(zip_file.read(), content_type='application/zip')
    #     response['Content-Disposition'] = f'attachment; filename="{name}.zip"'
    return response

def export_data_to_excel_subcompany(request):
    instances = SubCompany.objects.filter()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subcompany.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')
    row_num = 0
    columns = ['name', 'line1', 'line2', 'line3', 'line4', 'weight', 'Invoicenumber', 'date', 'invoicedate']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)
 
    for instance in instances:
        if instance.invoicedate:
            invoice = instance.invoicedate.strftime('%d-%m-%Y')
        date = instance.date.strftime('%d-%m-%Y')
        row_num += 1
        row = [instance.name,  instance.line1, instance.line2, instance.line3, instance.line4, instance.weight, instance.Invoicenumber, date, invoice]
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)
    wb.save(response)
    return response


def export_data_to_excel_subcompany_head(request,id):
    headcompany = HeadCompany.objects.get(id=id)
    instances = SubCompany.objects.filter(head_company = headcompany)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subcompany.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')
    row_num = 0
    columns = ['name', 'line1', 'line2', 'line3', 'line4', 'weight', 'Invoicenumber', 'date', 'invoicedate']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)
    for instance in instances:
        if instance.invoicedate:
            invoice = instance.invoicedate.strftime('%d-%m-%Y')
        date = instance.date.strftime('%d-%m-%Y')
        row_num += 1
        row = [instance.name,  instance.line1, instance.line2, instance.line3, instance.line4, instance.weight, instance.Invoicenumber, date, invoice]
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)
    wb.save(response)
    return response


def export_data_to_excel_splitcompany(request, id):
    subcom = SubCompany.objects.get(id=id)
    instances = SplitCompnay.objects.filter(sub_company=subcom)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{subcom.name}aplit.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet1')
    row_num = 0
    columns = ['date_time', 'drop_time', 'vehicle', 'drop', 'weight']
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)
    for instance in instances:
        my_date = instance.date_time.strftime('%d-%m-%Y')
        time = instance.drop_time.strftime('%H:%M')
        row_num += 1
        row = [my_date,  time, instance.vehicle, instance.drop, instance.weight]
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, cell_value)
    wb.save(response)
    return response


def updatesubview(request, id):
    number = request.POST.get("upadtenumber")
    numberview = request.POST.get("numberview")
    mydate = request.POST.get("date")
    filternumber = int(numberview)
    headcom = HeadCompany.objects.get(id = id)
    mynum = int(number)
    number_to_divide = mynum
    my_instances = SubCompany.objects.filter(head_company = headcom)[:filternumber]
    part_sizes = []
    mul = 1

    for i in my_instances:
        subcomadd = PreviousDataSubCompany(myid = i.id,head_company = i.head_company, name = i.name, line1 = i.line1, line2=i.line2, line3 = i.line3, line4 = i.line4, urlname = i.urlname, weight = i.weight, Invoicenumber = i.Invoicenumber, invoicedate = i.invoicedate, rangemin = i.rangemin, rangemax = i.rangemax)
        subcomadd.save()
        sumprint = mul * 4
        part_sizes.append(sumprint)
        mul+=1 

    part_sizes.reverse()
    total_size = sum(part_sizes)
    for instance, item2 in zip(my_instances, part_sizes):
        number = random.randint(200, 300)
        part = (item2 / total_size) * number_to_divide
        instance.weight = part
        instance.Invoicenumber = number
        instance.invoicedate = mydate
        instance.save()
    
    return redirect(f'/subcompanyone/{id}/')

class SubCompanyOneView(View):
    def get(self, request, id):
        subform = SubcompanyForm()
        headcom = HeadCompany.objects.get(id=id)
        subview = SubCompany.objects.filter(head_company = headcom)
        return render(request, "subcompanyone.html", {'subview' :subview, 'myid' : id, 'form' : subform})

    def post(self, request, id):
        form = SubcompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect(f'/subcompanyone/{id}')
        

class SubcompanyUpdateView(View):
    def get(self, request, id, id2):
        pi = SubCompany.objects.get(id=id)
        form = SubcompanyUpdateForm(instance=pi)
        return render(request, 'update_subcompany.html', {'form': form})
    
    def post(self, request, id, id2):
        pi = SubCompany.objects.get(id=id)
        form = SubcompanyUpdateForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect(f'/subcompanyone/{id2}/')
      
class SubcompanyDeleteView(View):
    def get(self, request, id, id2):
        pi = SubCompany.objects.get(id=id)
        pi.delete()
        messages.error(request, "Deleted Successfully")
        return redirect(f'/subcompanyone/{id2}/')

class ClientcompanyDeleteView(View):
    def get(self, request, id, id2):
        pi = ClientCompany.objects.get(id=id)
        pi.delete()
        messages.error(request, "Deleted Successfully")
        return redirect(f'/clientcompanyone/{id2}/')

class ClientCompanyOneView(View):
    def get(self, request, id):
        myid = id
        subform = ClientCompanyForm()
        headcom = HeadCompany.objects.get(id=id)
        clientview = ClientCompany.objects.filter(head_company = headcom)
        return render(request, "clientcompanyone.html", {'clientview' : clientview, 'myid' : myid,'form' : subform})

    def post(self, request, id):
        form = ClientCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect(f'/clientcompanyone/{id}')
        

class ClientcompanyUpdateView(View):
    def get(self, request, id, id2):
        pi = ClientCompany.objects.get(id=id)
        form = ClientcompanyUpdateForm(instance=pi)
        return render(request, 'update_clientcompany.html', {'form': form})
    
    def post(self, request, id, id2):
        pi = ClientCompany.objects.get(id=id)
        form = ClientcompanyUpdateForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect(f'/clientcompanyone/{id2}/')


class SubCompanySplit(View):
    def get(self, request, id):
        current_time = timezone.now()
        splitcompany = SubCompany.objects.get(id = id)
        valuenumber = splitcompany.weight
        rangenumber = splitcompany.rangemin
        rangenumbermin = splitcompany.rangemax
        date = splitcompany.invoicedate
        date = str(date)
        totalfetch = float(valuenumber)/float(rangenumber)
        totalfetch = floor(totalfetch)
        placelist = ["BT1 1AA", "BT1 1AL", "BT1 1AR", "BT1 1BG", "BT1 1BW", "BT1 1DA", "BT1 1DJ", "BT1 1DN", "BT1 1FF", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1DN", "BT1 1FF", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH"]
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{splitcompany.name}aplit.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')
        row_num = 0
        columns = ['date_time', 'drop_time', 'vehicle', 'drop', 'weight']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)
        value = float(valuenumber)
        num_parts = totalfetch

        total = value
        n = num_parts
        range_min = float(rangenumbermin)
        range_max = float(rangenumber)
     
        numbers = []
        for i in range(n):
            num = random.uniform(range_min, range_max)
            num = round(num, 2)  
            numbers.append(num)

        numbers.append(total - sum(numbers))
        numbers = [round(num, 2) for num in numbers]
        splitcompanyview = SplitCompnay.objects.filter(sub_company = splitcompany).count()
        my_models_to_delete = SplitCompnay.objects.filter(sub_company = splitcompany).order_by('id')[:splitcompanyview]
        my_date = datetime.strptime(date, '%Y-%m-%d').date()
        for my_model in my_models_to_delete:
            my_model.delete()

        drop = 0
        for i in range(n+1):
            if drop <= 5:
                drop+=1
                
            else:
                my_date = my_date + timedelta(days=int(1))
                drop = 1
           
            
            date_time = my_date
            drop_time = current_time
            vehicle = placelist[i]
            drop = drop
            if numbers[i] > 0:
                weight = numbers[i]
            new_date = date_time.strftime('%d-%m-%Y')
            new_time = drop_time.strftime('%H:%M')
            row_num += 1
            row = [new_date, new_time, vehicle, drop, weight]
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response

class ClientCompanySplit(View):
    def get(self, request, id):
        current_time = timezone.now()
        splitcompany = ClientCompany.objects.get(id = id)
        valuenumber = splitcompany.weight
        rangenumber = splitcompany.rangemin
        rangenumbermin = splitcompany.rangemax
        date = splitcompany.invoicedate
        date = str(date)
        totalfetch = int(valuenumber)/float(rangenumber)
        totalfetch = floor(totalfetch)
        placelist = ["BT1 1AA", "BT1 1AL", "BT1 1AR", "BT1 1BG", "BT1 1BW", "BT1 1DA", "BT1 1DJ", "BT1 1DN", "BT1 1FF", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1DN", "BT1 1FF", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH", "BT1 1FJ", "BT1 1FH"]
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{splitcompany.name}aplit.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Sheet1')
        row_num = 0
        columns = ['date_time', 'drop_time', 'vehicle', 'drop', 'weight']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)
        value = int(valuenumber)
        num_parts = totalfetch
        total = value
        n = num_parts
        range_min = float(rangenumbermin)
        range_max = float(rangenumber)
        numbers = []
        for i in range(n):
            num = random.uniform(range_min, range_max)
            numbers.append(num)
        
        numbers.append(total - sum(numbers))
        numbers = [round(num, 2) for num in numbers]
        numbers = numbers
        my_date = datetime.strptime(date, '%Y-%m-%d').date()
        drop = 0
        for i in range(n+1):
            if drop <= 5:
                drop+=1
            else:
                my_date = my_date + timedelta(days=int(1))
                drop = 1
            date_time = my_date
            drop_time = current_time
            vehicle = placelist[i]
            drop = drop
            if numbers[i] > 1:
                weight = numbers[i]
            new_date = date_time.strftime('%d-%m-%Y')
            new_time = drop_time.strftime('%H:%M')
            row_num += 1
            row = [new_date, new_time, vehicle, drop, weight]
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)
        wb.save(response)
        return response


class InvoiceDateUpdateView(View):
    
    def post(self, request):
        
        date = request.POST["date"]
        id = request.POST["myid"]
        my_instances = SubCompany.objects.get(id = id)
        subcomadd = PreviousDataSubCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()
        
        my_instances.invoicedate = date
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

class InvoiceNumberUpdateView(View):
    def post(self, request):
        innumber = request.POST["invoicenumber"]
        id = request.POST["myid"]
        my_instances = SubCompany.objects.get(id = id)
        subcomadd = PreviousDataSubCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()

        my_instances.Invoicenumber = innumber
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

class UpdateClinetViewWeight(View):
    def post(self, request):
        myid = request.POST['myid']
        weight = request.POST["weight"]
        my_instances = ClientCompany.objects.get(id = myid)
        subcomadd = PreviousDataClientCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()
        my_instances.weight = float(weight)
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class UpdateClinetViewWeight(View):
    def post(self, request):
        myid = request.POST['myid']
        weight = request.POST["weight"]
        my_instances = ClientCompany.objects.get(id = myid)
        subcomadd = PreviousDataClientCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()
        my_instances.weight = weight
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class UpdateClinetViewInvoice(View):
    def post(self, request):
        myid = request.POST['myid']
        invoicenumber = request.POST["invoicenumber"]
        my_instances = ClientCompany.objects.get(id = myid)
        subcomadd = PreviousDataClientCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()
        my_instances.Invoicenumber  = invoicenumber
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


class UpdateClinetViewDate(View):
    def post(self, request):
        myid = request.POST['myid']
        indate = request.POST["invoicedate"]
        my_instances = ClientCompany.objects.get(id = myid)
        subcomadd = PreviousDataClientCompany(myid = my_instances.id,head_company = my_instances.head_company, name = my_instances.name, line1 = my_instances.line1, line2=my_instances.line2, line3 = my_instances.line3, line4 = my_instances.line4, urlname = my_instances.urlname, weight = my_instances.weight, Invoicenumber = my_instances.Invoicenumber, invoicedate = my_instances.invoicedate, rangemin = my_instances.rangemin, rangemax = my_instances.rangemax)
        subcomadd.save()
        my_instances.invoicedate = indate
        my_instances.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))


def updateclientview(request, id):
    mydate = request.POST.get("date")
    headcom = HeadCompany.objects.get(id = id)
    my_instances = ClientCompany.objects.filter(head_company = headcom)
    for instance in my_instances:
        instance.invoicedate = mydate
        instance.save()
    return redirect(f'/clientcompanyone/{id}/')

def export_data_to_excel_clientcompany(request):
    your_model_resource = ClientCompanyModelResource()
    dataset = your_model_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clientcompany.xls"'
    return response


def render_pdf_view_clientcompany(request, id):
    clientcompany = ClientCompany.objects.get(id=id)
    name = clientcompany.name
    template_path = 'maintemplate.html'
    context = {'clientcompany': clientcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    
    return response


def render_pdf_view_clientcompany_one(request, id):
    clientcompany = ClientCompany.objects.get(id=id)
    name = clientcompany.name
    template_path = 'maintemplate2.html'
    context = {'clientcompany': clientcompany}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    
    return response

def import_excel(request):
    if request.method == 'POST' and request.FILES['file']:
        excel_file = request.FILES['file']
        df = pd.read_excel(excel_file, engine='xlrd')
        for index, row in df.iterrows():
            column1_value = row['name']
            column2_value = row['line1']
            column3_value = row['line2']
            column4_value = row['line3']
            column5_value = row['line4']
            column6_value = row['weight']
            column7_value = row['Invoicenumber']
            column8_value = row['date']
            column9_value = row['invoicedate']

            try:
                model_instance = SubCompany.objects.get(name=column1_value)
                date_object = datetime.strptime(column8_value, '%d-%m-%Y')
                django_date_format = date_object.strftime('%Y-%m-%d')

                date_object_invoice = datetime.strptime(column9_value, '%d-%m-%Y')
                django_date_format_invoice = date_object_invoice.strftime('%Y-%m-%d')

                model_instance.name = column1_value
                model_instance.line1 = column2_value
                model_instance.line2 = column3_value
                model_instance.line3 = column4_value
                model_instance.line4 = column5_value
                model_instance.weight = column6_value
                model_instance.Invoicenumber = column7_value
                model_instance.date = django_date_format
                model_instance.invoicedate = django_date_format_invoice
                model_instance.save()

            except SubCompany.DoesNotExist:
                pass
            
        return redirect(request.META.get('HTTP_REFERER', '/'))

class PreviousSubCom(View):
    def get(self, request, id):
        headcom = HeadCompany.objects.get(id=id)
        subview = PreviousDataSubCompany.objects.filter(head_company__id = id)
        return render(request, 'previoussubcom.html', {'subview' : subview, 'myid' : id, 'name': headcom.name})


class PreviousSubComDelete(View):
    def get(self, request, id):
        subview = PreviousDataSubCompany.objects.get(id = id)
        subview.delete()
        return redirect(f'/previoussubcom/{subview.head_company.id}/')



class PreviousSubClient(View):
    def get(self, request, id):
        headcom = HeadCompany.objects.get(id=id)
        subview = PreviousDataClientCompany.objects.filter(head_company__id = id)
        return render(request, 'previoussubclient.html', {'subview' : subview, 'myid' : id, 'name': headcom.name})


class PreviousSubClientDelete(View):
    def get(self, request, id):
        subview = PreviousDataClientCompany.objects.get(id = id)
        subview.delete()
        return redirect(f'/previoussubclient/{subview.head_company.id}/')
