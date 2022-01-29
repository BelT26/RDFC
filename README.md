# Reigate Dads FC

https://reigate-dads.herokuapp.com/

## Author: Helen Taylor  
## Version 1.0.0

![site preview on a variety of devices]()


## Contents
* [Overview](#overview)
* [Planning](#planning)
    * [Project Conception Meeting](#project-conception-meeting)
    * [Project Review](#project-review-meeting)
    * [User Stories](#user-stories)
* [Models](#models)
    * [ClubMember](#clubmember)
    * [Match](#match)
    * [MatchPlayer](#matchplayer)
* [Features](#features)
    * [User Authentication](#user-authentication)
    * [Messages](#messages)
    * [Navigation](#navigation)
    * [Footer](#footer)
    * [Home Page](#home)
        * [About](#about)
        * [Social](#social)
        * [Contact](#contact)
    * [Member Zone](#member-zone)
        * [Next Fixture](#fixture)
        * [League Table](#league-table)
        * [Past Results](#past-results)
        * [Match Registration](#match-registration)
    * [Manager Zone](#manager-zone)
        * [Add Fixture](#add-fixture)
        * [Match Admin](#match-admin)
            * [Edit Match](#edit-match)
            * [Delete Match](#delete-match)
            * [Flag Next Fixture](#flag-next-fixture)
            * [Open Registrations](#open-registrations)
            * [Allocate Teams](#allocate-teams)
            * [Add Scores](#add-scores)
            * [View Players](#view-players)
        * [Member Admin](#member-admin)
    * [404 Page](#404-page)     
* [Bugs and challenges](#bugs-and-challenges)
* [Testing](#testing)
    * [Automated Tests](#automated-tests)
    * [Manual Tests](#manual-tests)
* [Deployment](#deployment)
* [Credits](#credits)
* [Future Development Opportunities](#future-development-possibilities)

## Overview

The project was created following a request from a friend of mine called Steve, who is the manager of an amateur football club. He was finding it time consuming to manually manage match place bookings, allocate teams and keep all players updated of their position in the club's player league table.

The club plays a six a side match every week so 12 players can register for each game.  To make the teams evenly balanced before they are allocated the players are sorted according to their scores from their previous matches.  Each time they are part of the winning team they earn 3 points and if the teams draw all players are allocated 1 point. If 2 players have the same number of points they are then sorted according to the number of matches they have played with members who have played fewer games ranking more highly.


## Planning

### Project Conception Meeting
Before starting work on the project I met with the club manager to ascertain his requirements for the site.  Essential features that he requested were:
* A home page with information about the club
* A booking facility for club members to reserve their place in the next match
* A login facility so that approved members can access match information and the match booking form.
* A function that would allocate teams based on the members' current points and number of matches played
* A league table displaying all players' results
* A sign up facility so that new members can apply to join the club 

Optional features that were discussed were:
* A page displaying details of the next fixture and the names of the players in each team
* A table containing the results of past games
* A page on which the manager could upload match reports and other members could comment
* A page dedicated to upcoming social events

### Project Review Meeting
Once the project was near completion I scheduled another meeting with the club manager to review the progress of the site. Steve was happy to leave the pages for the match reports and social events to a later date, but requested that I add a page in which he could view which members had registered for the upcoming match and also a facility whereby players could be placed on a reserve list if all of the team places were already taken. This would allow him to reassign the place to an available member if somebody cancelled. I suggested adding an email alert so that Steve would be advised if a team member cancels and would know to reallocate the teams.

The extra features requested have been implemented in the project.

### User Stories
After receiving the initial project brief I created a project with the Kanban template on Github and added user stories. 
Following my first meeting with the club manager the list of stories was extended. They were arranged into epics as shown in the excel table below and allocated a priority rating of between 1 and 3 with priority 1 being the most important. I found it easier visually to prioritise my work using the excel spreadsheet rather than the project board in Github and so it became my main tool for the project planning.

![Epics and User Stories](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/user_stories.jpg)

When approaching an epic I would focus first on the user stories with priority 1 and break them  down into tasks as in the example below. 

![Example of user story tasks](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/tasks.jpg)

Once I had completed the user stories with the highest priority I would assess how simple and time consuming it would be to complete the tasks with a lower rating.  If they were quick and easy to implement I would complete them before moving on. Otherwise I would leave them for a future sprint.

### Wireframes
The original wireframes that I first presented to the club manager are included below.  The finished project does not bear a great deal of resemblance to the initial plan, apart from the layout of the home page. I found that as I talked to the client, progressed with my learning and implemented certain features, that the needs of the site gradually grew.

The member zone page was becoming crowded and so I separated all the features into their own pages which are accessible through the dropdown menu for the member zone in the navbar.

Rather than create a sign up form I installed Allauth to handle user authentication.

I originally intended to use the admin panel for management functions but after discussions with the club manager, it became apparent that it would be necessary to create a management section to implement the required functionality.

![Home Page Wireframe](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/wireframe-home.jpg)

![Member Zone Wireframe](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/wireframe-members.jpg)

![Sign Up Wireframe](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/wireframe-signup.jpg)


## Models
I used three models to create this project, ClubMember, Match and MatchPlayer

### ClubMember
The ClubMember model is a custom user model that inherits from the Django user model. Each time a user completes a sign up form a new instance is created.

### Match
The Match model is used to create an instance of each game. The add match function in the manager zone enables the manager to create new matches. The details are used to populate the Next Fixture and Past Results pages and the manager is able to manage the properties of each Match within the Match Admin table. 

### MatchPlayer
Each time a ClubMember registers for a Match an instance of the MatchPlayer field is created.  The MatchPlayer model has two foreign keys: the match_id that is based on the Match model and the player_id that is based on the ClubMember model.
The results of each game are stored on the MatchPlayer model and these are used to dynamically generate the scores for the player league table.

## Admin
When setting up the project I customised the admin display, filter and search fields for the ClubMembers and MatchPlayers and added an 'approve member' function.  It is not now expected that most of these will usually be used by the manager as I have since created views on the main site for the manager to approve membership applications, see which members are available and view their contact details.

## Features

## User Authentication
Django Allauth was installed to enable users to sign up, log in and log out.  I customised the standard Allauth model  
so that users also need to enter their first and last name when signing up.  I copied the Allauth templates into a separate folder and used my own base.html file to extend them.  I also created a custom container for them so that they took up all the space on the screen that was not occupied by the header or footer.

![Sign Up Form](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/signup.jpg)

## Messages
Feedback on user interaction is provided via Django messages.  Bootstrap classes have been applied to convey success or error messages.  The code to install and customise the messages was taken from the 'I think therefore I blog' walkthrough project. To improve the user experience, the messages automatically disappear after several seconds without the user needing to manually dismiss them.

## Navigation
I created a responsive navbar that collapses on mobile devices using Bootstrap classes. To make the site as user friendly as possible, I felt it was important to keep the Navbar as simple as possible and only show items that are relevant to the user. The items displayed on the navbar change according to whether the user is logged in or not and whether they are the club manager as detailed below:

### General User Access
Visitors to the site can view general information about the club.  They also have the option of signing up to the club or logging in if they are a member.

![Site User Navbar](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/navbar-user.jpg)

### Member Access
Once a user has logged in, their logged in status is displayed on the right of the navbar. Logged in users have access to the member zone in which they can book a place in the next match, view details of the next fixture, view past results and view the player league table. The signup option disappears and the login option is replaced with a logout option.

![Member Navbar](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/navbar-member.jpg)

### Manager Access
As well as all of the member facilities, the manager has access to a dropdown management menu.  This offers options for him to add a new match fixture, update details of the existing matches and approve and remove members.

![Manager Navbar](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/navbar-manager.jpg)

## Footer
The footer contains social media links to Facebook, Twitter and Instagram. The icons change from white to gold when the user hovers over them to indicate to the user that they are links. The club manager has not yet set up accounts with these sites so the links currently take the user to the home page. These links will be updated once the club's accounts have been created.

![Footer](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/footer.jpg)

## Home Page
The home page is split into three sections, accessible by a dropdown menu, a general introduction to the club, a social section and a contact section including a Google map showing where the team play. The links to each of the sections were created using template tags.

### About
The text provides a lighthearted introduction to the club for potential new members and was provided by Steve, the club manager. The main image is replaced with a cropped version on mobile devices.

![Club Intro](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/homepage.jpg)

### Social
This section lets potential members know that the players like to socialialise together after the game. Eventually it will be moved to its own page and the manager will be able to add details of upcoming events.

![Social](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/social.jpg)

### Contact
I used the Bootstrap Resume walkthrough project as a guide to creating the JavaScript code to link to the Google Maps API.  At the moment only one location is marked as the club both play and socialise at the South Park grounds.  I decided to still use marker clusters as the club manager mentioned to me that he may like to add other venues to the map in the future.

The contact details allow the users to get in touch with any queries. The email address opens up a link to the user's email account with a prepopulated 'to' field.

![Contact](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/map.jpg)

## Member Zone

### Next Fixture
The next fixture page shows members the details of the next match.  If no match has been flagged by the manager as the next fixture then the most recent match in the database is displayed.

Members can see whether the booking system is currently open for the match displayed.  If it is, a link is shown which takes them to the match booking form.

Once the manager has allocated the teams for the match, the player names and a list of the reserves are displayed.

![Next Fixture](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/next_fixture.jpg)

### League Table
The league table sorts the players by the number of points they have scored and then by the number of matches they have played. When two or more players have the same number of points the player who has played the fewer matches ranks more highly.
To enable the member to locate their place in the table more easily a highlighted class is applied to the details of the logged in user.

![League Table](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/league.jpg)

### Past Results
The past results page shows the scores of any previous matches so that members can find out about any games they missed.  The members of each teams are also listed on larger devices but not on mobiles.

![Results Table](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/results.jpg)

### Match Booking Form
If match registrations are open a booking form is displayed. Otherwise users see a message informing them that registrations are currently closed. In the booking form users can see the date of the match.  

12 members can register for a match once this number has been reached the user is informed that the match is full but they are still able to book a place on the reserve list.  If they do decide to be a reserve a message shows them their place on the list when they submit the form.

If a member has already registered for the match rather than being shown the 'book match place' button they are given the option to cancel their place. If teams have already been allocated by the manager and the member has a place on the team, an email is generated to the manager to inform them that a player has cancelled and that they need to reselect the teams.

![Match Booking Form](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/book_match.jpg)

## Manager Zone

### Add Fixture
The Manager is able use this form to create a new match and add the date, time and locations. A datepicker has been used on the datefield to enable the user to enter the date more easily. Once the form is submitted an new instance of the Match model is created.

![Add Match Form](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/add_match.jpg)

### Match Admin

![Match Admin Table](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/match_admin.jpg)

#### Edit Match
This enables the manager to amend the time, date and location of matches. The form mirrors the form to add fixtures and is autopopulated with the details of the selected match.

#### Delete Match
This allows the manager to delete a match and all associated MatchPlayer instances.

#### Open Registrations
Once registrations have been opened for a match the booking form is enabled and the match date is displayed.  Registrations can only be open for one match at a time.  If the manager tries to open registrations for a second match an error message will be displayed. Once match registrations are open the option displayed is amended to 'close match registrations'.

#### Flag Next Fixture
The next fixture flag controls which match details are displayed on the Next Fixture page.  Only one match can be flagged at a time.  Trying to flag a second fixture results in a custom error message being displayed. If a match is flagged as the next fixture the option changes to 'remove next fixture flag'.

#### Allocate Teams
A maximum of 12 members per week can play. Once 12 people have registered a function can be called to allocate players to either the blue or the white team as follows: 
The points are calculated dynamically by accessing the past results stored on the MatchPlayer models associated with each registered. Players are sorted in descending order according to their current points. If 2 or members have the same number of points, they are then ranked according to the number of matches with players with  the fewest number of matches played ranking higher. The username has been added as a third field to avoid players with the same number of points and matches played having the same index.

The teams are then assigned according to the players' position in the sorted list:
Blues: 1, 4, 6, 8, 10, 12
Whites: 2, 3, 5, 7, 9, 11

Once assignment has occurred the next fixture details are updated with the team details and the 'Allocate Teams' button changes to 'Clear Teams'.  In the event that a player who has a place on the team cancels, the manager would use the Clear Teams button to clear the current selection and then click on 'Allocate Teams' again to resort the players. When 'Allocate Teams' is called after confirmed players cancel, it checks the number of confirmed players and then pulls in members from the reserve list, which is sorted by booking time, until 12 players are reached. 


#### Add Results
The manager has the ability to manually enter the latest match score. The MatchPlayers are allocated either a win, loss or a draw according to the results input by the manager. A win counts as 3 points, a draw as 1 point and a loss as 0 points. The league table view is then able to recalculate and update the player scores and sort the players. The new scores are automatically populated in the latest results table by the results view.

If the results have already been added then the manager has the option to delete the result if they have made a mistake.  The statistics of the players in the match are updated by the league_table view to reflect that the result has been annulled.

![Results Form](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/add_result.jpg)

#### View Players
This feature was added after being requested by the manager during the project review. He wanted to be able to see which players had registered for a match prior to allocating teams and displaying them im the member zone.

### Member Admin
The member admin page offers the manager the possibility to view, approve or rejects any pending club membership applications. Once an applicant has been approved or rejected an email is auto generated to advise them of the club decision.

The member page also contains a list of all approved members with their email addresses so that the club manager is able to contact them if necessary.  The manager has the possibility of deleting members if they leave the club or are barred for misbehaving!

![Member Admin](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/member_admin.jpg)

## Media Queries
A cropped version of the main homepage image is used for smaller devices.

On mobiles non essential columns are hidden on tables by using a 'mobile-hide' class to improve readability.

On the league table only the player, played and points columns appear and on the results page just the match date and the scores are displayed as these are the statistics by which the players are ranked.

The club manager informed me that he intended to carry out the club admin on a laptop but may occasionally need to open the match registrations, allocate teams or add scores on a mobile device so these were the match admin fields chosen to be displayed on small screens.

![Mobile Views](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/mobile-views.jpg)

For the member admin page he felt the most important fields were the approve and reject buttons for pending applications and the email address for current members so the other columns were hidden.


## Bugs and Challenges
I had several problems when trying to customize the standard allauth signup form and create the ClubMember model. Each time I ran a migration I was getting an error message.  I tried to resolve the issue through my own research but eventually contacted tutor support with the below problem statement.

![Allauth Problem Statement](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/allauth_issues.jpg)

Deleting the database and the migrations file did eventually resolve the issues which I did with the help of Ed at tutor support.

The next fixture page  was throwing an error if no matches were flagged as the next fixture and causing the site to crash. To resolve this I added an if statement so that if now matches were flagged the latest match would be displayed.

I tried to determine the matches played, won, drawn and lost and total points for each member by adding property methods to the ClubMember model. These methods calculated the figures by retrieving the MatchPlayer instances created with the player_id of the ClubMember. Although this worked, I ran into an issue as I was not able to sort the players by methods in the league table.  I eventually resolved this by removing the methods from the property models and calculating the number of matches and points in the league table view instead.

Initially the allocate teams functions was not working correctly.  if 2 members had the same number of points and matches played, one of the members was being omitted. I realised that this could be because they had been allocated the same index number in the database so added a 3rd search parameter, the username, which rectified the issue

The styling in the base.css file was not being applied in the deployed version although the local version did not have the same issue.  I discussed this with my mentor during our final meeting and we tried changing the roots to the static files but it still was not working as expected.  As the css files in the app directory did not have the same issues I tried moving the base.css file to the app folder and it resolved the issue.  The only problem that remained was that the main image on the home page was not loading.  I had originally loaded it as a background image on a container div as I wanted the heading to appear within the image.  To rectify this I loaded it instead as an image element and used z-indexes and absolute positioning to make the main heading text appear in front of the image. Unfortunately when messages appeared at the top of the screen this then moved the heading outside the image borders. I decided to resize the background image and move the heading on top and all issues were resolved.

### 404 Page
I created a custom 404 page with a link to the home page to handle incorrect addresses 

![404 Page]()

## Testing

### Automated Tests
All 4 css files passed through the W3C CSS validation service with no errors.

The map js file was copied to the JSHint validator and returned the following results:
![JavaScript Validation](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/js-validation.jpg)

Python testing:
Many errors were returned for the views file of the type 'Match has no objects member'.  These were ignored as advise in the CI blog walkthough project.
Long line errors have not been corrected where they formed part of the preinstalled setting or I felt that splitting the lines would impair the readability of the code.

I created some automated tests for views and forms following the examples in the Hello Django module.  These are not currently running correctly as they are returning errors concerning the database connection.  I have tested the same features manually and they are working as expected. 




### Manual Tests
Manual testing was carried out by myself and the club manager.

Messages confirming user actions appear at the top of the screen.

All navigation links work as expected althought the navbar hides the title of the social section.

The Google map api works and displays the correct location.

The Next Fixture page displays the correct details and links to the booking page if registrations are open.  If teams have been allocated the names are displayed.

The Player League table sorts the players correctly and highlights the details of the logged in user.

The match booking form works as expected and generates a new MatchPlayer instance.  The display on the page changes according to whether registrations are open and the player has already booked a place in the match. If the team is full the message returns the correct place on the reserve list. If a confirmed player cancels an email to the manager is generated.

The 'add fixture' form generates a new instance of the Match model.

The 'edit fixture' form updates the Match details correctly.

The 'next fixture' flag works. Details of the next fixture are updated on the template.  An error message appears if the manager attempts to flag more than one match as the next fixture.

The 'open registrations' function works.  The booking page is updated allowing members to register. An error message appears if the manager tries to open registrations for more than one match. Emails are auto generated to all club members.

The 'add results' form is displayed correctly.  When submitted the player scores update on league table and the results appear on the results page. 

The 'see members' function shows all members that have registered their availability for the next match.

Approving a member results in the member moving from the pending applications to the confirmed member list, allows them to login to the member zone and generates an email to the member.

Rejecting a member results in the application being removed and generates an email to the applicant.

Deleting a member removes them from the database.

I tested all auto generated emails using my own email address and received the expected messages.

![Test Emails](https://github.com/BelT26/RDFC/blob/main/club/static/club/screenshots/test-emails.jpg)




## Deployment
The project was created on Github and deployed via Heroku following the steps below based on the Code Institute 'I think therefore I blog' walkthrough project:

### In Github
* Initialise a git repository

### In the Gitpod terminal
* Install Django and gunicorn by entering pip3 install Django==3.2 gunicorn in the terminal
* Install the postgres database by entering pip3 install dj_database_url psycopg2 in the terminal
* Install Cloudinary libraries by entering pip3 install dj3-cloudinary-storage
* Create a requirements file by typing pip3 freeze --local > requirements.txt
* Create a project folder in the current directory by typing django-admin startproject reigate-dads .
* Create the app folder by entering python3 manage.py startapp RDFC
* Add 'RDFC' to the list of installed apps in settings.py
* Migrate Changes using the command python3 manage.py migrate

### In Heroku
* Login to Heroku, click on the 'NEW' button and create a new app
* Navigate to the Resources tab and add 'Heroku Postgres'
* In the settings tab click to reveal the Config Vars and copy the DATABASE_URL value.

### In Gitpod
* Create new env.py file on top level directory
* At the top of this file type 'import os'
* To link the database enter 'os.environ["DATABASE_URL"] =' followed by the value copied from Heroku in inverted commas
* Add a secret key by typing 'os.environ["SECRET_KEY"] = ' followed by the name of your chosen secret key in inverted commas

### In Heroku
* Navigate to the the settings tab and add the Secret Key to the Config Vars

#### In Gitpod
* Open up the settings.py file and add the following code
    from pathlib import Path
    import os
    import dj_database_url
    if os.path.isfile("env.py"):
        import env
* Remove the secret key from settings.py and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* To update the database replace the old database settings with 
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
* Enter python3 manage.py migrate in the terminal

#### In Cloudinary.com: 
* Login and copy your CLOUDINARY_URL from the Cloudinary Dashboard

#### In Gitpod
* Add the Cloudinary URL to the env.py file in the following format:
    os.environ["CLOUDINARY_URL"] = "cloudinary://************************"

#### In Heroku:
* In settings add the Cloudinary URL to the Config Vars 

#### In Gitpod
* Add the following Cloudinary Libraries to the list of installed apps in settings.py in the order below:
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
* Add the following code to settings.py to let Django know to use Cloudinary for static and media files:
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
* Add the following code to settings.py under BASE_DIR to link the templates directory
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    TEMPLATES = [
    {'DIRS': [TEMPLATES_DIR],},
    ]
* Add the allowed hosts: ALLOWED_HOSTS = ["reigate-dads.herokuapp.com", "localhost"]
* Create static, media and templates folders in the top level directory 
* Create a new file named 'Procfile' in the top level directory and add the code:
    web: gunicorn PROJ_NAME.wsgi
* Add, commit and push all changes to Github

#### In Heroku:
* Deploy the site manually using Github as the deployment method, on the main branch


## Credits
I learnt how to send emails in Django from the following online tutorial [Pretty Printed Django Email Tutorial](https://www.youtube.com/watch?v=X7DWErkNVJs)

The following tutorial was used as a guide for using template tags in the homepage. [Template Tags Tutorial](https://engineertodeveloper.com/a-better-way-to-route-back-to-a-section-ids-in-django/)

The text for the home page was provided by Steve Wilson, the club manager.

The club logo was created using Canva

The favicon was generated using favicon.io

Raleway and Roboto fonts were imported from Google Fonts.

The social media icons and the icons in the contact section were imported from Font Awesome

#### Images
* Home page banner:  Mick Haupt / Unsplash
* Social section: Rawpixel / Shutterstock
* League table: QuinceCreative / Pixabay
* Results table: Chaos Soccer / Unsplash
* Next fixture: Emrah Kara / Unsplash

## Future Development Possibilities
In the future I would like to address the items marked in the user stories as priority to promote the social side of the club. I plan to add a social page showing future get-togethers and give the manager the possibility to add events.  

Another possibility that was discussed with the club manager was the inclusion of a blog style page containing match reports. These would be uploaded by the manager after the game and all members would be able to like and comment on them.
