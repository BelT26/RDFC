# Reigate Dads FC

https://belt26.github.io

## Author: Helen Taylor  
## Version 1.0.0

![site preview on a variety of devices]()


## Contents
* [Overview](#overview)
* [Planning](#planning)
    * [Initial Meeting](#initial-meeting)
    * [Epics](#epics)
    * [User Stories](#user-stories)
    * [Project Review](#project-review)
* [Models](#models)
    * [ClubMember](#clubmember)
    * [Match](#match)
    * [MatchPlayer](#matchplayer)
* [Features](#features)
    * [User Authentications](#user-authentication)
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
        * [Member Admin](#member-admin)
        * [View Players](#view-players)
* [Bugs and challenges](#bugs-and-challenges)
* [Testing](#testing)
    * [Automated Tests](#automated-tests)
    * [Manual Tests](#manual-tests)
* [Deployment](#deployment)
* [Credits](#credits)
* [Future Development Opportunities](#future-development-possibilities)

## Overview

Site created for a friend of mine who is the manager of an amateur football club. He was finding it time consuming to manually manage match registrations, update the player league table and keep all members informed of club activities.

## Planning

Meeting with club manager to ascertain requirements.  
Project created with Kanban template on Github
26 User Stories added to initial board
Word document created to break down user stories into tasks
Set up views / urls / templates in club app folder
Added member model
Added member zone
Set up base html and base css
Add navbar and footer to base html
Club manager indicated that it would be important to be store reserves on a list and have the possibility of reallocating teams if a team member cancelled.

## Models

### ClubMember

### Match

### MatchPlayer

## Features

## User Authentication
Django Allauth was installed to enable users to sign up, log in and log out.  I customised the standard Allauth model  
so that users also need to enter their first and last name when signing up

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
The home page is split into three sections, accessible by a dropdown menu, a general introduction to the club, a social section and a contact section including a Google map showing where the team play.

## Map
I used the Bootstrap Resume walkthrough project as a guide to creating the JavaScript code to link to the Google Maps API.  At the moment only one location is marked as the club both play and socialise at the South Park grounds.  I decided to still use marker clusters as the club manager mentioned to me that he may like to add other venues to the map in the future


## Member Zone


### Next Fixture
The next fixture page shows members the details of the next match.  If no match has been flagged by the manager as the next fixture then the most recent match in the database is displayed.

Members can see whether the booking system is currently open for the match displayed.  If it is a link is shown which takes them to the match booking form.

Once the manager has allocated the teams for the match the player names and a list of the reserves are displayed.

### League Table
The league table sorts the players by the number of points they have scored and then by the number of matches they have played. When two or more players have the same number of points the player who has played the fewer matches ranks more highly.

### Past Results

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

#### Flag Next Fixture


#### Allocate Teams
A maximum of 12 members per week can play. Once 12 people have registered a function is called to allocated players to either the blue or the white team as follows: 
The registered players are sorted in descending order according to their current points.
If 2 or members have the same number of points, they are then ranked according to the number of matches with players with  the fewest number of matches played ranking higher
The teams are then assigned according to the players' position in the sorted list:
Blues: 1, 4, 6, 8, 10, 12
Whites: 2, 3, 5, 7, 9, 11
Once assignment has occurred the next fixture details are updated with the team details.


#### Add Results
The manager has the ability to manually enter the latest match score.
The winning team gets 3 points, the losing team 0 points and in the case of a draw each team receives 1 point.
Players automatically inherit their team’s points once the scores have been input by the manager
The league table automatically updates the player scores and resorts the players.
The scores areautomatically populated in the latest results table


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

#### Images
Home page banner:  Mick Haupt / Unsplash.
Social section: Rawpixel / Shutterstock
League table: QuinceCreative / Pixabay
Results table: Chaos Soccer / Unsplash
Next fixture: Emrah Kara / Unsplash

## Future Development Possibilities

Add the possibility to add social events - not current requirement

Add to the management functionality so that they can manually adjust members details

Add a blog featuring the weekly match report

