from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rango.models import Bar, Tapas
from rango.forms import BarForm, TapaForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tango_with_django_project import settings





# Create your views here.

def index(request):
    bar_list =  Bar.objects.order_by('-numero_visitas')
    context_dict = {'bares':bar_list,}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    bar_list =  Bar.objects.order_by('-numero_visitas')
    context_dict = {'bares':bar_list,}
    return render(request, 'rango/about.html', context_dict)

def bares(request, bar_name_slug):
    context_dict = {}

    try:
        b = Bar.objects.get(slug=bar_name_slug)
        context_dict['bar_direccion'] = b.direccion
        context_dict['bar_nombre'] = b.nombre
        b.numero_visitas += 1
        b.save()
        tapa = Tapas.objects.filter(bar = b)
        context_dict['tapa'] = tapa
        context_dict['bar'] = b

        bar_list =  Bar.objects.order_by('-numero_visitas')
        context_dict['bares'] = bar_list


    except Bar.DoesNotExist:
        pass

    return render(request, 'rango/bares.html', context_dict)
def tapas(request,bar_name_slug, tapas_name_slug):
    context_dict = {}

    try:
        t = Tapas.objects.get(slug = tapas_name_slug, bar=Bar.objects.get(slug=bar_name_slug))
        bar_tapa = t.bar.nombre
        t.votos += 1
        t.save()
        context_dict['bar'] = bar_tapa
        context_dict['tapas'] = Tapas.objects.filter(bar = t.bar)
        context_dict['tapa_image'] = t.picture
        context_dict['tapa'] = t.nombre
        context_dict['votos_tapa'] = t.votos
        context_dict['b'] = t.bar
        context_dict['MEDIA_URL'] = settings.MEDIA_URL
    except Tapas.DoesNotExist:
        pass

    return render(request, 'rango/tapas.html', context_dict)
def add_bar(request):
    if request.method == "POST":
        form = BarForm(request.POST)

        if form.is_valid():
            form.save(commit = True)

            return index(request)

        else:
            print form.errors
    else:
        form = BarForm()

    bar_list =  Bar.objects.order_by('-numero_visitas')
    return render(request, 'rango/add_bar.html', {'form':form, 'bares':bar_list} )

@login_required
def add_tapa(request, bar_name_slug):
    try:
        bar = Bar.objects.get(slug=bar_name_slug)
    except Bar.DoesNotExist:
        bar = None

    if request.method == "POST":
        form = TapaForm(data=request.POST)
        if form.is_valid():
            if bar:
                t = form.save(commit=False)
                t.bar = bar
                t.votos = 0
                print '**************************************************************'
                if 'picture' in request.FILES:
                    print '**************************************************************'
                    t.picture = request.FILES['picture']
                t.save()

                return bares(request, bar_name_slug)
        else:
            print form.errors
    else:
        form = TapaForm()

    bar_list =  Bar.objects.order_by('-numero_visitas')
    context_dict = {'form':form, 'bar':bar, 'bar_name_slug':bar.slug}
    context_dict['bares'] = bar_list
    return render(request, 'rango/add_tapa.html', context_dict )


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form=UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form':profile_form, 'registered':registered}
    bar_list =  Bar.objects.order_by('-numero_visitas')
    context_dict['bares'] = bar_list
    return render(request, 'rango/register.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Tu cuenta esta deshabilitada")
        else:
            print "Login incorrecto: {0}, {1}".format(username, password)
            return HttpResponse("Usuario o contrasenia incorrectas<br><a href='/rango/login/'>Login</a>")

    else:
        context_dict = {}
        bar_list =  Bar.objects.order_by('-numero_visitas')
        context_dict['bares'] = bar_list
        return render(request, 'rango/login.html', context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')

@login_required
def add_votos(request, bar_name_slug, tapas_name_slug):
    tapa = Tapas.objects.get(slug = tapas_name_slug)
    tapa.votos = tapa.votos + 1
    return HttpResponseRedirect('/rango/bar/'+tapa.bar.slug +'/tapas/'+tapa.slug+'/')

def track_url(request):
    page_id = None
    url = '/rango/'
    if request.method == 'POST':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.numero_visitas = page.numero_visitas + 1
                page.save()
                url = page.url
            except:
                pass
    return redirect(url)

def reclama_datos(request):
    datos = ()
    visitas = []
    lista_bares = []
    bares =  Bar.objects.order_by('-numero_visitas')
    for b in bares:
        lista_bares.append(b.nombre)
        visitas.append(b.numero_visitas)

    datos = lista_bares, visitas
    return JsonResponse(datos, safe=False)
