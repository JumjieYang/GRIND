# 1584. Min Cost to Connect All Points

## Desc

> You are given an array **points** representing integer coordinates of some points on a 2D-plane, where ith value is x, y

> The cost of connecting two points x_1, y_1 and x_2, y_2 is the manhattan distance between them

> Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points

## Idea

> We can use Prim's algorithm to solve this problem

> To start with, we will keep track of the total cost, number of points connected, and visited points

> And to kick off the process, we will create a minheap, with **(cost, node)** pair

> Then, as long as the we haven't connect the whole points, we will try to connect the new points

> we will pop the first element from the heap, and check if it is visited, if it is, we simply skip it

> if not, we will add this node to visited points, and increment the total cost and number of points connected

> then we will search for other points, if any point is not visited, we will simply compute the cost between the two, and add the cost with the point to the heap

## Complexity

### TC: O(n^2logn)
### SC: O(n^2)