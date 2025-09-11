# WoW Guild Recruitment

A full-stack application for World Of Warcraft ("Video Game") players to find and recruit for guilds.
**This is Portfolio Project 3**

![Responsive Mockup of the WoW Guild Recruitment site](screenshots.mockup.png)






























============================================================
## Purpose and Value
Simple guild recruitment board for World of Warcraft. Users can post guild ads with guild name, role and realm.

## User Stories
- As a visitor, I can see a list of guild ads so I can find active guilds.
- As a logged-in user, I can create a guild ad (guild name, role, realm) so I can recruit players.
- As the ad owner, I can edit my ad so I can correct details without creating a new one.
- As the ad owner, I can delete my ad so I can remove outdated posts.
- As a user, I can log in/out so I can manage my ads.

  ## Wireframes
  (Will be added in /docs/wireframes)

  ## Tech
  Python 3.9.2,
  Django 4.2,
  Bootstrap,
  Allauth,
  Postgres (prod

  ## Deployment

  (Will add Heroku steps later)
  
## What i have done today -07
- Created app 'guilds' and added to installed_apps
- added templates folder and base layout
- added guild and application models; ran migrations
- registered models in admin and added test data
-implemented list, detail, and apllly flow
- added simple search (q=).



## Setup & Settings

Added crispy_forms and crispy_bootstrap5 to INSTALLED_APPS.

Set TEMPLATES_DIR = BASE_DIR / "templates" and pointed TEMPLATES['DIRS'] to it.

Enabled WhiteNoise static storage: STORAGES['staticfiles'] = CompressedManifestStaticFilesStorage.

Kept local DEBUG = True. For production I will use a separate prod branch where DEBUG = False.

Added STATIC_ROOT, STATICFILES_DIRS, and created static/css/style.css.

## URLs

Project urls include the app: path("", include("guilds.urls")).

App urls now include a root route ("") so / shows the guild list.

Kept clean order: specific paths first, slug route last.

## Templates

Fixed template lookup by moving base.html to templates/base.html.

base.html loads Bootstrap and {% load static %}.

guild_list.html shows a search box and loops over guilds.

guild_detail.html shows guild data and an Apply button.

application_form.html uses {% load crispy_forms_tags %} and {{ form|crispy }}.

## Forms & Views

Added ApplicationForm (fields: character_name, class_spec, discord, message).

application_create view saves an application and shows a success message.

Staff-only CRUD for applications:

application_edit (update).

application_delete (confirm + delete).

Fixed search bug in list view (name__icontains and simple Q filter).

## Static files

Created static/css/style.css and linked it in base.html.

## Git (micro commits)

feat: add ApplicationForm and connect create view

fix: move base.html to templates/

feat: show search + loop on guild list

feat: staff-only application edit/delete

chore: settings cleanup (templates dir, whitenoise, static)

docs: add simple docstrings

## Why I did these changes

Root route: Avoid 404 should show content.

base.html in templates/: Template inheritance works everywhere.

Crispy + Bootstrap: Clean forms and responsive UI.

Staff-only CRUD for Applications: Meets P3 CRUD requirement and access control.

WhiteNoise + static config: Required for Heroku static files.

## Features

The site is a full CRUD (Create, Read, Update, Delete) application that allows users to manage guild recruitment ads for World of Warcraft. It also includes an application feature for Game-loving interested players.

### Existing Features
* **Read:** Any visitor can see a list of all published guild ads and view the details for each one.
* **Create:** A logged-in user can create a new guild ad. The ad is automatically assigned to them as the owner.
* **Update:** The owner of a guild ad can edit its details. Access is restricted so users cannot edit ads they do not own.
* **Delete:** The ad owner can delete their ad. This action requires a confirmation step to prevent accidental deletion. Access is restricted to the ad owner.
* **Apply:** Any visitor can apply to a guild via a simple form on the guild's detail page.
* **Admin Management:** The site administrator can manage all aspects of guilds via the Django Admin panel.
