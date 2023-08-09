# 125. Valid Palindrome

## Desc

> Given a string **s**, return **true** if it is a **palindrome**, or **false** otherwise

## Idea

> We can use two pointer to solve this problem

> To start with, we can set the left pointer to 0, and right pointer to the last index of string

> Then, as long as the two pointer doesn't meet, we iterate the string and update the pointers

> For each iteration, if the char at any pointer is not alphanumeric, we simply skip the char

> When the chars of two pointers are both alphanumeric, and if they are not the same, return **False**

> Otherwise keep iterating the string

> Once we finish iterating the string, simply return True as it is a palindrome by definition

## Complexity

### TC: O(n)

### SC: O(1)