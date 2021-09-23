from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Malade
from malade.form import MaladeForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    malades = Malade.objects.all()
    list_malades = list(malades)
    compte_malade_list = len(list_malades)
    context = {'compte_malade_list':compte_malade_list}
    return render(request,'malade/index.html',context)

class Maladeform(CreateView):
    template_name = "malade/malade_form.html"
    model = Malade
    form = MaladeForm
    fields = "__all__"
    def form_valid(self,form):
        if form.is_valid():
            form.save()
            #messages.success(self,'le malade a bien été enregistré')
            return redirect('/')
        else:
            form = MaladeForm
            return redirect('/')
    


def maladelist(request):
    malades = Malade.objects.all()
    malades = list(malades)
    return render(request,'malade/malade_list.html',{'malades':malades})


class MaladeUpdate(UpdateView):
    model = Malade
    fields = "__all__"
    template_name = "malade/malade_update.html"
    form = MaladeForm
    def form_valid(self,form):
        if form.is_valid():
            form.save()
            #messages.success(self,'le malade a bien été enregistré')
            return redirect('/')
        else:
            form = MaladeForm
            return redirect('/')

def delete(request, id):
    malade = Malade.objects.get(id=id)
    malade.delete()
    return redirect("/")


def search(request):
    given_name = request.POST['name']
    malades = Malade.objects.filter(nom=given_name)
    return render(request,'malade/malade_list.html',{'malades':malades})