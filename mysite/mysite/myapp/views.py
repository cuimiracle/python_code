from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect    
from django.shortcuts import render
from mysite.myapp.models import *
from mysite.component.common_function import *
import json

def testFirstReq(request):
    # print '111111'
    if request.method == 'POST':
        # print request.POST
        pass
    else:
        pass
    response = HttpResponse(json.dumps({"key": "value", "key2": "value"}), content_type='application/json')  
    # response["Access-Control-Allow-Origin"] = "*"  
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"  
    # response["Access-Control-Max-Age"] = "1000"  
    # response["Access-Control-Allow-Headers"] = "*"
    return response
    
def getNews(request):
    re = []

    if request.method == 'GET' and request.GET.has_key('action'):
        if request.GET['action'] == 'get_newest_20':
            return_object = News.objects.raw('SELECT n.id,n.title,n.content,c.title AS category_title FROM myapp_news AS n,myapp_category AS c WHERE n.category_id = c.id')
        else:  
            pass
        
    if 'return_object' in locals():    
        for x in return_object:
            aDict = {attr:value for attr,value in x.__dict__.items() if attr <> '_state'}
            re.append(aDict) 
    
    response = HttpResponse(json.dumps(re), content_type='application/json')
    return response

def publishNews(request):
    re = dict(result = False);
    if request.method == 'GET':
        should_exist_params = ('title','content','publish_time','category_id')
        Tools_class = Tools()
        try:
            has_exist_params = Tools_class.hasExistParams(request_obj = request, item = should_exist_params, request_method = 'GET')
            if has_exist_params == True:
                N = News(title=request.GET['title'],content=request.GET['content'],publish_time=request.GET['publish_time'],category_id=request.GET['category_id'])
                try:
                    N.save()
                    re['result'] = True
                    re['last_insert_id'] = N.id
                except Exception,e:
                    if e.__dict__.has_key('messages') and len(e.__dict__['messages']) > 0:
                        re['message'] = e.__dict__['messages'][0]
            else:
                re['message'] = 'without enough parameters'
        except TypeError,e:
            pass

    response = HttpResponse(json.dumps(re), content_type='application/json')
    return response

def addCategory(request):
    re = dict(result = False);
    if request.method == 'GET':
        should_exist_params = ('title','description')
        Tools_class = Tools()
        try:
            has_exist_params = Tools_class.hasExistParams(request_obj = request, item = should_exist_params, request_method = 'GET')
            if has_exist_params == True:
                C = Category(title=request.GET['title'],description=request.GET['description'])
                try:
                    C.save()
                    re['result'] = True
                    re['last_insert_id'] = C.id
                except Exception,e:
                    if e.__dict__.has_key('messages') and len(e.__dict__['messages']) > 0:
                        re['message'] = e.__dict__['messages'][0]
            else:
                re['message'] = 'without enough parameters'
        except TypeError,e:
            pass

    response = HttpResponse(json.dumps(re), content_type='application/json')
    return response

def subscribeNews(request):
    re = dict(result = False);
    if request.method == 'GET':
        should_exist_params = ('news_id','user_id')
        Tools_class = Tools()
        try:
            has_exist_params = Tools_class.hasExistParams(request_obj = request, item = should_exist_params, request_method = 'GET')
            if has_exist_params == True:
                try:
                    N = News.objects.get(pk=request.GET['news_id'])
                    U = User.objects.get(pk=request.GET['user_id'])
                    N.users.add(U)
                    re['result'] = True
                except Exception,e:
                    if e.__dict__.has_key('messages') and len(e.__dict__['messages']) > 0:
                        re['message'] = e.__dict__['messages'][0]
            else:
                re['message'] = 'without enough parameters'
        except TypeError,e:
            pass

    response = HttpResponse(json.dumps(re), content_type='application/json')
    return response

def desubscribeNews(request):
    re = dict(result = False);
    if request.method == 'GET':
        should_exist_params = ('news_id','user_id')
        Tools_class = Tools()
        try:
            has_exist_params = Tools_class.hasExistParams(request_obj = request, item = should_exist_params, request_method = 'GET')
            if has_exist_params == True:
                try:
                    N = News.objects.get(pk=request.GET['news_id'])
                    U = User.objects.get(pk=request.GET['user_id'])
                    N.users.remove(U)
                    re['result'] = True
                except Exception,e:
                    if e.__dict__.has_key('messages') and len(e.__dict__['messages']) > 0:
                        re['message'] = e.__dict__['messages'][0]
            else:
                re['message'] = 'without enough parameters'
        except TypeError,e:
            pass

    response = HttpResponse(json.dumps(re), content_type='application/json')
    return response




