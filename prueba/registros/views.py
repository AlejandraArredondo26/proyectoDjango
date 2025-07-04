from django.shortcuts import render, redirect
from .models import *
from .forms import ComentarioContactoForm
from .models import ComentarioContacto


# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save() #inserta
            return redirect("Comentario")

    form = ComentarioContactoForm()
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")


def registros(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request, "registros/comentario.html", {'comentarios': comentarios})
