How to Incorporate Google+ Hangout With Python
==============================================

We will have a central server hosted somewhere (such has http://ludum-dare.jacobvgardner.com).  This server will act as a matchmaker server (cue Fiddler on the Roof Matchmaker song) and central daterbase.  For ease of development, we may do the battlefield 3 approach for everything (as described here).  

The game will run an http server on localhost (0.0.0.0 so it cannot be connected to externally).

Starting the game will minimize it and open a browser to a central page showing a list of available games to join or create a game option.  

When an game is created/joined a request will be sent to the local http server telling it what the client desires.   

There will also be an option to join a google+ hangout for the game.  If this is chosen the browser will be opened to our google+ hangout app.  This app will send its link to the central server so that anyone else joining can join that hangout.  

The hangout could also be used to display game stats and whatnot if we cared.


Advantages
----------

- by leveraging the browser, we don't have to make a menu for the game 
- allows us to provide multiplayer chat/video/etc. easily

Disadvantages
-------------

- People may not want us spinning up http servers on their computers (they don't really have to know how it works though...).  IT WOULD BE SECURE
- People may hate having to use the browser
- Requires us to support some sort of http client for displaying information (this may only be a disadvantage if this would take more work than doing it all in-game)


Architecture
============

A central server that uses gevent or twisted.  It will be what clients connect to and handle game-logic.

Django Server - Requests from the central server who is currently connected and displays that information.  Also general game info that we wish to provide.

client - The game that interacts with the central server, and hosts the local http server that the django server tries to communicate with.