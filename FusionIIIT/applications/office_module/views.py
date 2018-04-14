<<<<<<< HEAD
from django.contrib.auth.models import User 
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from applications.academic_information.models import Meeting
from applications.globals.models import Faculty, ExtraInfo
from applications.office_module.models import Member
import datetime

def officeOfDeanStudents(request):
    context = {}

    return render(request, "officeModule/officeOfDeanStudents/officeOfDeanStudents.html", context)


def officeOfPurchaseOfficr(request):
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html", {})


def officeOfRegistrar(request):
    context = {}

    return render(request, "officeModule/officeOfRegistrar/officeOfRegistrar.html", context)


def officeOfDeanRSPC(request):
    context = {}

    return render(request, "officeModule/officeOfDeanRSPC/officeOfDeanRSPC.html", context)


def genericModule(request):
    context = {}

    return render(request, "officeModule/genericModule/genericModule.html", context)


def directorOffice(request):
    context = {}

    return render(request, "officeModule/directorOffice/directorOffice.html", context)


def appoint(request):
    print('there')
    purpose = request.POST.get('purpose')
    venue = request.POST.get('venue')
    adate = request.POST.get('adate')
    adate = adate.replace(",","")
    print(adate)
    adate = str(datetime.datetime.strptime(adate, '%B %d %Y'))[:10]
    print(adate)
    # if (adate==""):
    #     adate = None
    # print(datetime.date.today())
    member = request.POST.get('member')
    print(purpose,venue,adate,member)
    print('here 1')
    meetobj = Meeting(venue=venue, agenda=purpose, date=adate)
    meetobj.save()
    print('here 2')
    user = User.objects.get(username=member)
    info = ExtraInfo.objects.get(user=user)
    mem = Faculty.objects.get(id = info)
    print('here 3')
    print(mem)
    # meeting = Meeting.objects.get(id=meetobj.id)
    # print(meeting)
    appointobj = Member(member_id=mem, meeting_id=meetobj)
    print(appointobj)
    appointobj.save()

    return HttpResponseRedirect("/office/directorOffice/")
=======
from django.shortcuts import render


def officeOfDeanStudents(request):
    context = {}

    return render(request, "officeModule/officeOfDeanStudents/officeOfDeanStudents.html", context)


def officeOfPurchaseOfficr(request):
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html", {})


def officeOfRegistrar(request):
    context = {}

    return render(request, "officeModule/officeOfRegistrar/officeOfRegistrar.html", context)


def officeOfDeanRSPC(request):
    context = {}

    return render(request, "officeModule/officeOfDeanRSPC/officeOfDeanRSPC.html", context)


def officeOfDeanPnD(request):
    context = {}

    return render(request, "officeModule/officeOfDeanPnD/officeOfDeanPnD.html", context)


def officeOfHOD(request):
    context = {}

    return render(request, "officeModule/officeOfHOD/officeOfHOD.html", context)


def genericModule(request):
    context = {}

    return render(request, "officeModule/genericModule/genericModule.html", context)
>>>>>>> 8840ea3da5f4a670a7683a29f89c0509c75da90e
