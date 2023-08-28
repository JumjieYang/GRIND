# 68. Text Justification

## Desc

> Given an array of strings **words** and a width **maxWidth**, format the text such that each line has exactly **maxWidth** characters

> And it is fully justified

> You should pak your words in a greedy approach; that is, packa as many words as you can in each line. Pad extra spaces when necessary

> Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words

> the empty slots on the left will be assigned more spaces than the slots on the right

> For the last line of text, it should be left-justified, and no extra space is inserted between words

## Idea

> We can solve this problem by simulate the whole process

> We will first create the result array, and the current line array, as well as a variable to track the current width

> Then, we can iterate through the words

> At each step, we first check if we can insert a new word into the line,

> that is, we check if the sum of the width of the words in the line with 1 extra space and the current word is less than or equal to the threshold

> If not, we will consider the current line as completed, and add it to the resulting array

> Otherwise, we will add the word to the current line, and update the current width

> To add the line to the resulting array, we will first compute how many spaces we need to insert between the words, and then insert the spaces

> After those procedures, we can add the line to the res, and clean the line and width for next line

> In the end, when we building the last line, we simply consider the trailing spaces, that is, we will only add 1 space between the words, and fill the array with spaces

## Complexity

### TC: O(nk)

### SC: O(n)