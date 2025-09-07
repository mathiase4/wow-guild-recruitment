from django.contrib import admin
from .models import Guild, Application

# Register your models here.
@admin.register(Guild)

class GuildAdmin(admin.ModelAdmin):
    """List key fields and make slug auto-fill from name."""
    
    list_display = ("name", "faction", "region", "realm", "published",)
    list_filter = ("faction", "published", "region")
    search_fields = ("name", "realm", "region")
    prepopulated_fields = {"slug": ("name",)} #auto-fill slug from name
    

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """ Quick overview of incoming applications."""
    list_display = ("character_name", "class_spec", "guild", "created_on")
    search_fields = ("character_name", "class_spec", "guild_name")    