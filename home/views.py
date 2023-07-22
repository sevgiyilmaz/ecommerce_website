from django.core.checks import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render

# Create your views here.
from django.template import loader

from home.models import Setting, ContactFormMessage, ContactFormu
from product.models import Product


def index(request):
  setting = Setting.objects.get(pk=1)
  context = {'setting':setting, 'page':'home'}
  return render(request, 'index.html',context)

  '''  template = loader.get_template('homebase.html')
  return HttpResponse(template.render())
'''

def hakkimizda(request):
  setting = Setting.objects.get(pk=1)
  context = {'setting':setting,'page':'hakkimizda'}
  return render(request, 'hakkimizda.html',context)

def computer(request):
  setting = Setting.objects.get(pk=1)
  context = {'setting':setting,'page':'computer'}
  return render(request, 'computer.html',context)

def products(request):
  setting = Setting.objects.get(pk=1)
  context = {'setting':setting,'page':'products'}
  return render(request, 'products.html',context)

def contact(request):
  setting = Setting.objects.get(pk=1)
  context = {'setting':setting,'page':'contact'}
  return render(request, 'contact.html',context)


def iletisim(request):

  if request.method == 'POST': #form post edildiyse
    form = ContactFormu(request.POST)
    if form.is_valid():
      data = ContactFormMessage() #model ile bağlantı kur
      data.name = form.cleaned_data['name'] #formdan bilgiyi al
      data.email = form.cleaned_data['email']
      data.phone = form.cleaned_data['phone']
      data.message = form.cleaned_data['message']
      data.save() #veritabanına kaydet
      messages.success(request,"Mesajınız başarıyla gönderilmiştir. Teşekkür ederiz.")
      return HttpResponseRedirect('/contact')

  setting = Setting.objects.get(pk=1)
  form =ContactFormu()
  context = {'setting':setting, 'form':form}
  return render(request, 'contact.html',context)