from django.contrib import admin
from django.urls import path, include

from .views import index, tentangpengajar, programlainnya, faq, artikel, detailartikel, eventint, eventkeg, eventsem, pendaftaranonline

urlpatterns = [
    path('', index, name="index"),
    path('tentangpengajar', tentangpengajar, name="tentangpengajar"),
    path('programlainnya', programlainnya, name="programlainnya"),
    path('faq', faq, name="faq"),
    path('pendaftaranonline', pendaftaranonline, name="pendaftaranonline"),
    path('artikel', artikel, name="artikel"),
    path('detailartikel', detailartikel, name="detailartikel"),
    path('eventint', eventint, name="eventint"),
    path('eventkeg', eventkeg, name="eventkeg"),
    path('eventsem', eventsem, name="eventsem"),

]
