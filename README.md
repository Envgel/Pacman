# Pacman

The aims of this project are to improve the understanding of the various search algorithms and to experience how to derive heuristics, using the Berkely Pacman framework.

The Pac-Man projects were developed for UC Berkeley's introductory artificial intelligence course, CS 188. They apply an array of AI techniques to playing Pac-Man. However, these projects don't focus on building AI for video games. Instead, they teach foundational AI concepts, such as informed state-space search, probabilistic inference, and reinforcement learning. These concepts underly real-world application areas such as natural language processing, computer vision, and robotics.

There are four pars in this project:

# Part 1: 

Implement the Iterative Deeping Search algorithm. You should be able to test the algorithms using the following command:

python pacman.py -l mediumMaze -p SearchAgent -a fn=ids

# Part 2: 

Implement the Weighted A* algorithm discussed in lectures using W = 2. You should be able to test the algorithm using the following command:

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=wastar,heuristic=manhattanHeuristic

# Part 3: 

Just like in Q7 of the Berkerley PacMan framework, we woud like to create an agent that will eat all of the dots in a maze.
Before doing so, however, the agent must eat a Capsule that is present in the maze. Your
code should ensure that no food is eaten before the Capsule. You can assume that there is
always exactly one Capsule in the maze, and that there will always be at least one path from
Pacman’s starting point to the capsule that doesn’t pass through any food.
In order to implement this, you should create a new problem called CapsuleSearchProblem
and a new agent called CapsuleSearchAgent. You will also need to implement a suitable
foodHeuristic. You may choose to implement other helper classes/functions. You should
be able to test your program by running the following code:
python pacman.py -l capsuleSearch -p CapsuleSearchAgent
-a fn=wastar,prob=CapsuleSearchProblem,heuristic=foodHeuristic
An agent that eats the capsule then proceeds to eat all of the food on the maze will receive 3
marks. The remaining 3 marks will be based on the performance of your agent (i.e. number
of nodes expanded), as in Q7 of the Berkeley problem. Since you are using the Weighted A*
algorithm, however, the number of node expansions required for each grade will vary.



