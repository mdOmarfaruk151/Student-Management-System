from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin

class HomeView(TemplateView):
    template_name = "home.html"

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy('student_list')
    success_message = "Student deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"


class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        course = self.request.GET.get('course')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone_number__icontains=search)
            )

        if course:
            queryset = queryset.filter(course=course)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Student.objects.values_list(
            'course', flat=True
        ).distinct()
        return context