from django.shortcuts import render, redirect
from .models import *
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404


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

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentario.html",{'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html",{'comentarios':comentarios})
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
