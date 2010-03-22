# Create your views here.
import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, Template, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.db.models import Q
from rota.models import RotaActivity, RotaItem, Team 
from backends.pdfexport import render_to_pdf
import settings

@login_required
def view_rota(request, year, month, day, template, pdf=None):
	
	# No additional security required here apart from a valid login. We allow all users to view 
	# their own rota plus the team and department rotas, and if they know the Edit Rota URL (hidden by default) they 
	# can load that page but not actually do anything in rota.views.edit_rota()

	cal = calendar.Calendar()
	if request.method == 'POST':
		pass
	else:
		now = datetime.datetime.now()										# now = datetime.datetime(2009, 9, 14, 17, 21, 29, 220270)
		today = datetime.date( now.year, now.month, now.day )

		if year and month and day:
			# User has asked for a specific week to be shown
			requested = datetime.date(int(year), int(month), int(day))	
		else:
			# Work out the days for this week
			requested = today
		
		this_week = calculate_week(requested)

	teams = Team.objects.all()
	
	if pdf: 
		return render_to_pdf(template, {'this_week': this_week, 'today': today, 'teams': teams, 'title': 'Rota', 'paper_orientation': 'landscape', 'paper_size': 'a3', 'files': settings.STATIC_DOC_ROOT }, filename="ROTA.pdf")
	else:
		return render_to_response(template, {'this_week': this_week, 'today': today, 'teams': teams }, context_instance=RequestContext(request))

@login_required
def edit_rota(request, year, month, day, shift, username):

	# Some security, if the user isn't allowed to edit the rota raise 404
	if not request.user.has_perm('rota.can_edit'):
		raise Http404
	
	date = datetime.date(int(year), int(month), int(day))	
	person = User.objects.get(username=username)
	activity = RotaActivity.objects.get(id=shift)

	try:
		r = RotaItem.objects.get(date=date, person=person)
	except RotaItem.DoesNotExist:
		r = RotaItem()	
			
	r.date=date	
	r.person=person
	r.activity=activity
	r.author=request.user
	r.save()
	return HttpResponse('Updated to %s' % r.activity )
	

def calculate_week(requested_date):

	''' Returns a list of days - this_week - given a date. '''

	cal = calendar.Calendar()
	day_of_week = calendar.weekday( requested_date.year, requested_date.month, requested_date.day ) 					# 0 = Monday, 1 = Tuesday, 2 = Wednesday
	monday_of_this_week = requested_date + datetime.timedelta(days=-day_of_week) 										# datetime.datetime(2009, 9, 14, 17, 21, 29, 220270)
	monday_of_this_week = datetime.date( monday_of_this_week.year, monday_of_this_week.month, monday_of_this_week.day )	# Abbreviate down to one day
	
	for week in cal.monthdatescalendar( requested_date.year, requested_date.month ):
		if monday_of_this_week in week:
			return week

