from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from word.forms import QuestionForm
from . models import Question
from django.views.generic import TemplateView, CreateView

from django.views.generic import ListView
from .forms import NameForm
from .models import Person 
from .forms import SearchForm
from .forms import PersonFilterForm
from .models import Address
from .forms import AddressForm
 
def person_list(request):
    search_query = request.GET.get('search')
    if search_query:
        results = Person.objects.filter(name__contains=search_query).order_by('name')
    else:
        results = Person.objects.all().order_by('name')
    return render(request, 'person_list.html', {'persons': results, 'search_query': search_query })

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'  
    context_object_name = 'persons'

def get_queryset(self):
    search_query = self.request.GET.get('search', '')
    if search_query:
        return Person.objects.filter(name__contains=search_query).order_by('name')
    else:
        return Person.objects.all().order_by('name')
    
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['search_query'] = self.request.GET.get('search', '')
    return context

def filter_persons(request):
    form = PersonFilterForm(request.GET)
    persons = Person.objects.all()
    print("Request GET data:", request.GET)
    
    if form.is_valid():
        print("Form is valid")
        name_query = form.cleaned_data.get('name')
        city_query = form.cleaned_data.get('city')

        if name_query:
            persons = persons.filter(name__contains=name_query)

        if city_query:
            persons = persons.filter(city__contains=city_query)
    return render(request, 'person_list.html', {'form': form, 'persons': persons})

def your_view(request):
    if request.method == 'GET':
        form = PersonFilterForm(request.GET)
    if form.is_valid():
       name = form.cleaned_data['name']
       city = form.cleaned_data['city'] 
    else:
        form = PersonFilterForm()
    return render(request, 'person_list.html', {'form': form})

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

def get_queryset(self):
        queryset = super().get_queryset()
        name_query = self.request.GET.get('name')
        city_query = self.request.GET.get('city')
        
        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        
        if city_query:
            queryset = queryset.filter(city__icontains=city_query)
        return queryset

def post(self, request, *args, **kwargs):
    form = SearchForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data.get('q')
        queryset = Person.objects.filter(name__icontains=query).order_by('name')
        return render(request, self.template_name, {
            'persons': queryset,
            'form': form
            })
    else:
        queryset = self.get_queryset()
        return render(request, self.template_name, {
            'persons': queryset,
            'form': form
            })

class PersonCreateView(CreateView):
    model = Person
    form_class = NameForm
    template_name = 'name.html'
    success_url = reverse_lazy('person_list')  

    def form_valid(self, form):
        return super().form_valid(form)

def add(request, person_id=None):
    if person_id:
        person = get_object_or_404(Person, id=person_id)
    else:
        person = None
    
    if request.method == "POST":
       form = NameForm(request.POST, instance=person) 
       if form.is_valid():
           form.save()
           return redirect('person_list')
    else:
        form = NameForm(instance=person)
    return render(request, "name.html", {"form": form})

class Index(TemplateView):
    template_name = 'word/index.html'

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'person_list.html', {'addresses': addresses})


class CreateQuestion(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'word/question_form.html'
    success_url = reverse_lazy('index')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)