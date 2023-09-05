# 953. Verifying an Alien Dictionary

## Desc

> In an alien language, suprisingly, they also use English lowercase letters, but possibly in a different order.

> The **order** of the alphabet is some permutation of lowercase letters.

> Given a sequence of **words** written in the alien language, and the **order** of the alphabet, return **true** if and only if

> the given **words** are sorted lexicographically in this alien language.

## Idea

> We can first create a mapping between the alphabet and the index

> Then, we can iterate the sequence, and check if they follow the order by comparing the neighboring words

> If at any time, the current word starts with the next word, we return False, as it does not follow the order

> Or if at any time, the current char of the current word is not equal to the current char of the next word

> we simply theck the index map, and if the first index is larger than the second index, we simply return False

> otherwise it is sorted

## Complexity

### TC: O(m * n)
### SC: O(1)