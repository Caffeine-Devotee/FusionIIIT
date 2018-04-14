<<<<<<< HEAD
from django.contrib import admin

from .models import (DepartmentInfo, Designation, ExtraInfo, Faculty, Feedback,
                     Issue, IssueImage, Staff)
from applications.office_module.models import Member

# Register your models here.
admin.site.register(IssueImage)
admin.site.register(ExtraInfo)
admin.site.register(Issue)
admin.site.register(Feedback)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Faculty)
admin.site.register(DepartmentInfo)
admin.site.register(Designation)
=======
from django.contrib import admin

from .models import (DepartmentInfo, Designation, ExtraInfo, Faculty, Feedback,
                     HoldsDesignation, Issue, IssueImage, Staff)

admin.site.register(IssueImage)
admin.site.register(ExtraInfo)
admin.site.register(Issue)
admin.site.register(Feedback)
admin.site.register(Staff)
admin.site.register(Faculty)
admin.site.register(DepartmentInfo)
admin.site.register(Designation)
admin.site.register(HoldsDesignation)
>>>>>>> 8840ea3da5f4a670a7683a29f89c0509c75da90e
