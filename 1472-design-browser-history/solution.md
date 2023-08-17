# 1472. Design Browser History

## Desc

> You have a **browser** of one tab where you start on the **homepage** and you can visit another **url**

> get back in the history number of **steps** or move forward in the history number of **steps**

> Implement the **Browser History** class

> **BrowserHistory(string homepage)** initializes the object with the **homepage** of the browser

> **void visit(string url)** visits **url** from the current page. It clears up all the forward history

> **string back(int steps)** move **steps** back in hitory. If you can only return **x** steps back

> and **step > x**, then return only history **x** steps back

> **string forward(int steps)** similar to **back**

## Idea

> We can use a linked list to solve this problem

> When initializing the object, we init head with homepage as value, and a current pointer to point at the head

> **visit** will simply add a new node after the current node

> **back and forward** will check if the **prev and next** pointer of the current node, and iterate **step times**

> If the **prev or next** is null during the iterations, simply break and return the current node

## Complexity

### TC: O(1)/ O(k)

### SC: O(n)