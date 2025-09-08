from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Guild
from .forms import ApplicationForm, GuildForm
from django.contrib.auth.decorators import login_required # what user is logged in
#create your views here

def guild_list(request):
    """Public list of published guilds, wth a simple text search."""
    q = request.GET.get("q","").strip()
    guilds = Guild.objects.filter(published=True)
    if q:
        guilds = guilds.filter(name_icontains=q)
    context = {"guilds": guilds, "q": q}
    return render(request, "guilds/guild_list.html", context)


def guild_detail(request, slug):
    """Show details for one published guild by slug, or 404 if not found."""
    guild = get_object_or_404(Guild, slug=slug, published=True)
    return render(request, "guilds/guild_detail.html", {"guild": guild})

def application_create(request, guild_id):
    """Create a simple application for a specific guild.
    save, show a message, then redirect back to the guild detail."""
    
    guild = get_object_or_404(Guild, id=guild_id, published=True)
    
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False) 
            app.guild = guild
            app.save()
            messages.success(request, "Thanks! Your application was sent.")
            return redirect("guild_detail", slug=guild.slug)
        else:
            form = ApplicationForm()
            
        return render(request, "guilds/application_form.html", {"form": form, "guild": guild})
    
    @login_required
    def guild_create(request):
        """ Renders the form to create a new guild
        and handles the form submission by a logged-in user.
        """
        if request.method == "POST":
            form = GuildForm(request.POST)
            if form.is_valid():
                guild = form.save(commit=False)
                guild.owner = request.user
                guild.save()
                
                messages.success(request, "Your guild ad was created successfully!")
                return redirect('guild_detail', slug=guild.slug)
            else:
                form = GuildForm()
                
            context = {
                "form": form
            }
            return render(request, "guilds/guild_form.html", context)
            
