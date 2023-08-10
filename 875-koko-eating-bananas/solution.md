# 875. Koko Eating Bananas

## Desc

> Koko loves to eat bananas. There are **n** piles of bananas, the ith pile has corresponding bananas

> The guards have gone and will have come back in **h** hours

> Koko can decide her bananas-per-hour eating speed of **k**.

> Each hour, she chooses some pile of bananas and eats **k** bananas from that pile.

> If the pile has less than **k** bananas, she eats all of them instead and will not eat any more during this hour

> Koko likes to eat slowly but sill wants to finish eating all the bananas before the guards return

> Return the minimum integer **k** such that she can eat all the bananas within **h** hours

## Idea

> To solve this problem, we can use binary search

> we can set the pointers to be **1 and max among piles** respectively

> And while the pointers don't cross, we compute the mid point

> for each mid computed, we will check if she can eat all the bananas within **h** hours

> If she can, we search the lower part, otherwise upper part

> And the result will simply be the larger pointer + 1 after the whole iteration

## Complexity

### TC: O(nlogn)

### SC: O(n)


