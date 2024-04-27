# ArrayUtilities (Arr)

[![Tests](https://github.com/borkweb/python-arrayutilities/workflows/Tests/badge.svg)](https://github.com/borkweb/python-arrayutilities/actions?query=branch%3Amain)

A library for list, dict, and UserDict manipulations.


## Installation

Install arrayutilities via pip:

```bash
pip install arrayutilities
```

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
    * [accessible](#usage.accessible)
    * [add](#usage.add)
    * [add\_prefixed\_keys\_to](#usage.add_prefixed_keys_to)
    * [add\_unprefixed\_keys\_to](#usage.add_unprefixed_keys_to)
    * [array\_visit\_recursive](#usage.array_visit_recursive)
    * [collapse](#usage.collapse)
    * [dot](#usage.dot)
    * [exists](#usage.exists)
    * [filter\_prefixed](#usage.filter_prefixed)
    * [first](#usage.first)
    * [flatten](#usage.flatten)
    * [forget](#usage.forget)
    * [get](#usage.get)
    * [has](#usage.has)
    * [insert\_after\_key](#usage.insert_after_key)
    * [insert\_before\_key](#usage.insert_before_key)
    * [is\_dict](#usage.is_dict)
    * [is\_list](#usage.is_list)
    * [join](#usage.join)
    * [last](#usage.last)
    * [list\_to\_array](#usage.list_to_array)
    * [merge\_recursive](#usage.merge_recursive)
    * [only](#usage.only)
    * [prepend](#usage.prepend)
    * [pull](#usage.pull)
    * [query](#usage.query)
    * [random](#usage.random)
    * [recursive\_ksort](#usage.recursive_ksort)
    * [set](#usage.set)
    * [shape\_filter](#usage.shape_filter)
    * [shuffle](#usage.shuffle)
    * [sort\_by\_priority](#usage.sort_by_priority)
    * [sort\_recursive](#usage.sort_recursive)
    * [sort\_recursive\_desc](#usage.sort_recursive_desc)
    * [stringify\_keys](#usage.stringify_keys)
    * [strpos](#usage.strpos)
    * [to\_list](#usage.to_list)
    * [undot](#usage.undot)
    * [usearch](#usage.usearch)
    * [where](#usage.where)
    * [where\_not\_none](#usage.where_not_none)
    * [wrap](#usage.wrap)

## Usage

Here are descriptions and usage examples for each method in the `Arr` class that you can get by:

```python
from arrayutilities import Arr
```

<a id="Arr.accessible"></a>

### accessible

```python
@staticmethod
def accessible(value)
```

Determines if the given value is a list, dict, or UserDict.

**Arguments**:

- `value` _Any_ - Value to determine if it is accessible.


**Returns**:

- `boolean` - Whether the the value is a list, dict, or UserDict.

<a id="Arr.add"></a>

### add

```python
@staticmethod
def add(array, key, value)
```

Add an element to an array if it doesn't exist.

**Arguments**:

- `array` - Array to manipulate.
- `key` - Key to use.
- `value` - Value to inject.


**Returns**:

  Manipulated array

<a id="Arr.add_prefixed_keys_to"></a>

### add\_prefixed\_keys\_to

```python
@staticmethod
def add_prefixed_keys_to(array, recursive=False)
```

Duplicates any key not prefixed with '_' creating a prefixed duplicate one.

**Arguments**:

- `array` - Array to manipulate.
- `recursive` _bool, optional_ - Whether to recursively change the array. Defaults to False.


**Returns**:

  Manipulated array.

<a id="Arr.add_unprefixed_keys_to"></a>

### add\_unprefixed\_keys\_to

```python
@staticmethod
def add_unprefixed_keys_to(array, recursive=False)
```

Duplicates any key prefixed with '_' creating an un-prefixed duplicate one.

**Arguments**:

- `array` - Array to manipulate.
- `recursive` _bool, optional_ - Whether to recursively change the array. Defaults to False.


**Returns**:

  Manipulated array.

<a id="Arr.array_visit_recursive"></a>

### array\_visit\_recursive

```python
@staticmethod
def array_visit_recursive(input_array, visitor)
```

Recursively visits all elements of an array applying the specified callback to each element key and value.

**Arguments**:

- `input_array` - The input array whose nodes should be visited.
- `visitor` - A callback function that will be called on each array item; the callback will
  receive the item key and value as input and should return an array that contains
  the update key and value in the shape [ &lt;key&gt;, &lt;value&gt; ]. Returning a null
  key will cause the element to be removed from the array.


**Returns**:

  Manipulated array.

<a id="Arr.collapse"></a>

### collapse

```python
@staticmethod
def collapse(array)
```

Collapse an array of arrays into a single array.

**Arguments**:

- `array` - Array of arrays to collapse.


**Returns**:

  Collapsed array.

<a id="Arr.dot"></a>

### dot

```python
@staticmethod
def dot(array, prepend='')
```

Flatten a multi-dimensional associative array with dots.

**Arguments**:

- `array` - Array to manipulate.
- `prepend` _str, optional_ - Value to prepend to dict keys. Defaults to ''.


**Returns**:

  Manipulated array.

<a id="Arr.exists"></a>

### exists

```python
@staticmethod
def exists(array, key)
```

Determine if the given key exists in the provided array.

**Arguments**:

- `array` - Array to check.
- `key` - Key to look for.


**Returns**:

- `boolean` - Whether or not the key exists.

<a id="Arr.filter_prefixed"></a>

### filter\_prefixed

```python
@staticmethod
def filter_prefixed(array, prefix)
```

Filters an associative array non-recursively, keeping only the values attached to keys starting with the specified prefix.

**Arguments**:

- `array` - Array to filter.
- `prefix` _str|list_ - The prefix or prefixes of the keys to keep.


**Returns**:

  Filtered array.

<a id="Arr.first"></a>

### first

```python
@staticmethod
def first(array, callback=None, default=None)
```

Return the first element in an array passing a given truth test.

**Arguments**:

- `array` - Array to look at.
- `callback` _Callable, optional_ - Callback function that returns a boolean of whether to match or not. Defaults to None.
- `default` _optional_ - Default value if no other value is found. Defaults to None.


**Returns**:

  Found value or default.

<a id="Arr.flatten"></a>

### flatten

```python
@staticmethod
def flatten(array, depth=float('inf'))
```

Flatten a multi-dimensional array into a single level.

**Arguments**:

- `array` - Array to flatten.
- `depth` _number, optional_ - Number of nestings deep that should be flattened. Defaults to float('inf').


**Returns**:

  Flattened array.

<a id="Arr.forget"></a>

### forget

```python
@staticmethod
def forget(array, keys)
```

Remove one or many array items from a given array using "dot" notation.

**Arguments**:

- `array` - Array to manipulate.
- `keys` _str|array_ - Key or keys to remove.

<a id="Arr.get"></a>

### get

```python
@staticmethod
def get(array, keys, default=None)
```

Find a value inside of an array or object, including one nested a few levels deep.

**Arguments**:

- `array` - Array to search
- `keys` _str|array_ - Key or keys to get.
- `default` _optional_ - Value to return if none found. Defaults to None.


**Returns**:

- `_type_` - _description_

<a id="Arr.has"></a>

### has

```python
@staticmethod
def has(array, keys)
```

Check if an item or items exist in an array using "dot" notation.

**Arguments**:

- `array` - Array to check.
- `keys` _str|array_ - The indexes to search; in order the function will look from the first to the last.


**Returns**:

- `boolean` - Whether the key exists or not.

<a id="Arr.insert_after_key"></a>

### insert\_after\_key

```python
@staticmethod
def insert_after_key(key, source_array, insert)
```

Insert an array after a specified key within another array.

**Arguments**:

- `key` _str|number_ - The key of the array to insert after.
- `source_array` _array_ - The array to insert into.
- `insert` _Any_ - Value or array to insert.


**Returns**:

  Manipulated array.

<a id="Arr.insert_before_key"></a>

### insert\_before\_key

```python
@staticmethod
def insert_before_key(key, source_array, insert)
```

Insert an array before a specified key within another array.

**Arguments**:

- `key` _str|number_ - The key of the array to insert before.
- `source_array` _array_ - The array to insert into.
- `insert` _Any_ - Value or array to insert.


**Returns**:

  Manipulated array.

<a id="Arr.is_dict"></a>

### is\_dict

```python
@staticmethod
def is_dict(array)
```

Returns whether the array is a dict or not.

**Arguments**:

- `array` _array_ - Array to check.


**Returns**:

- `boolean` - Whether the array is a dict or not.

<a id="Arr.is_list"></a>

### is\_list

```python
@staticmethod
def is_list(array)
```

Returns whether the array is a list or not.

**Arguments**:

- `array` _array_ - Array to check.


**Returns**:

- `boolean` - Whether the array is a list or not.

<a id="Arr.join"></a>

### join

```python
@staticmethod
def join(array, glue, final_glue='')
```

Join all items using a string. The final items can use a separate glue string.

**Arguments**:

- `array` - Array to join.
- `glue` _str_ - String to inject between elements.
- `final_glue` _str, optional_ - String to inject between the final two elements. Defaults to ''.


**Returns**:

- `str` - Joined string.

<a id="Arr.last"></a>

### last

```python
@staticmethod
def last(array, callback=None, default=None)
```

Return the last element in an array passing a given truth test.

**Arguments**:

- `array` - Array to look at.
- `callback` _Callable, optional_ - Callback function that returns a boolean of whether to match or not. Defaults to None.
- `default` _optional_ - Default value if no other value is found. Defaults to None.


**Returns**:

  Found value or default.

<a id="Arr.list_to_array"></a>

### list\_to\_array

```python
@staticmethod
def list_to_array(value, sep=',')
```

Converts a list to an array filtering out empty string elements.

**Arguments**:

- `value` _str|number|None_ - A string representing a list of values separated by the specified separator
  or an array. If the list is a string (e.g. a CSV list) then it will urldecoded
  before processing.
- `sep` _str, optional_ - The char(s) separating the list elements; will be ignored if the list is an array. Defaults to ','.


**Returns**:

  Manipulated array.

<a id="Arr.merge_recursive"></a>

### merge\_recursive

```python
@staticmethod
def merge_recursive(array1, array2)
```

Recursively merge two arrays preserving keys.

**Arguments**:

- `array1` - Starting array.
- `array2` - Array to merge into the first.


**Returns**:

  Merged array.

<a id="Arr.only"></a>

### only

```python
@staticmethod
def only(array, keys)
```

Get a subset of the items from the given array.

**Arguments**:

- `array` - Array to search.
- `keys` _str|array_ - Key or keys to include in the final array.


**Returns**:

  Array subset.

<a id="Arr.prepend"></a>

### prepend

```python
@staticmethod
def prepend(array, value, key=None)
```

Push an item onto the beginning of an array.

**Arguments**:

- `array` - Array to manipulate.
- `value` _Any_ - Value to prepend.
- `key` _string|number, optional_ - Key value for the prepended item. Defaults to None.


**Returns**:

  Manipulated array.

<a id="Arr.pull"></a>

### pull

```python
@staticmethod
def pull(array, key, default=None)
```

Get a value from the array, and remove it.

**Arguments**:

- `array` - Array to search and manipulate.
- `key` _str|number_ - Key to look for and fetch.
- `default` _Any, optional_ - Default value if none found. Defaults to None.


**Returns**:

- `Any` - The found value or default.

<a id="Arr.query"></a>

### query

```python
@staticmethod
def query(data)
```

Convert the array into a query string.

**Arguments**:

- `data` - Array to convert.


**Returns**:

- `str` - URL query string.

<a id="Arr.random"></a>

### random

```python
@staticmethod
def random(array, number=None, preserve_keys=False)
```

Get one or a specified number of random values from an array.

**Arguments**:

- `array` - Array to search through.
- `number` _number, optional_ - Number of items to randomly grab. Defaults to None.
- `preserve_keys` _bool, optional_ - Whether the keys should be preserved or not. Defaults to False.


**Raises**:

  ValueError


**Returns**:

  Array with the random values.

<a id="Arr.recursive_ksort"></a>

### recursive\_ksort

```python
@staticmethod
def recursive_ksort(array)
```

Recursively key-sort an array.

**Arguments**:

- `array` - The array to sort.


**Returns**:

  Sorted array.

<a id="Arr.set"></a>

### set

```python
@staticmethod
def set(array, keys, value)
```

Set key/value within an array, can set a key nested inside of a multidimensional array.

**Arguments**:

- `array` - The array containing the key this sets.
- `keys` _array_ - To set a key nested multiple levels deep pass an array
  specifying each key in order as a value.
- `Example` - array( 'lvl1', 'lvl2', 'lvl3' );
- `value` _Any_ - The value.


**Returns**:

  The manipulated array.

<a id="Arr.shape_filter"></a>

### shape\_filter

```python
@staticmethod
def shape_filter(array, shape)
```

Shapes, filtering it, an array to the specified expected set of required keys.

**Arguments**:

- `array` - The input array to shape.
- `shape` _array_ - The shape to update the array with. It should only define keys
  or arrays of keys. Keys that have no values will be set to null.
  To add the key only if set, prefix the key with ?, e.g. ?foo.


**Returns**:

  The manipulated array.

<a id="Arr.shuffle"></a>

### shuffle

```python
@staticmethod
def shuffle(array, seed=None)
```

Shuffle the given array and return the result.

**Arguments**:

- `array` - Array to shuffle.
- `seed` _Any, optional_ - The random number generator seed. Defaults to None.


**Returns**:

  The shuffled array.

<a id="Arr.sort_by_priority"></a>

### sort\_by\_priority

```python
@staticmethod
def sort_by_priority(array)
```

Sort based on Priority.

**Arguments**:

- `array` - A dict with priority keys.


**Returns**:

  Sorted dict.

<a id="Arr.sort_recursive"></a>

### sort\_recursive

```python
@staticmethod
def sort_recursive(array, descending=False)
```

Recursively sort an array by keys and values.

**Arguments**:

- `array` - Array to sort
- `descending` _bool, optional_ - Whether to sort in descending order or not. Defaults to False.


**Returns**:

  Sorted array.

<a id="Arr.sort_recursive_desc"></a>

### sort\_recursive\_desc

```python
@staticmethod
def sort_recursive_desc(array)
```

Recursively sort an array by keys and values in descending order.

**Arguments**:

- `array` - Array to sort


**Returns**:

  Sorted array.

<a id="Arr.stringify_keys"></a>

### stringify\_keys

```python
@staticmethod
def stringify_keys(input_array, prefix=None)
```

Stringifies the numeric keys of an array.

**Arguments**:

- `input_array` - Array to manipulate.
- `prefix` _str, optional_ - Prefix for array keys. Defaults to None.


**Returns**:

  Manipulated array.

<a id="Arr.strpos"></a>

### strpos

```python
@staticmethod
def strpos(haystack, needles, offset=0)
```

Behaves exactly like the native PHP's strpos(), but accepts an array of needles.

**Arguments**:

- `haystack` _str_ - String to search through.
- `needles` _str|array_ - Needle or needles to look for in the haystack.
- `offset` _int, optional_ - Starting position of search. Defaults to 0.


**Returns**:

- `_type_` - _description_

<a id="Arr.to_list"></a>

### to\_list

```python
@staticmethod
def to_list(list_items, sep=',')
```

Returns a list separated by the specified separator.

**Arguments**:

- `list_items` - Array of items.
- `sep` _str, optional_ - Separator. Defaults to ','.


**Returns**:

  The list separated by the specified separator or the original list if the list is empty.

<a id="Arr.undot"></a>

### undot

```python
@staticmethod
def undot(obj)
```

Convert a flatten "dot" notation array into an expanded array.

**Arguments**:

- `obj` - Array to undot.


**Returns**:

  Manipulated array.

<a id="Arr.usearch"></a>

### usearch

```python
@staticmethod
def usearch(needle, haystack, callback)
```

Searches an array using a callback and returns the index of the first match.

**Arguments**:

- `needle` _Any_ - The element to search in the array.
- `haystack` - The array to search.
- `callback` _function_ - A callback function with signature def x(needle, value, key) :bool
  that will be used to find the first match of needle in haystack.


**Returns**:

  Either the index of the first match or False if no match was found.

<a id="Arr.where"></a>

### where

```python
@staticmethod
def where(array, callback)
```

Filter the array using the given callback.

**Arguments**:

- `array` - Array to filter.
- `callback` _function_ - Function that returns True if the element should be retained, False otherwise.


**Returns**:

  The filtered array.

<a id="Arr.where_not_none"></a>

### where\_not\_none

```python
@staticmethod
def where_not_none(array)
```

Filter items where the value is not None.

**Arguments**:

- `array` - Array to filter.


**Returns**:

  The filtered array.

<a id="Arr.wrap"></a>

### wrap

```python
@staticmethod
def wrap(value)
```

If the given value is not a list, dict, or UserDict and not None, wrap it in one.

**Arguments**:

- `value` _Any_ - Value to wrap.


**Returns**:

  Wrapped value.

