from django.contrib import admin
from .models import Customer, Feedback, Ground, Shift, Gallery, Notice


# Register your models here.
admin.site.register(Ground)
admin.site.register(Shift)
admin.site.register(Gallery)
admin.site.register(Notice)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','fb_name','email','subject','message',)
    list_display_link = ('id','fb_name,')

admin.site.register(Feedback, FeedbackAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact','ground','shift',)
    list_display_link = ('id','name,')

admin.site.register(Customer, CustomerAdmin)

admin.site.site_header = 'Danfe Futsal'                   
admin.site.index_title = 'Welcome to Danfe Futsal'  
admin.site.site_title = 'Danfe Futsal Dashboard' 