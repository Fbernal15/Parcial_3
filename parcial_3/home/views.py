from django.shortcuts import render, redirect,get_object_or_404
from django.template import loader
from .models import Nota
from .forms import NotasForm
from django.http import HttpResponse
from datetime import date, datetime
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    print(request.user)
    #consultar animales y categorias
    notas= Nota.objects.filter(usuario=request.user)

    #Obtener el template
    template = loader.get_template("index.html")
    #Agregar el contexto
    context = {"notas": notas}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))



#DESPUES DE ALEJA

def borrarNota(request,id):
    #Obtener el template
    template = loader.get_template("borrar.html")

    #Buscar el producto
    obj = get_object_or_404(Nota, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('index')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))


def editarNota(request,id):
    #Obtener el template
    template = loader.get_template("editar.html")
    #Buscar Producto
    obj = get_object_or_404(Nota, id = id)
    #formulario que contiene la instancia
    form = NotasForm(request.POST or None, instance = obj)
    if form.is_valid():
        nota = form.save(commit=False)
        form.save()
        return redirect('index')   
    #Agregar el contexto
    context = {'form': form, 'note': obj}
    return render(request, 'editar.html', context)

def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('index')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html")
    return HttpResponse(template.render(context,request))

    

def principal(request):
    return render(request, 'principal.html')

def verNota(request, id):
    #Consultar producto 
    nota = Nota.objects.get(id=id)           

    #Consultar datos de producto
    context = {'nota':nota}
    #Obtener el template
    template = loader.get_template("ver.html")

    return HttpResponse(template.render(context,request))


@login_required
def crearNota(request):
    # Obtener el template
    template = loader.get_template("nueva_nota.html")

    if request.method == "POST":
        form = NotasForm(request.POST)
        if form.is_valid():
            nota_nueva = form.save(commit=False)
            nota_nueva.usuario = request.user
            nota_nueva.save()
            return redirect('index')
    else:
        form = NotasForm()

    context = {'form': form}
    return HttpResponse(template.render(context, request))