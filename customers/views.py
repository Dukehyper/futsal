from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer, Ground, Shift, Feedback, Gallery, Notice


class CustomerListview(ListView):
   model = Customer
   template_name='customers/main.html'

def customer_render_pdf_view(request,*args,**kwargs):
   pk = kwargs.get('pk')
   customer = get_object_or_404(Customer, pk=pk)
   template_path = 'customers/pdf2.html'
   context = {'customer': customer,}
    # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"' # if you want to download pdf
   #response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
   template = get_template(template_path)
   html = template.render(context)

    # create a pdf
   pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response


# Create your views here.
# def render_pdf_view(request):
#     template_path = 'customers/pdf2.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"' if you want to download pdf
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response)
#     # if error then show some funy view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# def contactform(request):
#    if request.method == "POST":
#       name = request.POST['name']
#       contact = request.POST['contact']
#       new_data = Customer.objects.create(name=name, contact=contact)
#       new_data.save()

#    return render(request, 'customers/contactform.html')

def contact(request):
   context = {
      'grounds' : Ground.objects.all(),
      'shifts' : Shift.objects.all(),
      'gallery' : Gallery.objects.all(),
      'notice' : Notice.objects.all()
   }
   if request.method == 'POST' and 'booked' in request.POST:
      error = ""
      name = request.POST['name']
      contact = request.POST['contact']
      ground = request.POST['ground']
      shift = request.POST['shift']

      # ground1 = request.POST['ground']
      # shift1 = request.POST['shift']
      if Customer.objects.filter(ground=ground, shift=shift).exists():
         booked = "false"
         context1 = {
            # 'message' : "already booked",
            'grounds' : Ground.objects.all(),
            'shifts' : Shift.objects.all(),
            'booked' : booked,
            'gallery' : Gallery.objects.all(),
            'notice' : Notice.objects.all()
         }
         return render(request, 'customers/index.html', context1)
      else:
         new_data = Customer.objects.create(name=name, contact=contact, ground=ground, shift=shift)
         new_data.save()
         booked = "true"
         context1 = {
            # 'message' : " Thank you for Booking ",
            'grounds' : Ground.objects.all(),
            'shifts' : Shift.objects.all(),
            'booked' : booked,
            'gallery' : Gallery.objects.all(),
            'notice' : Notice.objects.all()
            # 'customer' : Customer.objects.filter().order_by('-pk')[0]
            # 'customer' : Customer.objects.get().order_by('-pk')[0]
         }
         # return render(request, customer_render_pdf_view, context1)
         
         return render(request, 'customers/index.html', context1)

     
   
   if request.method == "POST" and 'feedback' in request.POST:
      fb_name=request.POST['fb_name']
      email=request.POST['email']
      subject=request.POST['subject']
      message=request.POST['message']
      new_data=Feedback.objects.create(fb_name=fb_name,email=email,subject=subject,message=message)
      new_data.save()

   return render(request, 'customers/index.html', context)

   