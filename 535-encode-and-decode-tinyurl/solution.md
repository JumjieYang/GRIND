# 535. Encode and Decode TinyURL

## Desc

> Implement the **Solution** class

> **Solution()** initializes the object of the system

> **String encode(longUrl)** return a tiny URL for the given longUrl

> **String decode(shortUrl)** return the original long URL for the given shortUrl

## Idea

> We can use two HashMaps and a count to implement the class

> When init, we init the count to be 0, and **encode_map** and **decode_map** as two maps

> for encode, we can assign the longUrl to be the value of **(count, value)** pair

> then, we place the pair in **encode_map**, and vise versa for **decode_map**

> then increment the count

> for decode, we simply read from the map

## Complexity

### TC: O(1)

### SC: O(n)