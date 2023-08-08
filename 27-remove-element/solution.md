# 27. Remove Element

## Desc

> Given an integer array **nums** and an integer **val**, remove all occurances of **val** in **nums** **in-place**.

> The order of the elements may be changed

> Then return the number of elements in **nums** which are not equal to **val**

## Idea

> We can use two pointers to solve this questions

> Both pointers are init to 0 at first, and we increment the fast pointer during each iteration

> For each iteration, if number at fast is not **val**, then we switch the number at **slow** and **fast**

> Then increment the slow pointer

> After we iterate the whole array, no **val** will be in nums from **0 to slow**

## Complexity

### TC: O(n)

### SC: O(1)
