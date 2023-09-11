# 2477. Minimum Fuel Cost to Report to the Capital

## Desc

> There is a tree structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads

> The capital city is city 0. You are given a 2D integer array roads where ith value denotes that

> there exists a bidirectional road connecting cities a and b.

> There is a meeting for the representatives of each city. THe meeting is in the capital city.

> There is a car in each city. You are given an integer seats that indicates the number of seats in each car

> A representative can use the car in their city to travel or change the car and ride with another representative

> The cost of travelling between two cities is one liter of fuel.

> Return the minimum number of liters of fuel to reach the capital city.

## Idea

> We can use Topological sort to solve this problem

> Before getting started, we will build the graph and count the degree of each node

> Then, we create an empty queue, and put all nodes with degree 1 to the queue, as they are the furthest cities in the network

> Then, we create another array to keep track the number of representatives in each city.

> Then we can start the topo sort, at each step, we will calculate the ceil value of current number of representatives in city divide by seats

> then add the value to the total fuel, and we will search the neighbors, and for each neighbor, we will first decrease the degree,

> and update the number of representatives in the neighbor, then if the degree of the neighbor is 1, and it is not capital, we will add

> the city to the queue and traverse further

## Complexity

### TC: O(|V| + |E|)
### SC: O(|V| + |E|)