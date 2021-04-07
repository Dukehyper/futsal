from django.contrib import admin
from .models import Customer, Feedback, Ground, Shift, Logo


# Register your models here.
admin.site.register(Ground)
admin.site.register(Shift)
admin.site.register(Logo)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','fb_name','email','subject','message',)
    list_display_link = ('id','fb_name,')

admin.site.register(Feedback, FeedbackAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','contact','ground','shift',)
    list_display_link = ('id','name,')

admin.site.register(Customer, CustomerAdmin)