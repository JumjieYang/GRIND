# 367. Valid Perfect Square

## Desc

> Given a positive integer **num**, return **True** if **num** is a perfect square

> You must not use any built-in library function, such as **sqrt**

## Idea

> To solve this problem, we can use binary search

> We can start by initing two pointers to be 1 and **num** respsectively

> Then, as long as the two pointer doesn't cross, we compute the mid value

> if the square of the mid value equals **num**, we simply return **True**

> as it is the definition of perfect square

> otherwise, if the result is lower, we search the upper part, vise versa

> If the two pointers cross, and we yet find an answer, simply return False

## Complexity

### TC: O(logn)

### SC: O(1)