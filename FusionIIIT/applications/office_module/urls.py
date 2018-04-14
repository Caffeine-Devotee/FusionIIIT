<<<<<<< HEAD
from django.conf.urls import url

from . import views

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^directorOffice/$', views.directorOffice, name='directorOffice'),
    url(r'^directorOffice/appoint', views.appoint, name='appoint'),
]
=======
from django.conf.urls import url

from . import views

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^officeOfDeanPnD/', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^officeOfHOD/', views.officeOfHOD, name='officeOfHOD'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
]
>>>>>>> 8840ea3da5f4a670a7683a29f89c0509c75da90e
