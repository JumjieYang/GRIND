# 332. Reconstruct Itinerary

## Desc

> You are given a list of airline tickets where ith value repesent the departure and the arrival airports of one flight

> Reconstruct the itinerary in order and return it.

> All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries

> you should the itinerary that has the smallest lexical order when reading as a single string.

> You may assume all tickets form at least one valid itinerary.

> You must use all the tickets once and only once.

## Idea

> We can use DFS with greedy algorithm to solve this problem

> Before we traverse the graph, we need to build the graph first

> We start with sort the tickets, which will provide us with a lexical order

> Then, we will create an empty HashMap, with the key be the airport name, and the value be a deque containing the destinations

> And then we will populate the graph, and create a result list with 'JFK' in it initially

> Then, for DFS function, we will first check if the result list has enough elements, if it is, we simply return True to indicate it is valid

> If the current element we visit is not in the graph, we return False to indicate it is invalid

> Then, we will try to pop each neighbor of the current node in the graph to see if we can form a valid itinerary, if it is, we simply return True

> Otherwise we return False, and for each time we visit a neighbor, we add it to the result list, and pop if not valid

## Complexity

### TC:(|E| * max_flights_from_an_air_port)

### SC: O(|V| + |E|)

