# Hash Table

- Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

<br>

## Challenge

- Implement Hashtable data-structure and manipulate it.

<br>

## Features

- add

> _This method  hash the key, and add the key and value pair to the table, handling collisions as needed._

- get

> _Returns Value associated with that key in the table_

- contains

> _Returns Boolean, indicating if the key exists in the table already._

- hash


> _Returns Index in the collection for that key_


## Big O_________


- Time and Space complexity (__hash) --> O(1).

- Time and Space complexity  (add) --> O(1).

>  **contains**
- Time --> O(n).
- Space -->  O(1).

>  **get**
- Time --> O(n).
- Space --> O(1).

<br>

## Testing

- [x] Adding a key/value to your hashtable results in the value being in the data structure
- [x] Retrieving based on a key returns the value stored
- [x] Successfully returns null for a key that does not exist in the hashtable
- [X] Successfully handle a collision within the hashtable
- [X] Successfully retrieve a value from a bucket within the hashtable that has a collision
- [x] Successfully hash a key to an in-range value

