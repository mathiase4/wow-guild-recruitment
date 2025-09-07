from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Guild
from .forms import ApplicationForm

def guild_list(request):
    """Public list of published guilds, wth a simple text search."""
    q = request.GET.get("q","").strip()
    guilds = Guild.objects.filter(published=True)
    if q:
        guilds = guilds.filter(name_icontains=q)
    context = {"guilds": guilds, "q": q}
    return render(request, "guilds/guild_list.html", context)

# Create your views here.
