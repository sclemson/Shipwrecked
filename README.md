# Shipwrecked

## Project Overview
_Shipwrecked_ is a text-based RPG puzzler about trying to get off a desert island. The game was my final project on the General Assembly Software Engineering course and was created in collaboration with ![Preston Ng](https://github.com/sungchun) and used **Django**, **Python**, **JavaScript** and **React**.

I wanted to create a project that utilised a database in a different way so came up with the idea of an RPG. I was responsible for database and app design as well as the writing of the game itself. The project provided a creative solution to a project brief and provided significant opportunities to embed learning from across the SEI course.

## The Brief
- Build a full-stack application by making your own backend and your own frontend.
- Use a Python Django API using Django REST Framework to serve your data from a Postgres database.
- Consume your API with a separate front-end built with React.
- Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models.
- Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut.
- Be deployed online so it’s publicly accessible.

## First Steps
Initially, I had conceived of _Shipwrecked_ as a solo project but, in initial planning conversations with my course cohort, it became clear that Preston was just as passionate about the concept as I was. Our initial conversations also led us to conclude that the game that we envisaged would take both of us to complete within the timeframe that we had. We spent some time thinking about the structure of the game and how it would work in reality, focussing particularly hard on our pseudocode. Finally, we pitched our idea to our instructor who was concerned that we were taking on too much given our deadline. He set us the challenge of building one particular section of the first level of the game - we had to demonstrate that we could get the player to ‘walk’ to a particular area and ‘pickup’ an object within it - do this successfully, and we would be signed off…

## Day 1
As the project had so many components and we would need to work on separate elements for the most part, we decided to code the whole thing using **Live Share** on **VS Code** so that we would be able to test our code constantly. Our goal for the first day was simply to demonstrate viability and, as a result, we focussed on two key areas:

- The structure of each level in the game.
- The method by which we would give our character instructions.

We had a clear idea of how to go about our initial challenge and decided to try and build an entire section of a level, reasoning that - if this was feasible - we could work with this structure for the rest of the levels within the game. We came up with a system of **zones** within levels with each containing **objects**. I wrote the problems for the first level, based on the structure that we had designed, and we implemented the first version of our **WALKTO** command which used a **GET** request to access a particular **ZoneID**. Each zone in the game would contain certain objects so the **PICKUP** function was designed to check a zone for the object’s presence, if the object was there we used a **POST** request to put that object into the player’s inventory. With this achieved, we were signed off and we set about developing the rest of the game.

## Days 2 - 3
Our sign off meant that we could now focus on fleshing out the game’s structure. I started off by building the framework of the **backend**, ensuring that Shipwrecked had authentication capability and the ability for users to register and login. We followed this by revisiting the game structure that we had designed, then focussing on two main elements:

- The **content** of the game itself, which I took responsibility for.
The **save** function - a key aspect of the brief was to create something with **CRUD** capability, and we decided that the ability to save games would be a way of achieving this. We started with the MVP of simply being able to save which zone a player was in at any one time, but ideally wanted the game to remember the items that the player had in their inventory as well. Preston went on to design this particular aspect of the game.

As we were working on very separate aspects of the game we set up a **Trello** board to monitor progress. To this, I added scripts for each level (as well as the background graphics that I designed later in the week).

<p float="left">
  <img src="https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Trello%20Board.png" width="53.2%"  />
  <img src="https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Trello%20Script.png" width="45%" /> 
</p>


