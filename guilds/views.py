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
    """
    Renders the form to create a new guild
    and handles the form submission by a logged-in user.
    """
    if request.method == "POST":
        # This block runs only when the user submits the form
        form = GuildForm(request.POST)
        if form.is_valid():
            guild = form.save(commit=False)
            guild.owner = request.user
            guild.save()
            guild.refresh_from_db()
            
            messages.success(request, "Your guild ad was created successfully!")
            return redirect('guild_detail', slug=guild.slug)
    else:
        # This block runs when user just visits the page 
        form = GuildForm()
        
    
    # It run for GET requests, or if a POST form is invalid.
    context = {
        "form": form,
        "guild": None
    }
    return render(request, "guilds/guild_form.html", context)
            
            

@login_required
def guild_edit(request, slug):
    """
    Fetches a guild ad by slug for editing, validates that the logged-in user is the owner,
    and fix the form submission.

    """
    
    # the security check if the logged-in user is the owner
    if guild.owner != request.user:
        messages.error(request, "You are not authorized to edit this ad.")
        return redirect('guild_list')
    
    #similar to the create view
    
    if request.method == "POST":
        # this populates the form with submitted data
        form = GuildForm(request.POST, instance=guild)
        if form.is_valid():
            form.save()
            messages.success(request, "Your guild ad has been updated successfully!")
            return redirect('guild_detail', slug=guild.slug)
    else:
        #prefill the form with the guilds data
        form = GuildForm(instance=guild)
        
    context = {
        "form": form,
        "guild": guild
    }
    return render(request, "guilds/guild_form.html", context)
