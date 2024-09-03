from django.contrib import admin
from .models import Membre, Livre, Cd, Dvd, JeuxDePlateau


@admin.register(Membre)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Livre)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Cd)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Dvd)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(JeuxDePlateau)
class AuthorAdmin(admin.ModelAdmin):
    pass


