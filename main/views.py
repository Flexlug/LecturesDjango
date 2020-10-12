from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Lectures
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import LecturesForm, SubjectForm



def index(request):
    subject = Subject.objects.order_by('-name')
    return render(request, 'main/index.html', {'subject': subject})


def subject_list(request, subject_slug=None):
    subject = None
    subjects = Subject.objects.all()
    lectures = Lectures.objects.all()
    if subject_slug:
        subject = get_object_or_404(Subject, slug=subject_slug)
        lectures = lectures.filter(subject=subject)
    return render(request,
                  'main/subject.html',
                  {'subject': subject,
                   'subjects': subjects,
                   'lectures': lectures})

def lectures_detail(request):
    lectures = Lectures.object.all()
    return render(request, 'main/details_view.html', {'lectures': lectures})

class NewsDetailView(DetailView):
    model = Lectures
    template_name = 'main/details_view.html'
    context_object_name = 'lectures'

class NewsUpdateView(UpdateView):
    model = Lectures
    template_name = 'main/create.html'
    success_url = '/'
    form_class = LecturesForm

class NewsDeleteView(DeleteView):
    model = Lectures
    success_url = '/'
    template_name = 'main/news-delete.html'

def create(request):
    error = ' '
    if request.method == 'POST':
        form = LecturesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Формы была неверной'

    form = LecturesForm()

    data = {
        'error': error,
        'form': form
    }

    return render(request, 'main/createnew.html', data)

def creates(request):
    error = ' '
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Формы была неверной'

    form = SubjectForm()

    data = {
        'error': error,
        'form': form
    }

    return render(request, 'main/creates.html', data)