from django.contrib import admin
from .models import PlayerCoordinates

admin.site.register(PlayerCoordinates)

class PlayerCoordinatesAdmin(admin.ModelAdmin):
    list_display = ('x', 'y')

