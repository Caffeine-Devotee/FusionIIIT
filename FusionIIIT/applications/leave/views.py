from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from .handlers import (handle_faculty_leave_application,
                       handle_staff_leave_application,
                       handle_student_leave_application,
                       process_staff_faculty_application,
                       process_student_application, send_faculty_leave_form,
                       send_staff_leave_form, send_student_leave_form)


@login_required(login_url='/accounts/login')
def leave(request):

    user_type = request.user.extrainfo.user_type

    if request.method == 'POST':

        response = None

        if user_type == 'faculty':
            response = handle_faculty_leave_application(request)
        elif user_type == 'staff':
            response = handle_staff_leave_application(request)
        else:
            response = handle_student_leave_application(request)

        return response

    if user_type == 'faculty':
        response = send_faculty_leave_form(request)
    elif user_type == 'staff':
        response = send_staff_leave_form(request)
    else:
        response = send_student_leave_form(request)

    return response


@login_required(login_url='/accounts/login')
def process_request(request):
    if request.is_ajax():
        if request.POST.get('stud'):
            return process_student_application(request)

        return process_staff_faculty_application(request)
    return JsonResponse({'status': 'Failed'}, status=400)


@login_required(login_url='/accounts/login')
def get_leave_requests(request):
    return HttpResponse('Hey Works')
