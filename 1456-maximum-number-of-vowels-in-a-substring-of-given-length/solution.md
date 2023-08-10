# 1456. Maximum Number of Vowels in a Substring of Given Length

## Desc

> Given a string **s** and an integer **k**

> return the maximum number of vowel letters in any substring of **s** with length **k**

> **Vowel letters in English are a, e, i, o, u**

## Idea

> We can use sliding window to solve this problem

> As the size of window is fixed to **k**

> We can start to iterate the string from left and right

> And for each char visited, if it is a vowel, we simply increment the counter

> And if we have more elements than **k**, we simply remove the first element in window

> If that is an vowel, we simply decrement the counter

> The maximum number is simply the maximum count we encountered during the iteration

## Complexity

### TC: O(n)

### SC: O(1)