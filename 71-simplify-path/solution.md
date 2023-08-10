# 71. Simplify Path

## Desc

> Given a string **path**, which is an **absolute path** (starting with a slash '/') to a file in a Unix-like system

> convert it to the simplified **canonical path**

> In a Unix-style file system, a period '.' refers to the current dir, a double period '..' refers to the dir up a level

> any multiple consecutive slashes are treated as a single slash '/'

> any other format of periods are treated as file names

> The **canonical path** should have the following format

> The path starts with a single slash

> Any two directories are separated by a single slash '/'

> The path does not end with a trailing '/'

> The path only contains the directories on the path from the root dir to the target file or dir

> Return the simplified **canonical path**.

## Idea

> We can solve this problem by using a stack

> To begin with, we can create a single stack

> then, we split the string with '/'

> and for each component, we do the operation based on the content

> if the content is '..', we simply pop the stack

> else if the content is '.' or empty, we ignore the content

> otherwise we simply append the content

> After traversing the whole string, we simply return the stack joined by '/'