# -*- coding: utf-8 -*-  

from django.http import HttpResponse
try:
    import json
except ImportError:
    import simplejson as json

from shequ.models import Shequ,ZhiBu,Mobile


def shequ(request):
	result = []
	success = False
	try:
		list = Shequ.objects.all()
		result = [{"id":t.id,"name":t.name} for t in list]
		success = True
	except:
		pass

	json_str = json.dumps({"result":result,"success":success})
	callback = request.GET.get('callback')
	if callback:
		return HttpResponse("%s(%s)"%(callback,json_str))
	else:
   		return HttpResponse(json_str, content_type="application/json")


def zhibu(request,shequ_id):
	result = []
	success = False
	try:
		list = ZhiBu.objects.filter(shequ=Shequ.objects.get(pk=shequ_id)).filter(is_display=True)
		result = [{"id":t.id,"name":t.name,"sort":t.sort,"add_time":t.add_time.strftime('%Y-%m-%d %H:%M:%S')} for t in list]
		success = True
	except:
		pass
	json_str = json.dumps({"result":result,"success":success})
	callback = request.GET.get('callback')
	if callback:
		return HttpResponse("%s(%s)"%(callback,json_str))
	else:
   		return HttpResponse(json_str, content_type="application/json")

def mobile(request,zhibu_id):
	result = []
	success = False
	try:
		list = Mobile.objects.filter(zhibu=ZhiBu.objects.get(pk=zhibu_id))
		result = [{"id":t.id,"name":t.name,"mobile":t.mobile,"phone":t.phone,"sort":t.sort,"add_time":t.add_time.strftime('%Y-%m-%d %H:%M:%S')} for t in list]
		success = True
	except:
		pass
	json_str = json.dumps({"result":result,"success":success})
	callback = request.GET.get('callback')
	if callback:
		return HttpResponse("%s(%s)"%(callback,json_str))
	else:
   		return HttpResponse(json_str, content_type="application/json")


