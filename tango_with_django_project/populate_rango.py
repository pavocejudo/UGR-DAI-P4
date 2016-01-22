import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

from rango.models import Bar, Tapas

def add_bar(name, direc, n_visitas=0):
    b = Bar.objects.get_or_create(nombre = name)[0]
    b.direccion = direc
    b.numero_visitas = n_visitas
    b.save()
    return b

def add_tapa(bar_procedente, nombre_tapa, puntuacion=0):
    t = Tapas.objects.get_or_create(bar=bar_procedente, nombre=nombre_tapa)[0]
    t.votos = puntuacion
    t.save()
    return t

def populate():
    #Adding Bars
    almendro_bar = add_bar(name='Almendro', direc='C/ Espania')
    conchita_bar = add_bar('Conchita', 'C/ Manzanares')

    #Adding Tapas
    add_tapa(almendro_bar, 'kikos')
    add_tapa(almendro_bar, 'Tortilla de patatas')
    add_tapa(almendro_bar, 'hamburguesas')
    add_tapa(almendro_bar, 'nachos')
    
    add_tapa(conchita_bar, 'bocadillo de lomo')
    add_tapa(conchita_bar, 'montaditos')
    add_tapa(conchita_bar, 'calamares fritos')
    add_tapa(conchita_bar, 'fajita vegetal')

    for b in Bar.objects.all():
        print "-"+str(b)
        for t in Tapas.objects.filter(bar = b):
            print "{0}".format(str(t))
        print "\n"


if __name__ == '__main__':
    print "starting Rango Application script..."
    populate()
