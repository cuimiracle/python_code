from django.http import HttpResponse, Http404
# from django.template import Template, Context
# from django.template.loader import get_template
from django.shortcuts import render
import datetime
import json
# import os.path
from books.models import Publisher
from mysite.books.models import Book
from mysite.component.common_function import *

# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect

def hello(request):
    return HttpResponse("Hello world")

my_homepage_view = hello

def current_datetime(request):
    now = datetime.datetime.now()
    # Simple way of using templates from the filesystem.
    # This is BAD because it doesn't account for missing files!

    # temp_path = os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')
    # fp = open(temp_path+"/mytemplate.html")
    # t = Template(fp.read())
    # fp.close()

    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))

    # return render(request, 'socket_checkPort/current_datetime.html', {'current_date': now})
    # return HttpResponse(html)
    
    return render(request, 'current_datetime.html', {'current_date': now})
    

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)

    return render(request, 'hours_ahead.html', locals())

def first_app(request):
    publisher_list = Publisher.objects.all()
    return render(request, 'first_app.html', {'publisher_list': publisher_list})

def current_url_view_good(request):
    requestList = request.__dict__.items()
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return render(request, 'request_list.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'errors': errors})

# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('testemail_1') and '@' not in request.POST['testemail_1']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
# #             send_mail(
# #                 request.POST['subject'],
# #                 request.POST['message'],
# #                 request.POST.get('testemail_1', 'cuimiracle@gmail.com'),
# #                 ['cuimiracle@gmail.com'],
# #             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request, 'contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'testemail_1': request.POST.get('testemail_1', ''),
#     })







