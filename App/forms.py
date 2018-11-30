from django import forms
from django.contrib.auth.models import User
from App.models import *
from django.http import HttpResponseRedirect,HttpResponse


class ComplainForm(forms.ModelForm):
    class Meta():
        model = Complains
        fields = ['LabName',  'Issue', 'ResolvedValue']


class NoticeForm(forms.ModelForm):
    class Meta():
        model = Notice
        fields = ['IssuedOn', 'Text']


class TimeTableForm(forms.ModelForm):
    class Meta():
        model = LabSchedule
        fields = ['Day','LabName']


class UpdateIssueStatusForm(forms.ModelForm):
    class Meta():
        model = Complains
        fields = ['LabName','ResolvedValue']
