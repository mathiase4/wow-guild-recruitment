""" Simple forms for the guilds app."""
from django import forms
from .models import Application, Guild

class ApplicationForm(forms.ModelForm):
    """form to apply to a guild.
    
    """
    class Meta:
        model = Application
        fields = ("character_name", "class_spec", "discord", "message")
        
        
        
        
class GuildForm(forms.ModelForm):
    """ Form based on the Guild model, for users to create and edit their guild ads."""
    class Meta:
        model = Guild
        #List the fields a user can fill out
        fields = [ 'name', 'faction', 'region', 'realm', 'description']
        
        

