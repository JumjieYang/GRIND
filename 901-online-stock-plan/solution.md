# 901. Online Stock Span

## Desc

> Implement the **StockSpanner** class

> **StockSpanner()** initializes the object of the class

> **int next(int price)** returns the **span** of the stock's price given the today's price

> The span of the stock's price in one day is the maximum number of consecutive days(backwards)

> for which the stock price was less than or equal to the price of that day

## Idea

> We can use a stack to implement the class

> to initialize the object, we simply create an empty stack where the val will be **(price, span)** pair

> then for next operation, we simply calculate the span and pop out all the element smaller than the current price

> then append the current price and current span to the stack

## Complexity

### TC: O(n)

### SC: O(n)