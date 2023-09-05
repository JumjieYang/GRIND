# 721. Accounts Merge

## Desc

> Given a list of accounts where each element is a list of strings, where the first element is a name, and the rest are emails

> Now, we would like to merge these accunts, two accounts definitely belong to the same person if there is some common email to both accounts

> A person can have any number of accounts initially, but all of their accounts definitely have the same name

> After merging the accounts, return the accounts in the following format

> the first element of each account is the name, and the rest of the element are emails in sorted order. The accounts themselves can be returned in any order

## Idea

> We can use Union-Find to solve this problem

> To start with, we can first create user-email pairs, and we need to keep track of all the pairs

> And when we create the pairs, for each entry, we consider the first pair as the root element, and we will union the pairs of the same person

> Then, we will create a HashMap that contains user-email pair as the key and emails as the value, and populate this map

> Finally, we will iterate all the entry in the map we just created, and build the entry as needed

## Complexity

### TC: O(NK log NK)
### SC: O(NK)