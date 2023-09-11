# 2101. Detonate the Maximum Bombs

## Desc

> You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.

> This area is in the shape of a circle with the center as the location of the bomb

> The bomb are represented by a 0-indexed 2D integer array bombs where ith value denotes the x-coord and y-coord of the location

> where r denotes the radius of its range

> You may choose to detonate a single bomb, when a bomb is detonated, it will detonate all bombs that lie in its range

> These bombs will further detonate the bombs that lie in their ranges

> Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb

## Idea

> We can use DFS to solve this problem

> To build the graph from the list, we will iterate the list and compare the current bomb to the rest of the list

> we will calculate the distance between the two origins, and if the distance is less than any of the radius, we will add the one to theothers neighbor

> Then we will perform dfs for each bomb, and for each bomb, we will keep track of the visited bombs, and we simply return the visited bombs for each bomb

> the result will simply be the maximum among the number of all the visited bombs for each bomb

## Complexity

### TC: O(n^2)
### SC: O(n^2)