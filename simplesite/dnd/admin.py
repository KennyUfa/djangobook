from django.contrib import admin
from .models import DndSpell,Character
# link,name,lvl,school,Время накладывания,Дистанция,Компоненты,Длительность,Классы,Архетипы,Источник,Описание


class DndAdmin(admin.ModelAdmin):
    list_display = ("name", "lvl")
    list_display_links = ("name", "lvl")
    search_fields = ("name", "lvl")
# class CharacterAdmin(admin.ModelAdmin):
#     list_display = ("account")
#     list_display_links = ("account")
#     search_fields = ("account")

admin.site.register(DndSpell,DndAdmin)
admin.site.register(Character)