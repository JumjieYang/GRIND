# 187. Repeated DNA Sequences

## Desc

> Given a string **s** that represnets a **DNA sequence**

> return all the **10-letter-long** sequences (substring) that

> occur more than once in a DNA module.

> You may return the answer in **any order**

## Idea

> We can use sliding window to solve this problem

> To begin with, we can init two empty HashSet, **res** and **visited**
> As we have fixed length sliding window, we can simply iterate the whole string

> For each window, we first check if it is visited before, if it is, then add it to res

> We add current window to visited

> After iterate the whole list, we convert the **res** set to list and return

## Complexity

### TC: O(n)

### SC: O(n)