# 680. Valid Palindrome II

## Desc

> Given a string **s**

> return **true** if the **s** can be palindrome after deleting **at most 1** character from it

## Idea

> We can solve this question by using two pointers

> We start with initializing the pointers to point at 0 and the last index of **s**

> Then, as we traverse the string, if the chars at two pointers are the same, we simply update the pointer

> Otherwise, we can write a helper function to help us to check whether it's still a palindrome by skipping one

> If the helper function returns **True** by skipping one of the pointer, then it's still valid.

> If we tried both pointer, and the helper function return **False** for both trial, then return **False**

> After iterating the whole **s**, simply return **True** as it suffice the definition of palindrome

## Complexity

### TC: O(n)

### SC: O(1)