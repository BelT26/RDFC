# Reigate Dads FC

https://belt26.github.io

## Author: Helen Taylor  
## Version 1.0.0

![site preview on a variety of devices]()


## Contents
* [Overview](#overview)
* [Planning](#planning)
    * [Project Conception Meeting](#project-conception-meeting)
    * [User Stories](#user-stories)
    * [Project Review](#project-review-meeting)
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
    * [Map](#map)
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
* A function that would allocate teams based on the members' current points and number of matches played
* A league table displaying all players' results
* A sign up facility so that new members can apply to join the club 

Optional features that were discussed were:
* A page displaying details of the next fixture and the names of the players in each team
* A table containing the results of past games
* A page on which the manager could upload match reports and other members could comment
* A page dedicated to upcoming social events

### User Stories
After receiving the initial project brief I created a project with the Kanban template on Github and added user stories. 
Following my first meeting with the club manager the list of stories was extended. They were arranged into epics as shown in the table below and allocated a priority rating of between 1 and 3 with priority 1 being the most important.
User stories were broken down into tasks as in the example below.

### Project Review Meeting
Once the project was near completion I scheduled another meeting with the club manager to review the progress of the site. Steve was happy to leave the pages for the match reports and social events to a later date, but requested that I add a page in which he could view which members had registered for the upcoming match and also a facility whereby players could be placed on a reserve list if all of the team places were already taken so that he could reassign the place if somebody cancelled.
I suggested adding an email alert so that Steve would be advised if a team member cancels and would know to reallocate the teams.

## Models
I used three models to create this project, ClubMember, Match and MatchPlayer

### ClubMember
The ClubMember model is a custom user model that inherits from the Django user model.

### Match
The Match model is used to create an instance of each game.  The details are used to populate the Next Fixture and Past Results pages and the manager is able to manage the properties of each Match within the Match Admin table. 

### MatchPlayer
Each time a ClubMember registers for a Match an instance of the MatchPlayer field is created.  The MatchPlayer model has two foreign keys: the match_id that is based on the Match model and the player_id that is based on the ClubMember model.
The results of each game are stored on the MatchPlayer model and these are used to dynamically generate the scores for the player league table.

## Features

## User Authentication
Django Allauth was installed to enable users to sign up, log in and log out.  I customised the standard Allauth model  
so that users also need to enter their first and last name when signing up

## Messages
Feedback on user interaction is provided via Django messages.  Bootstrap classes have been applied to convey success or error messages.  The code to install and customise the messages was taken from the 'I think therefore I blog' walkthrough project.

## Navigation
I created a responsive navbar that collapses on mobile devices using Bootstrap classes.  The items displayed on the navbar change according to whether the user is logged in or not and whether they are the club manager.

### General User Access
Visitors to the site can view general information about the club.  They also have the option of signing up to the club or logging in if they are a member.

### Member Access
Once a user has logged in their logged in status is displayed on the right of the navbar. Logged in users have access to the member zone in which they can book a place in the next match, view details of the next fixture, view past results and view the player league table.

### Manager Access
As well as all of the member facilities, the manager has access to a dropdown management menu.  This offers options for him to add a new match fixture, update details of the existing matches and approve and remove members.

## Footer
The footer contains social media links to Facebook, Twitter and Instagram.  The club manager has not yet set up accounts with these sites so the links currently take the user to the home page. These links will be updated once the club's accounts have been created.

## Home Page
The home page is split into three sections, accessible by a dropdown menu, a general introduction to the club, a social section and a contact section including a Google map showing where the team play. The links to each of the sections were created using template tags.

## Map
I used the Bootstrap Resume walkthrough project as a guide to creating the JavaScript code to link to the Google Maps API.  At the moment only one location is marked as the club both play and socialise at the South Park grounds.  I decided to still use marker clusters as the club manager mentioned to me that he may like to add other venues to the map in the future


## Member Zone

### Next Fixture
The next fixture page shows members the details of the next match.  If no match has been flagged by the manager as the next fixture then the most recent match in the database is displayed.

Members can see whether the booking system is currently open for the match displayed.  If it is, a link is shown which takes them to the match booking form.

Once the manager has allocated the teams for the match, the player names and a list of the reserves are displayed.

### League Table
The league table sorts the players by the number of points they have scored and then by the number of matches they have played. When two or more players have the same number of points the player who has played the fewer matches ranks more highly.

### Past Results
The past results page shows the scores of any previous matches so that members can find out about any games they missed.  The members of each teams are also listed.

### Match Booking Form
If match registrations are open a booking form is displayed. Otherwise users see a message informing them that registrations are currently closed. In the booking form users can see the date of the match.  

12 members can register for a match once this number has been reached the user is informed that the match is full but they are still able to book a place on the reserve list.  If they do decide to be a reserve a message shows them their place on the list when they submit the form.

If a member has already registered for the match rather than being shown the 'book match place' button they are given the option to cancel their place. If teams have already been allocated by the manager and the member has a place on the team, an email is generated to the manager to inform them that a player has cancelled and that they need to reselect the teams.

## Manager Zone

### Add Fixture
The Manager is able to create a new match and add the date, time and locations

### Match Admin

#### Edit Match
This enables the manager to amend the time, date and location of matches.

#### Delete Match
This allows the manager to delete a match and all associated MatchPlayer objects.

#### Open Registrations
Once registrations have been opened for a match the booking form is enabled and the match date is displayed.  Registrations can only be open for one match at a time.  If the manager tries to open registrations for a second match an error message will be displayed.

#### Flag Next Fixture
The next fixture flag controls which match details are displayed on the Next Fixture page.  Only one match can be flagged at a time.  Trying to flag a second fixture results in a custom error message being displayed.

#### Allocate Teams
A maximum of 12 members per week can play. Once 12 people have registered a function can be called to allocate players to either the blue or the white team as follows: 
The points are calculated dynamically by accessing the past results stored on the MatchPlayer models associated with each registered. Players are sorted in descending order according to their current points. If 2 or members have the same number of points, they are then ranked according to the number of matches with players with  the fewest number of matches played ranking higher. The username has been added as a third field to avoid players with the same number of points and matches played having the same index.
The teams are then assigned according to the players' position in the sorted list:
Blues: 1, 4, 6, 8, 10, 12
Whites: 2, 3, 5, 7, 9, 11
Once assignment has occurred the next fixture details are updated with the team details and the 'Allocate Teams' button changes to 'Clear Teams'.  In the event that a player who has a place on the team cancels, the manager would use the Clear Teams button to clear the current selection and then click on 'Allocate Teams' again to resort the players. When 'Allocate Teams' is called after confirmed players cancel, it checks the number of confirmed players and then pulls in members from the reserve list, which is sorted by booking time, until 12 players are reached. 


#### Add Results
The manager has the ability to manually enter the latest match score. The members of the winning team gets 3 points, the losing team 0 points and in the case of a draw all players receive 1 point.
The MatchPlayers are allocated either a win, loss or a draw according to the results input by the manager. The league table view then recalculates and updates the player scores and sorts the players. The new scores areautomatically populated in the latest results table

If the results have already been added then the manager has the option to delete the result if they have made a mistake.  The statistics of the players in the match are automatically updated to reflect that the result has been annulled.

#### View Players
This feature was added after being requested by the manager during the project review. He wanted to be able to see which players had registered for a match prior to allocating teams and displaying them im the member zone.

### Member Admin
The member admin page offers the manager the possibility to view, approve or rejects any pending club membership applications. Once an applicant has been approved or rejected an email is auto generated to advise them of the club decision.

The member page also contains a list of all approved members with their email addresses so that the club manager is able to contact them if necessary.  The manager has the possibility of deleting members if they leave the club or are barred for misbehaving!

## Bugs and Challenges
Linking to specific sections of a page[linking](https://engineertodeveloper.com/a-better-way-to-route-back-to-a-section-ids-in-django/)


Issues when testing deployment mid project were resolved with the help of Alan at tutor support who identified that my requirements.txt did not contain all of my dependencies.  Solved by freezing the requirements.txt file again.

I had several problems when trying to customize the standard allauth signup form and create the ClubMember model. Each time I ran a migration I was getting an error message.  The original message informed me 

book match place not working. implemented manual test driven approach, gradually increasing functionality

mambers page throwing an error if next fixture was not flagged. added try block

allocate teams functions not working correctly.  if 2 members had the same number of points and matches played the one of the members was being omitted. realised that this was because they had the same index number so added a 3rd search parameter which resolved the issue

## Testing

### Automated Tests


### Manual Tests


## Deployment

## Credits

The text for the home page was provided by Steve Wilson, the club manager.

The club logo was created using Canva

Raleway and Roboto fonts were imported from Google Fonts.

The social media icons and the icons in the contact section were imported from Font Awesome

#### Images
Home page banner:  Mick Haupt / Unsplash.
Social section: Rawpixel / Shutterstock
League table: QuinceCreative / Pixabay
Results table: Chaos Soccer / Unsplash
Next fixture: Emrah Kara / Unsplash

## Future Development Possibilities

In the future I would like to address the items marked in the user stories as priority to promote the social side of the club. I plan to add a social page showing future get-togethers and give the manager the possibility to add events.  

Another possibility that was dicsussed with the club manager was the inclusion of a blog style page containing match reports. These would be uploaded by the manager after the game and all members would be able to like and comment on them.
