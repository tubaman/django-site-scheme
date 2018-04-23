from django.contrib import admin
from django.contrib import sites

from .models import SiteScheme


class SiteSchemeInline(admin.TabularInline):
    model = SiteScheme


class SiteAdmin(sites.admin.SiteAdmin):
    inlines = [SiteSchemeInline]
    list_display = ['domain', 'name', 'get_scheme']

    def get_scheme(self, obj):
        try:
            return obj.sitescheme.scheme
        except SiteScheme.DoesNotExist:
            return SiteScheme._meta.get_field('scheme').get_default()
    get_scheme.short_description = 'Scheme'

admin.site.unregister(sites.models.Site)
admin.site.register(sites.models.Site, SiteAdmin)
