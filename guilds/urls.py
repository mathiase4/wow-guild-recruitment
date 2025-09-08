""" URL routes for the guilds app."""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.guild_list, name="guild_list"),
    path("guilds/", views.guild_list, name="guild_list_alt"),   # list page
    path("create/", views.guild_create, name="guild_create"),
    path("guilds/<slug:slug>/", views.guild_detail, name="guild_detail"), # detail page
    path("apply/<int:guild_id>/", views.application_create, name="application_create") # apply form
    
    
]