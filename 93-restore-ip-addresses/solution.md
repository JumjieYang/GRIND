# 93. Restore IP Address

## Desc

> A valid IP address consists of exactly four integers separated by single dots.

> Each integer is between 0 and 255 and cannot have leading zeros

> Given a string **s** consists only digits, return all possible IP addresses that can be formed by inserting dots into **s**

> You are not allowed to reorder or remove any digits in **s**. You may return the valid IP addresses in any order.

## Idea

> We can solve this problem by using backtracking

> We can first check the length of the string, if it is longer than 12 chars, we can simply return empty list

> Otherwise, we can begin to perform the backtracking, we will keep track the current index, dot used, and current ip string

> if at anytime, we have reached the end of the string and we use 4 dots, we will add the ip string to the result

> and if at anytime, we use more than 4 dots, we simply ignore the result, as it won't be valid

> for all other cases, we will get upto the next 3 chars, and see if the integer value of them is less than 256, and keep traversing

## Complexity

### TC: O(m^n * n)

### SC: O(mn)