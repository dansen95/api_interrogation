from django.contrib import admin

from .models import Interrogation


class InterrogationAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title',
                    'date_start',
                    'date_end',
                    'user',
                    'description')
    search_fields = ('text',)
    list_filter = ('date_start',)
    empty_value_display = '-пусто-'


admin.site.register(Interrogation, InterrogationAdmin)
