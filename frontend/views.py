from django.shortcuts import render

from .artikel import *

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
  return render(request, 'artikel.html', {'list_artikel': list_artikel.values()})  

def detailartikel(request, nama_artikel):
  artikel = list_artikel[nama_artikel]
  return render(request, 'detailartikel.html', {'artikel': artikel})  

def eventint(request):
  fashion_show_2015_imgs = [('fashionshow2015_' + str(i) + '.jpeg') for i in range(1,9)]
  fashion_show_2016_imgs = [('fashionshow2016_' + str(i) + '.jpeg') for i in range(1,15)]
  fashion_show_2017_imgs = [('fashionshow2017_' + str(i) + '.jpeg') for i in range(1,20)]
  return render(request, 'eventint.html', {'fashion_show_2015_imgs': fashion_show_2015_imgs, 'fashion_show_2016_imgs': fashion_show_2016_imgs, 'fashion_show_2017_imgs': fashion_show_2017_imgs})  

def eventkeg(request):
  eventkeg_imgs = [('eventkeg_' + str(i) + '.jpeg') for i in range(1,21)]
  return render(request, 'eventkeg.html', {'eventkeg_imgs': eventkeg_imgs})  

def eventsem(request):
  sem2015_imgs = [('seminar2015_' + str(i) + '.jpeg') for i in range(1,21)]
  sem2014_imgs = [('seminar2014_' + str(i) + '.jpeg') for i in range(1,11)]
  sem2016_imgs = [('seminar2016_' + str(i) + '.jpeg') for i in range(1,18)]
  talkshow_imgs = [('talkshow_' + str(i) + '.jpeg') for i in range(1,7)]
  return render(request, 'eventsem.html', {'sem2015_imgs': sem2015_imgs, 'sem2016_imgs': sem2016_imgs, 'sem2014_imgs': sem2014_imgs, 'talkshow_imgs': talkshow_imgs})  

def pendaftaranonline(request):
  return render(request, 'pendaftaranonline.html')  