from django.contrib import admin
from .models import Piracy, IUU, DrugTrafficking, ShipToShip, IllegalMigrations, MaritimeAccidents


admin.site.register([Piracy, IUU, DrugTrafficking, ShipToShip, IllegalMigrations, MaritimeAccidents])
