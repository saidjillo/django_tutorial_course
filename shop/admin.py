from django.contrib import admin

from shop.models import Game , Player, Developer

# Register your models here.
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Developer)
# admin.site.register(Transaction)
