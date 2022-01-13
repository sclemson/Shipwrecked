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
  <img src="https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Trello%20Board.png" width="53.1%"  />
  <img src="https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Trello%20Script.png" width="45%" /> 
</p>

This stage of the project required a huge amount of testing to ensure that the inventory updated according to the stage of the game that a player was at. Our **startGame async function** accessed the **items** section of our **API** and used a **GET** request to load objects that a player had picked up and this became a **POST** request within the **makeSave async function** so that, on loading, _Shipwrecked_ would use the API to access those levels and zones which had been completed. We used **Postman** and **Django** itself to test this aspect of the game extensively,  with Preston in particular honing each aspect of the save function until we had surpassed our MVP in this particular area.

## Day 4
With the content of the game written, our **zones.js** and **items.js** files needed populating. The zones and items were designed as **React components** with **classes** which stored the property values of that particular component. The **constructors** called during the creation of these two types of object looked like this:

**Zones**

![Zone Class](https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Zones%20Class.png)

**Items**

![Item Class](https://github.com/sclemson/Shipwrecked/blob/main/client/src/images/Items%20Class.png)

Both the **zones.js** and the **items.js** files were huge and the main job for the day was populating these from the game scripts on Trello. With the game written, any spare time that I had in the evenings at this point was spent populating the game database and creating the level artwork on **Adobe Photoshop**.

As the database expanded, we were increasingly able to test the functionality of the game via huge numbers of **console.logs** throughout. Working through this allowed Preston to hone the **game.js** file in particular - with a key focus for the day being the **COMBINE** function which worked by reading the **creates** section of the **Item** component (see above), and then subsequently added the newly created item to the **inventory** array whilst removing the ‘ingredient’ items from the inventory.

## Days 5 - 6
The nuances of the **save** function and the very nature of the game meant that we also had to do a huge amount of work on the **zone.js** file, above and beyond what we had already completed. Each zone in the game needed to have several different states in order to progress. For example, the **rockpool** on level one had to have three states, one in which a coin had not been given to a crab, one where the coin _had_ been given to the crab but the player had not picked up the exposed metal, and one where the player had picked up the exposed metal. Each different state had a **solution** which meant that the next state was triggered. Our **‘barrier’ zones** (which were the invisible ‘gateways’ between levels) worked in a similar way and our constant testing meant that new bugs and obstacles to player progress were constantly being revealed, meaning that the player functions: **WALKTO**, **USE**, **EXAMINE**, **GIVE**, **PICKUP**, **TALKTO**, and **COMBINE** needed honing in order to ensure that puzzles were solvable and game progress was possible. 

By this stage we had begun to build our **frontend** game components and were able to see both the **TextDisplay.js** and **SecondTextDisplay.js** files on our **localhost** screen. Again, we reverted to using **Live Share** continuously at this point, altering content that didn’t quite work, debugging continuously, and altering different aspects of the game to ensure that ‘playing through’ (or at least playing through the first few levels) was possible. 

