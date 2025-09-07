""" URL routes for the guilds app."""
from django.urls import path
from . import views

urlpatterns = [
    path("guilds/", views.guild_list, name="guild_list"),   # list page
    path("guilds/<slug:slug>/", views.guild_detail, name="guild_detail"), # detail page
    path("apply/<int:guild_id>/", views.application_create, name="application_create") # apply form
    
    
]