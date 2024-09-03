from django.shortcuts import render

from application_bibliothecaire.models import Membre,Livre,Cd,Dvd,JeuxDePlateau

def listeMembre(request):
    membres = Membre.objects.all()
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    jdps = JeuxDePlateau.objects.all()

    return render(request, 'application/application_bibliothecaire.html',
                  { 'livres': livres, 'membres': membres , 'cds': cds , 'dvds': dvds , 'jdps': jdps ,  } )


