# Jak and Daxter: The Precursor Legacy Random Cell Order, Python Edition and Knuckles
### Author: SiliconWG
### Date: 6 March 2022

## Description:
A power cell order randomizer (RCO) for Jak and Daxter: The Precursor Legacy [1] for Play Station 2 made in Python. The main purpose of this project is to make RCO more accessible to casual players. This project is a work in progress (WIP). I am not in the habit of opening WIP projects to the public. However, with everything else going on in my life, this project might never be worked on again. Even though it is unfinished, I believe it to be functional, and I would like people to see it. Some improvements I would like to make are in the notes section.

## Features:
- Adaptable order for multiple skill sets. Choose between "casual" and "speedrun" logic.
- Precursor orb logic.
- Misty Island logic. Power cells on Misty Island are not required before completing fish game.
- Minor streamlining. See notes.

## Notes:
- Speedrun logic assumes the player knows how to perform (1) idle deloads, specifically for skipping the Klaww boss fight, and (2) out of bounds skips, e.g., in Sentinel Beach to stop the cannon and get the orbs which normally requires the blue eco vent be opened and in Snowy Mountain to get Flut Flut outside her intended area as well as opening the lurker fortress door without Flut Flut rescued.
- Casual logic assumes that the player needs to activate eco vents and save Flut Flut to access their corresponding power cells.
- Both skill logic settings are also able to choose their random cell minimum as 4, 20, 45, 72, or 101.
- Orb logic is set by three assumptions: (1) All orbs in a given area are accessible from the moment you first enter it, (2) only visited areas have their orbs counted toward the available total, and (3) areas are not considered visited until a power cell is obtained within.
  - An example would be as follows. You collect the 4 power cells from Geyser Rock and return to Sandover Village. At this point, 50 orbs are counted as "available". This means that power cell 5 cannot be any of the trading cells in Sandover Village, i.e. with the Mayor, Uncle, or Oracle since Sandover Village has not been counted as visited yet. If cell 5 is one in Sentinel Beach or Forbidden Jungle, then the available orb total is updated to 200, and cell 6 can be any of the trading cells in Sandover Village. However, if cell 5 is one of the nontrading cells in Sandover Village, then the orb total is updated to only 100, and cell 6 CAN be trading with either the Mayor or Uncle but CANNOT be trading with the oracle. This does not mean that cell 6 is always a trading cell, but it does mean that cell 6 is the first point at which it is possible to obtain a trading cell.
- Streamlining consists of trying my best to not force skipping of obvious path cells. This is a mostly comprehensive list of the "logic" I have implemented.
  - Geyser Rock: The randomizer will not place "Climb up the cliff" before "Open precursor door"
  - Forbidden Jungle: The randomizer will not place "Defeat dark plant" before "get to the top of the temple" OR "Find the blue vent switch".
  - LPC: The randomizer will not place "Reach the bottom of the city" and "Climb the slide tube" before "Reach the center of the complex".
  - Mountain Pass: The randomizer will not place the zoomer cells in Mountain Pass before "Defeat Klaww".
  - Snowy Mountain: The randomizer will not place "Get through the lurker fort" before "Open the lurker fort gate"
  - Gol and Maia's Citadel: The randomizer will not place "Free the green sage" or "Find the 7 scout flies" before freeing the other three sages and collecting their respective power cells.
- There are several unpolished pieces of this program which I would like to improve upon or add to:
  - Improve the streamlining such that small sequences are implemented. This would primarily show up in the Forbidden Jungle temple, where climbing the tower is immediately followed by opening the blue eco vents followed by defeating the dark eco plant, or at least some version of this progression. There are other areas where this would be helpful but none worth mentioning here.
  - Solidify the logic such that "available" orbs or scout flies are not locked behind walls I forgot to consider.
- I started this project mainly to practice using objects and object oriented programming in Python. I put this program together over a weekend, and I was somewhat careless in the manner I went about making it since I wanted it to just be a fun little thing. I apologize if this steps on any toes; that was never my intention.
- Knuckles is not actually in this randomizer, I just think it's a fun meme to attach "and knuckles" to the end of seemingly excessively long titles.

## Code Version:
This project was developed using the latest Anaconda 3 Python distribution. At the time of writing, the relevant package versions are:
- Python 3.8.12
- IPython 7.31.1
- Numpy 1.20.3

## Acknowledgment:
I would like to specifically thank SixRockFire for creating the C++ version of RCO [2]. This RCO edition was heavily inspired by that program. I would also like to thank the Jak speedrunning community for the inspiration and good times.

## References:
```
[1] Jak and Daxter: The Precursor legacy, Greatest Hits Edition. Play Station 2. Naughty Dog, 2001

[2] SixRockFire/JakRCO: A Jak and Daxter power cell order randomizer (c++). github.com/https://github.com/SixRockFire/JakRCO. Accessed: 6 March 2022. Online.
```
