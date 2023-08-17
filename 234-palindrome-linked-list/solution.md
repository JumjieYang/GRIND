# 234. Palindrome Linked List

## Desc

> Given the **head** of a singly linked list, return **true** if it is a **palindrome** or **false** otherwise

## Idea

> We can get the mid of the linked list, and reverse it to get the **tail**

> Then, we can begin the comparation, as long as the **tail** is not null, we compare and increment the pointers

> If at any point, **head and tail** don't have the same value, then the linked list is not a palindrome

> Otherwise, it is a palindrome