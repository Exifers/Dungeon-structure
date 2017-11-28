# Dungeon-structure
Generates randomly a basic plan for a dungeon with rooms and corridors, to make a video game out of it.

# How to use it ?
You need python 2.7 with pygame and numpy installed. Just run graph1.5.py script and it shows a window with a basic representation of the dungeon.

# Display
It displays elements next to each other.
Each element can be :
- an entrance    : in yellow
- a  corridor    : in grey
- a  locked room : in blue
- a  key room    : in red
The idea behind those elements is:
The player starts the game in the entrance. Then he visits the dungeon and finds some keys (one per key room). Once he has three keys he can open something in the locked room.

# Bugs
This is work in progress project.
- Some elements get stuck on (0, 0) coordinates on top left corner

# Improvements
Those feature needs to be improved :
- Corridors are alway horizontals
- Elements can go out of the window
- Elements are separated byg gaps (we can't figure out well how rooms are connected)

# Todo
Those features would be interesting if implemented :
- Make sure that there's no dead-ends
- Make several layers with stairs/elevator
- Implement difficulty and difficulty increase with tests
- Build the map in a video game environment

# Licence
You're free to copy and use this code how you want.

# Author
Emmanuel aka Exifers
