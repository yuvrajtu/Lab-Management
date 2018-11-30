from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from django.views import generic

from django.urls import reverse_lazy

from App.forms import *
from App.models import *
# Create your views here.


def index(request):
    return render(request,'App/index.html')


def user_login(request):
    print("login page attempt")
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            #if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            #else:
                #return HttpResponse("Account Not Active")
        else:
            print("false login")
            return HttpResponseRedirect(reverse('login'))
    else:
        print("render part ran successfully")
        return render(request,'App/login.html')


@login_required
def user_logout(request):
    print("logout")
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class DeleteComplains(LoginRequiredMixin,generic.DeleteView):
    template_name = 'App/Teacher_dashboard.html'
    model = Complains
    success_url =reverse_lazy('dashboard')


@login_required
def dashboard(request):
    user_dashdata = Complains.objects.filter(author=request.user)
    ComplainsDic = {'dashdata': user_dashdata}
    return render(request, 'App/Teacher_dashboard.html', {'dashdata': user_dashdata})


class Dash(LoginRequiredMixin, generic.ListView):
    template_name='App/Dash.html'
    context_object_name='dashdata'

    def get_queryset(self):
        return Complains.objects.all()


class ComplainsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Complains
    form_class = ComplainForm
    template_name = 'App/AddComplains.html'

    def form_valid(self, form):
        AddComplains = form.save(commit=False)
        # form.instance.author = self.request.user
        AddComplains.author = self.request.user
        AddComplains.save()
        return redirect('dashboard')


class NoticeBoard(LoginRequiredMixin, generic.ListView):
    template_name='App/Notice.html'
    context_object_name='Notice'

    def get_queryset(self):
        return Notice.objects.all().order_by('IssuedOn')


class NoticeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'App/AddNotice.html'

    def form_valid(self, form):
        AddNotice = form.save(commit=False)
        AddNotice.save()
        return redirect('Notice')



class AttendentDetails(LoginRequiredMixin, generic.ListView):
    template_name='App/Attendents.html'
    context_object_name='LabAttendent'

    def get_queryset(self):
        return LabAttendent.objects.all().order_by('LabAssigned')


class FacultyDetails(LoginRequiredMixin, generic.ListView):
    template_name='App/Faculty.html'
    context_object_name='LabTeacher'

    def get_queryset(self):
        return LabTeacher.objects.all().order_by('TeacherName')


class TimeTable(LoginRequiredMixin,generic.CreateView):
    model = LabSchedule
    form_class = TimeTableForm
    template_name = 'App/TimeTable.html'
    context_object_name = 'LabSchedule'

    def get_queryset(self):
        # if self.request.method=='POST':
        #     return LabSchedule.objects.all()
        # else:
        return LabSchedule.objects.all()


from django.views.generic.edit import UpdateView


class StatusUpdate(UpdateView):
    model = Complains
    form_class = UpdateIssueStatusForm
    template_name = 'App/IssueUpdateView.html'

    def form_valid(self, form):
        issueupdate = form.save(commit=False)
        issueupdate.save()
        return redirect('dashboard_Att')



