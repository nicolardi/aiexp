# aiexp
Esperiments with AI


/puzzle8 

python3 library.py

library.py solves the puzzle8 (whenever possible) using one of two algorithms (others following)

search_algorithms='depth_first_search', 'breadth_first_search', 'best_first_search'


you can choose one algorithm changing the line 
algo = 'depth_first_search'

NOTE:   
puzzle8 cannot always be solved


```
Current puzzle to solve
---------
 1  2  3 
 4  0  5 
 6  7  8 
---------
Search algorithm depth_first_search
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
SOLVED!!! 15 moves !!!
Solution found with 4693 iterations
```


