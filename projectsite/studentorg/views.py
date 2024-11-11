from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.models import OrgMember
from studentorg.models import Student
from studentorg.models import College
from studentorg.models import Program
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org edit.html'
    success_url = reverse_lazy('organization-list')
    
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"
    
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
        return qs
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')
    
class OrgMemberDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org edit.html'
    success_url = reverse_lazy('orgmember-list')
    
class HomePageView(ListView):
    model = OrgMember
    context_object_name = 'home'
    template_name = "home.html"
    
class OrgMemberList(ListView):
    model = Organization
    context_object_name = 'orgmember'
    template_name = 'org_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student__icontains=query) |
                            Q(organization__icontains=query) | Q(date_joined__icontains=query))
        return qs
    
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('orgmember-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'org_del.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = OrganizationForm
    template_name = 'org edit.html'
    success_url = reverse_lazy('student-list')
    
class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = "home.html"
    
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'org_list.html'
    paginate_by = 5
    
class StudentCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('student-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'org_del.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = OrganizationForm
    template_name = 'org edit.html'
    success_url = reverse_lazy('college-list')
    
class HomePageView(ListView):
    model = College
    context_object_name = 'home'
    template_name = "home.html"
    
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'org_list.html'
    paginate_by = 5
    
class CollegeCreateView(CreateView):
    model = College
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('college-list')
    

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'org_del.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = OrganizationForm
    template_name = 'org edit.html'
    success_url = reverse_lazy('program-list')
    
class HomePageView(ListView):
    model = Program
    context_object_name = 'home'
    template_name = "home.html"
    
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'org_list.html'
    paginate_by = 5
    
class ProgramCreateView(CreateView):
    model = Program
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('program-list')