from django.template import RequestContext
from django.shortcuts import render_to_response,render,redirect
from blog.models import Entrada, Mensajes

# Create your views here.
def home(request):
    context= RequestContext(request)
    entradas = Entrada.objects.all()
    return render_to_response('Inicio.html',{"entradas":entradas},context)

def mensaje(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == "POST":
        de_post = Entrada.objects.get(id=request.POST['id'])
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        men = Mensajes()
        men.nombre = nombre
        men.mensaje = mensaje
        men.pub_en = de_post
        men.save()
        mensajes = Mensajes.objects.filter(pb_en=de_post, able=True)

        return render_to_response('mensajes.html',{'mensajes':mensajes},context)

def boton_magico(request):
    context= RequestContext(request)
    return render_to_response('boton_magico.html',{},context)
def calculadora(request):
    context= RequestContext(request)
    return render_to_response('Calculadora.html',{},context)
def contactos(request):
    context= RequestContext(request)
    if request.method=="post":
        nombre = request.POST["Nombre"]
        email = request.POST["Email"]
        contenido = request.POST["Mensaje"]
        send_mail(str(nombre),str(contenido),email,["acairiaelemail@gmail.com"],fail_silently=False)
    return render_to_response('Contactos.html',{},context)
def conversor(request):
    context= RequestContext(request)
    return render_to_response('conversor.html',{},context)
def cronometro(request):
    context= RequestContext(request)
    return render_to_response('cronometro.html',{},context)
def cv(request):
    context= RequestContext(request)
    return render_to_response('CV.html',{},context)
def image(request):
    context= RequestContext(request)
    return render_to_response('Image.html',{},context)

def verpost(request,id_post):
    context= RequestContext(request)
    mi_post = Entrada.objects.get(id = id_post)
    if request.method=="POST":
        nombre=request.POST["nombre"]
        contenido=request.GET["mensaje"]
        mensaje=Mensajes()
        mensaje.nombre=nombre
        mensaje.mensaje=contenido
        mensaje.pub_en=mi_post
        mensaje.save()
    mensaje = Mensajes.objects.filter(pub_en = id_post)
    return render_to_response('post.html',{"post":mi_post,"mensajes":mensaje},context)
    
	

