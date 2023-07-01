from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .forms import VehiculoForm, RegistroUsuarioForm
from .models import VehiculoModel

def indexview(request):
    template_name = 'index.html'
    return render(request, template_name)

@login_required(login_url='login')
@permission_required("vehiculo.visualizar_catalogo", raise_exception=True)
def listvehiculo(request):
    vehiculos = VehiculoModel.objects.all()
    return render(request, 'listvehiculo.html', {'listvehiculo': vehiculos})

def addvehiculo(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'El formulario se ha enviado correctamente!')

    return render(request, "addvehiculo.html", {'form': form})

def editvehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoModel, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listvehiculo')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'editvehiculo.html', {'form': form, 'vehiculo': vehiculo})

def deletevehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoModel, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('listvehiculo')
    return render(request, 'deletevehiculo.html', {'vehiculo': vehiculo})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                next_url = request.GET.get('next', '/')
                return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Usuario o contraseña inválidos.")
    else:
        form = AuthenticationForm()

    return render(request=request, template_name="login.html", context={"login_form":form})
    
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type)
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()
    
    return render(request=request, template_name="registro.html", context={"register_form": form})

def error_403_view(request, exception):
    return render(request, '403.html', status=403)
