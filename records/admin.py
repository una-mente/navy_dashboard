from django.contrib import admin
from .models import Piracy, IUU, DrugTrafficking, ShipToShip, StowAway, MaritimeAccidents


admin.site.register([Piracy, IUU, DrugTrafficking, ShipToShip, StowAway, MaritimeAccidents])
