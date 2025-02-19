
# aiexp

Experiments with AI

<img width="126" alt="puzzle 8 sample" src="https://github.com/user-attachments/assets/336fd34d-5a49-4b06-beae-aeaacc7c01cc" />

## How to Run

```bash
cd puzzle8
python3 puzzle8.py
```

## Run Unit Tests

```bash
python3 puzzle8_test.py
```

# Details

The `puzzle8.py` script can solve the puzzle8 (whenever possible) using one of three algorithms:

- `depth_first_search`
- `breadth_first_search`
- `best_first_search`

The `solve` method returns the solution. You can print all the moves by calling the `printTheSolution` method with the returned solution.

You will get something like this:

```
PUZZLE 8 SOLVER - AI Search State Space algorithms

Current puzzle to solve:

---------
 1  2  3 
 4  0  5 
 6  7  8 
---------

### Search algorithm depth_first_search ###
         -> Solution found in 14 moves with 4923 iterations. Visited nodes: 2937

### Search algorithm breadth_first_search ###
         -> Solution found in 29972 moves with 52786 iterations. Visited nodes: 30772

### Search algorithm best_first_search ###
         -> Solution found in 22 moves with 119 iterations. Visited nodes: 68

### Search algorithm A* ###
         -> Solution found in 14 moves with 189 iterations. Visited nodes: 110

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

```