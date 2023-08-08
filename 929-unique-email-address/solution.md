# 929. Unique Email Addresses

## Desc

> Every **valid email** consists of a **local name** and a **domain name**, separated by the **@** sign.

> Besides lowercase letters, the email may contain one or more **.** or **+**

> If you add periods **.** between some characters in the **local name** part of an email address, ignore the **.**

> If you add a plus **+** in the **local name**, everything after the first plus sign **will be ignored**

> It is possible to use both of these rules at the same time

> Given an array of strings **emails**, return the number of different addresses

## Idea

> We can use a HashSet to solve this problem

> We can start by iterating each email in the array

> For each email, we can split the email with **@**

> And then for the local part, we can replace **.** with empty string and only take the part where we encounter first *
*+**

> After the whole process, we can add the (local, domain) in the hashset

> Once we finish iterate the whole list, the number of elements in the set will be the answer

## Complexity

### TC: O(n * maxlen(email))

### SC: O(n)
