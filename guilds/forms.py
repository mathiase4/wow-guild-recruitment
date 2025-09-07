""" Simple forms for the guilds app."""
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    """form to apply to a guild.
    
    """
    class Meta:
        model = Application
        fields = ("character_name", "class_spec", "discord", "message")