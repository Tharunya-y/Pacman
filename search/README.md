## Farnaz mozghani ,Tharunya Yogananda ,Thasmaya Yogananda
# Summary of learning
There were noticeable variations in the exploration patterns and efficiency of each algorithm when tested in various maze sizes. DFS explored pointless pathways in bigger mazes but proved effective in micro mazes. Although BFS guaranteed the shortest path, it visited a lot of nodes, which resulted in a lot of exploration. A* was the most effective, balancing cost with heuristic guidance to produce an ideal path with fewer explored nodes, whereas UCS prioritized lower-cost pathways to decrease path cost. The overlay of explored nodes confirmed these behaviors, especially in how DFS and BFS explored nodes without prioritizing cost or goal proximity.
# Screenshots 
Screenshots of successful run for questions 1 , 2, 3 and 4 (DFS , BFS , UCS and A* search) when implemented.

DFS
![DFS](<images/Screenshot 2024-10-31 112130.png>)

BFS
![BFS](<images/Screenshot 2024-10-31 112209.png>)

UCS
![UCS](<images/Screenshot 2024-11-01 113114.png>)

A*
![A*](<images/Screenshot 2024-10-31 112412.png>)

# Question Response
 
1. Running DFS in Pacman demonstrated its depth-first exploration pattern: in tinyMaze, DFS quickly found the goal, while in larger mazes like mediumMaze and bigMaze, it explored deeply into many areas before reaching the target. The exploration overlay, with brighter red indicating earlier exploration, confirmed DFS's deep-diving nature, marking many paths without necessarily following each to completion. Pacman did not travel to every explored square on the way to the goal, as DFS marks states but only pursues one path at a time.
