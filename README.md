# Reigate Dads FC

https://belt26.github.io

## Author: Helen Taylor  
## Version 1.0.0

![site preview on a variety of devices]()


## Contents
* [Overview](#overview)
* [Planning](#planning)
* [Stucture](#structure)
* [Features](#features)
    * [Navigation](#navigation)
    * [Home Page](#home)
    * [Map](#map)
    * [Social Events](#social-events)
    * [Member Zone](#member-zone)
        * [Log In Form](#log-in-form)
        * [Next Fixture](#fixture)
        * [League Table](#league-table)
        * [Past Results](#past-results)
        * [Match Registration](#match-registration)
        * [Coutdown Clock](#countdown-clock)   
    * [Manager Zone](#manager-zone)
        * [Fixture Updates](#fixture-updates)
        * [Team Selection](#team-selection)
        * [Social Updates](#social-updates)
        * [Match Results](#match-results)
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

## Structure

## Features

## Navigation

## Home Page

## Map

## Social Events

## Sign Up Form

## Member Zone

### Log In Form

### Next Fixture

### League Table

### Past Results

### Match Registration

### Countdown Clock


## Manager Zone

### Fixture Updates
The Manager is able to add, cancel and edit the next match fixture details


### Team Selection
A maximum of 12 members per week can play. Once 12 people have registered a function is called to allocated players to either the blue or the white team as follows: 
The registered players are sorted in descending order according to their current points.
If 2 or members have the same number of points, they are then ranked according to the number of matches with players with  the fewest number of matches played ranking higher
The eams assigned according to the players' position in the sorted list:
Blues: 1, 4, 6, 8, 10, 12
Whites: 2, 3, 5, 7, 9, 11
Once assignment has occurred the next fixture details are be updated with the team details.


### Social Updates
The manager is able to add details and images of upcoming social events


### Match Results
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

## Testing

### Automated Tests
Tests to check that all fields are required on the sign up form and the password is at least 8 characters passed.

### Manual Tests
Tested that the modified sign up form worked manually and that new members were created.

## Deployment

## Credits

## Future Development Possibilities

