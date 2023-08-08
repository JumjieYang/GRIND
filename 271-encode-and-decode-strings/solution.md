# 271. Encode and Decode Strings

## Desc

> Design an algorithm to encode **a list of strings** to **a string**.

> The encoded string is then sent over the network and is decoded back to the original list of strings

## Idea

> If the range of input if fixed, we can encode with the char not in range, and decode with same char

> If the range of input is not fixed, then we can use a predefined section with customized parser

## Complexity

### TC: O(n)

### SC: O(n)