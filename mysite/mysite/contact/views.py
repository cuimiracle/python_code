from django.core.mail import send_mail
from django.http import HttpResponseRedirect    
from django.shortcuts import render
from mysite.contact.forms import ContactForm

def contact(request):
    print 'contact'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

#            send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('testemail_1', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site!'}
        )
    return render(request, 'contact_form_2.html', {'form': form})


