# WoW Guild Recruitment

A full-stack application for World Of Warcraft ("Video Game") players to find and recruit for guilds.
**This is Portfolio Project 3**

![Responsive Mockup of the WoW Guild Recruitment site](docs/screenshots/screenshot.mockup.png)

## Introduction

World of Warcraft is a social game where players join guilds to play together.
This project is a recruitment site where guild leaders can create ads and players can apply.
The goal is to make it faster and easier to connect the right players with the right guilds.

For many years, World of Warcraft players have said it is hard to find active people to play with.
The game feels less social when guild recruitment is spread across forums, chats, and other websites.

This project was built to fix that problem.
With this site, players can quickly find a guild that fits them, and guild leaders can easily reach new members.
In the future, more features will be added to make recruitment even better, solving many of the issues players 
have talked about for years.


## User Stories

### As a Visitor (Not Logged In)

**US1: View a list of guilds**
> **User Story:** As a visitor, I want to see a list of guilds so I can find options.

**Acceptance Criteria:**
- I can see the guild name, faction, and realm on each card in the list.
- I can click a "Details" button on a card to be taken to that specific guild's page.

**US2: View a guild's detail page**
> **User Story:** As a visitor, I want to open a guild page to read the full details.

**Acceptance Criteria:**
- I can see the guild's detailed description and other information.
- I can see an "Apply" button to start an application.

**US3: Apply to a guild**
> **User Story:** As a visitor, I want to click “Apply” so I can contact the guild easily.

**Acceptance Criteria:**
- I am presented with a simple form to fill out (character name, class/spec, discord, message).
- After submitting the form, I see a success message and am redirected back to the guild's detail page.


**US5: Create an Account or Log In**
> **User Story:** As a visitor, I want to be able to register for an account to create my own ads, or log in if I already have one.

**Acceptance Criteria:**
- I can easily find "Sign Up" and "Log In" links in the navigation bar.
- The registration form allows me to create a new account, which then logs me in.
- The login form allows me to sign in with my existing credentials.

---
### As a Registered User (Logged In)

**US6: Create a Guild Ad**
> **User Story:** As a logged-in user, I want to be able to create a new guild ad.

**Acceptance Criteria:**
- I can find and access a "Create Guild" page.
- After submitting the form, a new guild ad is created and I am listed as the owner.
- I am redirected to the detail page for my new guild ad.

**US7: Edit a Guild Ad**
> **User Story:** As an ad owner, I want to be able to edit the ads that I own.

**Acceptance Criteria:**
- On the detail page of a guild I own, I can see an "Edit" button.
- The edit page shows a form pre-filled with the current guild information.
- When I save the form, the guild's details are updated.

**US8: Delete a Guild Ad**
> **User Story:** As an ad owner, I want to be able to delete the ads that I own.

**Acceptance Criteria:**
- On the detail page of a guild I own, I can see a "Delete" button.
- I am asked to confirm before the ad is permanently deleted.
- Once deleted, the ad no longer appears on the site.

**US9: Upload an Image**
> [cite_start]**User Story:** As an ad owner, I want to be able to upload an image for my guild ad. [cite: 1]

**Acceptance Criteria:**
- The create/edit form has a field for uploading an image file.
- The uploaded image is shown on the guild's card and detail page.

**US10: Log Out**
> **User Story:** As a logged-in user, I want to be able to log out of my account.

**Acceptance Criteria:**
- I can see a "Log Out" link in the navigation bar.
- Clicking the link ends my session and updates the navigation bar to show "Sign Up" and "Log In" again.

---
### As a Site Administrator

**US11: Manage Content via Django Admin**
> **User Story:** As an administrator, I want to manage all guilds and user content in the admin panel.

**Acceptance Criteria:**
- I can log in to the Django Admin area with superuser credentials.
- I can create, view, update, and delete any guild or application from the admin panel.

**US12: Publish/Unpublish a Guild**
> **User Story:** As an administrator, I want to publish or unpublish a guild to control its visibility.

**Acceptance Criteria:**
- When a guild is marked as "published", it appears in the public list on the website.
- When a guild is marked as "unpublished", it is hidden from the public list.

