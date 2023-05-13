from django.shortcuts import render, redirect
from django.views import View
from excelapp.models import HeadCompany, SubCompany, ClientCompany, SplitCompnay
from django.http import HttpResponse
from .resources import HeadCompanyModelResource, SubCompanyModelResource, ClientCompanyModelResource, SplitCompanyModelResource
from .forms import HeadForm, SubcompanyForm, ClientCompanyForm, SubcompanyUpdateForm, ClientcompanyUpdateForm
from django.shortcuts import get_object_or_404, redirect
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

# Create your views here.
class HomeView(View):
    def get(self, request):
    
        database_name = settings.DATABASES['default']['NAME']
        database_user = settings.DATABASES['default']['USER']
        database_password = settings.DATABASES['default']['PASSWORD']

        print(f"Database Name: {database_name}")
        print(f"Database User: {database_user}")
        print(f"Database Password: {database_password}")
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


def export_data_to_excel_headcompany(request):
    your_model_resource = HeadCompanyModelResource()
    dataset = your_model_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="headcompany.xls"'
    return response


class SubCompanyView(View):
    def get(self, request):
        subform = SubcompanyForm()
        subview = SubCompany.objects.all()
        return render(request, "subcompany.html", {'subview' :subview, 'form' : subform})
    def post(self, request):
        form = SubcompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subcompany')
        else:
            return redirect('/subcompany')
        


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
  
    subcompany_price = subcompany.weight * subcompany.head_company.unit_price

  
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
    # Write the data rows to the Excel file
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
    filternumber = int(numberview)
    headcom = HeadCompany.objects.get(id = id)
    mynum = int(number)
    number_to_divide = mynum
    my_instances = SubCompany.objects.filter(head_company = headcom)[:filternumber]
    part_sizes = []
    mul = 1; 

    for i in my_instances:
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
        instance.save()
    
    return redirect(f'/subcompanyone/{id}/')





class SubCompanyOneView(View):
    def get(self, request, id):
        myid = id
        headcom = HeadCompany.objects.get(id=id)
        subview = SubCompany.objects.filter(head_company = headcom)
        return render(request, "subcompanyone.html", {'subview' :subview, 'myid' : id})



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
            return redirect(f'/subcompanyone/{id2}/')
      
       



class ClientCompanyView(View):
    def get(self, request):
        subform = ClientCompanyForm()
        subview = ClientCompany.objects.all()
        return render(request, "clientcompany.html", {'subview' :subview, 'form' : subform})
    def post(self, request):
        form = ClientCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientcompany')
        else:
            return redirect('/clientcompany')


class ClientCompanyOneView(View):
    def get(self, request, id):
        myid = id
        headcom = HeadCompany.objects.get(id=id)
        clientview = ClientCompany.objects.filter(head_company = headcom)
        return render(request, "clientcompanyone.html", {'clientview' : clientview, 'myid' : myid})


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

        import random

        total = value
        n = num_parts
        range_min = float(rangenumbermin)
        range_max = float(rangenumber)

     
        numbers = []
        for i in range(n):
            num = random.uniform(range_min, range_max)
            print(num)
            
            numbers.append(num)
        
       
        numbers.append(total - sum(numbers))

        print(numbers)

        mynumber = len(numbers)
      
        numbers = [round(num, 2) for num in numbers]


        numbers = numbers

        

    
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
           
            
            sub_company = splitcompany.name
            date_time = my_date
            drop_time = current_time
            vehicle = placelist[i]
            drop = drop
            weight = num
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

        import random

        total = value
        n = num_parts
        range_min = float(rangenumbermin)
        range_max = float(rangenumber)

  
        numbers = []
        for i in range(n):
            num = random.uniform(range_min, range_max)
            print(num)
            numbers.append(num)
        
    
        numbers.append(total - sum(numbers))

        print(numbers)

        mynumber = len(numbers)
      
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
           
            
            sub_company = splitcompany.name
            date_time = my_date
            drop_time = current_time
            vehicle = placelist[i]
            drop = drop
            weight = num
            new_date = date_time.strftime('%d-%m-%Y')
            new_time = drop_time.strftime('%H:%M')
            row_num += 1
            row = [new_date, new_time, vehicle, drop, weight]
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response





def updateclientview(request, id):
    number = request.POST.get("upadtenumber")
    numberview = request.POST.get("numberview")
    filternumber = int(numberview)
    headcom = HeadCompany.objects.get(id = id)
    mynum = int(number)
    number_to_divide = mynum
    my_instances = ClientCompany.objects.filter(head_company = headcom)[:filternumber]

    part_sizes = []  

    mul = 1; 

    for i in my_instances:
        sumprint = mul * 4
        part_sizes.append(sumprint)
        mul+=1
    
    total_size = sum(part_sizes)
    
    for instance, item2 in zip(my_instances, part_sizes):
        number = random.randint(200, 300)
        part = (item2 / total_size) * number_to_divide
        instance.weight = part
        instance.Invoicenumber = number
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

    template_path = 'clientcompanypdf1.html'

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

