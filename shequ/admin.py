# -*- coding: utf-8 -*-  


from django.contrib import admin
from shequ.models import Shequ, ZhiBu, Mobile


class ShequAdmin(admin.ModelAdmin):
    search_fields = ['name'] 


class ZhiBuAdmin(admin.ModelAdmin):
    search_fields = ['name'] 
    list_display    = ('name', 'shequ') 

class MobileAdmin(admin.ModelAdmin):
    search_fields = ['name'] 
    list_display    = ('name', 'mobile', 'phone') 


admin.site.register(Shequ, ShequAdmin)
admin.site.register(ZhiBu,ZhiBuAdmin)
admin.site.register(Mobile, MobileAdmin)


