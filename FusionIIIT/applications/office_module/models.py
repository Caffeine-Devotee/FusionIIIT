import datetime
from django.db import models
from applications.academic_information.models import Student, Grades, Meeting
from applications.globals.models import Staff, Faculty


class Member(models.Model):
	member_id = models.ForeignKey(Faculty)
	meeting_id = models.ForeignKey(Meeting)

	class Meta:
		db_table = 'Member'
		unique_together = (('member_id', 'meeting_id'))

	def __str__(self):
			return str(self.member_id)
