# 1189. Maximum Number of Balloons

## Desc

> Given a string **text**

> you want to use the characters of **text** to form as many word of **balloon** as possible

> You can use each character in **text** **at most once**.

> Return the maximum number of instances that can be formed.

## Idea

> We can solve this problem by using two HashMap

> To start, we can counter the number of occrance of each char in **text**

> Then we count the number of occurance of each char in **balloon**

> As the maximum number of instances depends on the minimum number char in the text

> We can find the minimum ratio of char in t and char in balloon, and that will be the answer

## Complexity

### TC: O(n)

### SC: O(1)