from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def tentangpengajar(request):
  return render(request, 'tentangpengajar.html')


def programlainnya(request):
  return render(request, 'programlainnya.html')  

def faq(request):
  return render(request, 'faq.html')  

def artikel(request):
  return render(request, 'artikel.html')  

def detailartikel(request):
  return render(request, 'detailartikel.html')  

def eventint(request):
  return render(request, 'eventint.html')  

def eventkeg(request):
  return render(request, 'eventkeg.html')  

def eventsem(request):
  return render(request, 'eventsem.html')  

def pendaftaranonline(request):
  return render(request, 'pendaftaranonline.html')  