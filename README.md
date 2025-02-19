# aiexp
Esperiments with AI

cd /puzzle8 

<img width="126" alt="puzzle 8 sample" src="https://github.com/user-attachments/assets/336fd34d-5a49-4b06-beae-aeaacc7c01cc" />

python3 puzzle8.py

The puzzle8.py is able to solve the puzzle8 (whenever possible) using one of three algorithms:

search_algorithms='depth_first_search', 'breadth_first_search', 'best_first_search'

The solve method returns the solution.
You can print all the moves calling the "printTheSolution" method passing the returned solution

you will get something like this:

```
PUZZLE 8 SOLVER - AI Search State Space algorithms

Current puzzle to solve:

---------
 1  2  3 
 4  0  5 
 6  7  8 
---------

### Search algorithm depth_first_search ###
         -> Solution found in 16 moves with 4923 iterations

### Search algorithm breadth_first_search ###
         -> Solution found in 29974 moves with 52786 iterations

### Search algorithm best_first_search ###
         -> Solution found in 16 moves with 71 iterations

---------
 1  2  3 
 4  0  5 
 6  7  8 
---------

---------
 1  2  3 
 4  5  0 
 6  7  8 
---------

---------
 1  2  3 
 4  5  8 
 6  7  0 
---------

---------
 1  2  3 
 4  5  8 
 6  0  7 
---------

---------
 1  2  3 
 4  5  8 
 0  6  7 
---------

---------
 1  2  3 
 0  5  8 
 4  6  7 
---------

---------
 1  2  3 
 5  0  8 
 4  6  7 
---------

---------
 1  2  3 
 5  6  8 
 4  0  7 
---------

---------
 1  2  3 
 5  6  8 
 4  7  0 
---------

---------
 1  2  3 
 5  6  0 
 4  7  8 
---------

---------
 1  2  3 
 5  0  6 
 4  7  8 
---------

---------
 1  2  3 
 0  5  6 
 4  7  8 
---------

---------
 1  2  3 
 4  5  6 
 0  7  8 
---------

---------
 1  2  3 
 4  5  6 
 7  0  8 
---------

---------
 1  2  3 
 4  5  6 
 7  8  0 
---------

---------
 1  2  3 
 4  5  6 
 7  8  0 
---------
```