---
### Security & Deployment

**US13: Secure Ad Management**
> **User Story:** As a user, I want to be sure that I cannot edit or delete ads that I do not own.

**Acceptance Criteria:**
- The "Edit" and "Delete" buttons are not visible on ads owned by other users.
- Attempting to go directly to the edit/delete URL for another user's ad results in an error.

**US14: Site Deployment**
> **User Story:** As the site owner, I want the application to be deployed and live on Heroku.

**Acceptance Criteria:**
- The site is live and accessible at its public Heroku URL.
- The live site uses a PostgreSQL database and serves media/static files correctly.


## Features

### User Accounts (powered by django-allauth)
- **Secure User Registration:** Users can create a personal account with a unique username, email, and password. This allows them to create and manage their own guild ads.
- **User Login and Logout:** Registered users can log in to access member-only features and log out securely. The navigation bar updates to reflect the user's logged-in status.
- **Password Reset:** Users who have forgotten their password can request a reset link via email, providing a secure way to regain access to their account.

### Guild Management (CRUD)
- **Create Guild Ad:** Logged-in users can create new guild advertisements through a simple and intuitive form.
- **Read Guilds:** All visitors can browse a list of all published guilds on the homepage. They can click on any guild to view a detailed page with more information.
- **Update Guild Ad:** Users can easily edit the information on the guild ads that they are the owner of.
- **Delete Guild Ad:** Users can permanently delete their own guild ads after a confirmation prompt to prevent accidental deletions.

### Interactivity & User Experience
- **Image Uploads:** Users can upload a custom image for their guild ad, which is hosted externally on Cloudinary.
- **Apply to Guild:** A simple application form allows players to easily send their information (character name, message, etc.) to a guild they are interested in.
- **User Feedback:** Clear success messages are shown to the user after performing important actions, such as creating an ad or sending an application.
- **Responsive Design:** The site is fully functional and visually appealing on all devices, from mobile phones to large desktops, ensuring a consistent user experience.

### Site Administration
- **Full Admin Control:** The site owner has full administrative control over all user-generated content (guilds, applications) via the built-in Django Admin panel.
- **Publish / Unpublish Content:** The site admin can toggle the visibility of any guild ad, allowing for content moderation.



## Data Schema

For this project, I created a database with two main tables to store all the information: one for the guilds and one for the applications.

### The Guild Model
This table holds all the information for a single guild advertisement.

| Field Name    | Field Type        | Description                                  |
|---------------|-------------------|----------------------------------------------|
| `name`        |  `CharField`       | The name of the guild.                       |
| `slug`        | `SlugField`       | A URL-friendly version of the name.          |
| `faction`     | `CharField`       | The guild's faction (Alliance or Horde).     |
| `region`      | `CharField`       | The server region (e.g., EU, US).            |
| `realm`       | `CharField`       | The name of the server.                      |
| `description` | `TextField`       | A longer description of the guild.           |
| `image`       | `ImageField`      | The image that the user uploads.             |
| `published`   | `BooleanField`    | Decides if the ad is visible or not.         |
| `owner`       | `ForeignKey(User)`| Connects the ad to the user who created it.  |
| `created_on`  | `DateTimeField`   | Automatically stores when the ad was made.   |
| `updated_on`  | `DateTimeField`   | Automatically stores when the ad was last edited. |

### The Application Model
This table holds the information for a player's application to a specific guild. It is connected to the Guild model, so each application knows which guild it belongs to.

| Field Name       | Field Type         | Description                                     |
|------------------|--------------------|-------------------------------------------------|
| `guild`          | `ForeignKey(Guild)`| Connects the application to a specific guild.   |
| `character_name` | `CharField`        | The applicant's character name.                 |
| `class_spec`     | `CharField`        | The applicant's class and spec.                 |
| `discord`        | `CharField`        | The applicant's Discord username.               |
| `message`        | `TextField`        | The message the applicant wrote to the guild.   |
| `created_on`     | `DateTimeField`    | Automatically stores when the application was sent. |























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
