from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

FACTIONS = (
    ("ALLIANCE", "Alliance"),
    ("HORDE", 'Horde'),
)

class Guild(models.Model):
    """A WoW guild visible on the public list.
    Keep fields simple for MVP. "Published" controls visibility.
    """
    name = models.CharField(max_length=120, unique=True)
    # guild display name
    slug = models.SlugField(max_length=140, unique=True)
    faction = models.CharField(max_length=9, choices=FACTIONS) #Ally or Horde
    
    
    region = models.CharField(max_length=40, blank=True)   # EU OR US
    realm = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    #show/hide in public list
    owner = models.ForeignKey(User , on_delete=models.SET_NULL, null=True,
                              blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]  #newest first on the list
        
    def __str__(self) -> str:
        """Show a friendly name in admin, logs and shells.""" 
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Auto-generate a slug from the guild name if one doesn't exist.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)
    
    # Application model
    
class Application(models.Model):
        """A player's application for a specific guild."""
        guild = models.ForeignKey("Guild", on_delete=models.CASCADE,
                                  related_name="applications")
        character_name = models.CharField(max_length=80)
        class_spec = models.CharField(max_length=80)
        discord = models.CharField(max_length=80, help_text="Example: CoolName#1234",
                                   blank=True)
        message = models.TextField(blank=True)
        created_on = models.DateTimeField(auto_now_add=True)
        
        def __str__(self) -> str:
            """ Help admins see who applied to which guild."""
            return f"{self.character_name} {self.guild.name}"
        
           
