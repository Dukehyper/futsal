from django.urls import path
from .views import render_pdf_view, CustomerListview, customer_render_pdf_view
from  . import views

app_name='customers'

urlpatterns = [
    path('pdf/', CustomerListview.as_view(), name='customer-list-view'),
    path('test/',render_pdf_view, name='test-view'),
    path('pdf/<pk>/', customer_render_pdf_view, name='customer-pdf-view'),
   
    path('', views.contact, name="contact"),
    path('feedback/', views.feedback, name="feedback")
]
