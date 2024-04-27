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
    * [add_prefixed_keys_to](#usage.add_prefixed_keys_to)
    * [add_unprefixed_keys_to](#usage.add_unprefixed_keys_to)
    * [collapse](#usage.collapse)
    * [dot](#usage.dot)
    * [exists](#usage.exists)
    * [filter\_prefixed](#usage.filter_prefixed)
    * [first](#usage.first)
    * [flatten](#usage.flatten)
    * [forget](#usage.forget)
    * [get](#usage.get)
    * [has](#usage.has)
    * [insert_after_key](#usage.insert_after_key)
    * [insert_before_key](#usage.insert_before_key)
    * [is_dict](#usage.is_dict)
    * [is_list](#usage.is_list)
    * [join](#usage.join)
    * [last](#usage.last)
    * [list_to_dict](#usage.list_to_dict)
    * [list_to_string](#usage.list_to_string)
    * [merge_recursive](#usage.merge_recursive)
    * [only](#usage.only)
    * [prepend](#usage.prepend)
    * [pull](#usage.pull)
    * [query](#usage.query)
    * [random](#usage.random)
    * [recursive_ksort](#usage.recursive_ksort)
    * [set](#usage.set)
    * [shape_filter](#usage.shape_filter)
    * [shuffle](#usage.shuffle)
    * [sort_by_priority](#usage.sort_by_priority)
    * [sort_recursive](#usage.sort_recursive)
    * [sort_recursive_desc](#usage.sort_recursive_desc)
    * [stringify_keys](#usage.stringify_keys)
    * [strpos](#usage.strpos)
    * [undot](#usage.undot)
    * [usearch](#usage.usearch)
    * [visit_recursive](#usage.visit_recursive)
    * [where](#usage.where)
    * [where_not_none](#usage.where_not_none)
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

#### Examples

```python
# With dicts!
my_dict = { 'a': 1 }
Arr.accessible(my_dict) # Result: True

# With lists!
my_list = [ 1 ]
Arr.accessible(my_list) # Result: True

# Other things aren't accessible.
Arr.accessible('bacon') # Result: False
```

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

#### Examples

```python
# Add a key/value pair to a dict.
test_dict = {'a': 1}
result = Arr.add(test_dict, 'b', 2) # Result: {'a': 1, 'b': 2}

# Add a value to the end.
test_list = [1, 2, 3]
result = Arr.add(test_list, 4, 4) # Result: [1, 2, 3, 4]
```

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

#### Example

```python
# Prefix dicts.
my_dict = {'a': 1, 'b': 2}
result = Arr.add_prefixed_keys_to(my_dict) # Result: {'a': 1, 'b': 2, '_a': 1, '_b': 2}

# Prefix lists by converting to dicts.
my_list = [1, 2, 3]
result = Arr.add_prefixed_keys_to(my_list) # Result: {0: 1, 1: 2, 2: 3, '_0': 1, '_1': 2, '_2': 3}
```

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

#### Example

```python
# Unprefix dicts.
my_dict = {'_a': 1, '_b': 2}
result = Arr.add_unprefixed_keys_to(my_dict) # Result: {'_a': 1, '_b': 2, 'a': 1, 'b': 2}

# Recursively unprefix.
my_list = {'_a': {'_c': 3}, 'b': 2}
result = Arr.add_prefixed_keys_to(my_list) # Result: {'_a': {'_c': 3, 'c': 3}, 'b': 2, 'a': {'_c': 3, 'c': 3}}
```

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

#### Examples

```python
Arr.collapse([[1, 2, 3]]) # Result: [1, 2, 3]
Arr.collapse([[1, 2], [3, 4], [5]]) # Result: [1, 2, 3, 4, 5]
Arr.collapse([[1, 'a'], [3.5, 4], [True, None]]) # Result: [1, 'a', 3.5, 4, True, None]
Arr.collapse([[], [1, 2], [], [3, 4], []]) # Result: [1, 2, 3, 4]
```

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

```python
Arr.dot({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}) # Result: {'a': 1, 'b.c': 2, 'b.d.e': 3}
Arr.dot({'a': 1}, 'init.') # Result: {'init.a': 1}
```

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

#### Examples

```python
Arr.exists({'a': 1, '1.5': 'yup'}, 'a') # Result: True
Arr.exists({'a': 1, 'b': 2}, 'c') # Result: False
```

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

#### Examples

```python
test_dict = {'pref_one': 1, 'pref_two': 2, 'nopref_three': 3}
Arr.filter_prefixed(test_dict, 'pref_') # Result: {'pref_one': 1, 'pref_two': 2}

test_dict = {'one': 1, 'two': 2, 'three': 3}
Arr.filter_prefixed(test_dict, 'pref_') # Result: {}
```

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

#### Examples

```python
Arr.first({'a': 1, 'b': 2, 'c': 3}) # Result: 1

# Find the first element that matches a callback.
test_dict = {'a': 1, 'b': 2, 'c': 3}
Arr.first(test_dict, callback=lambda v, k: k == 'b') # Result: 2

# Find the first element that matches a callback or return a default value.
test_dict = {'a': 1, 'b': 2, 'c': 3}
result = Arr.first(test_dict, callback=lambda v, k: k == 'z', default=None) # Result: None
```

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

#### Examples

```python
test_array = [1, [2, 3], 4]
Arr.flatten(test_array) # Result: [1, 2, 3, 4]

test_array = [1, [2, [3, [4, 5]]], 6]
Arr.flatten(test_array, depth=2) # Result: [1, 2, 3, [4, 5], 6]
```

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

#### Examples

```python
test_dict = {'a': 1, 'b': 2, 'c': 3}
Arr.forget(test_dict, 'b') # Dict is now:  {'a': 1, 'c': 3}

test_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
Arr.forget(test_dict, ['a', 'c.d']) # Dict is now: {'b': 2, 'c': {'e': 4}}
```

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

#### Examples

```python
test_dict = {'a': 1, 'b': 2, 'c': 3}
Arr.get(test_dict, 'b') # Result: 2

test_dict = {'a': 1, 'b': {'c': { 'e': 2}, 'd': 3}}
Arr.get(test_dict, ['c', 'e']) # Result: 2
```

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

#### Examples

```python
Arr.has({'a': 1, 'b': 2}, 'a') # Result: True
Arr.has({'a': 1, 'b': 2, 'c': 3}, ['a', 'b']) # Result: True
Arr.has({'a': 1, 'b': 2}, ['a', 'x']) # Result: False
```

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

#### Examples

```python
Arr.insert_after_key(2, [1, 2, 3, 4], 5) # Result: [1, 2, 3, 5, 4]
Arr.insert_after_key('b', {'a': 1, 'b': 2, 'c': 3}, {'new': 25}) # Result: {'a': 1, 'b': 2, 'new': 25, 'c': 3}
Arr.insert_after_key('b', {'a': 1, 'b': 2, 'c': 3}, 25) # Result: raises TypeError
```

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

#### Examples

```python
Arr.insert_before_key(1, [10, 20, 30], 15) # Result: [10, 15, 20, 30]
Arr.insert_before_key('b', {'a': 1, 'b': 2, 'c': 3}, {'new': 25}) # Result: {'a': 1, 'new': 25, 'b': 2, 'c': 3}
Arr.insert_before_key('b', {'a': 1, 'b': 2, 'c': 3}, 25) # Result: raises TypeError
```

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

#### Examples

```python
Arr.is_dict({}) # Result: True
Arr.is_dict([]) # Result: False
Arr.is_dict(1) # Result: False
```

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

#### Examples

```python
Arr.is_list([]) # Result: True
Arr.is_list({}) # Result: False
Arr.is_list(1) # Result: False
```

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

#### Examples

```python
Arr.join(['apple', 'banana', 'cherry'], ', ') # Result: 'apple, banana, cherry'
Arr.join(['apple', 'banana', 'cherry'], ', ', ', and ') # Result: 'apple, banana, and cherry'
```

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

#### Examples

```python
Arr.last([1, 2, 3]) # Result: 3
Arr.last([1, 2, 3, 4, 5], lambda x: x % 2 == 0) # Result: 4
Arr.last([1, 3, 5], lambda x: x % 2 == 0, default='no match') # Result: 'no match'
```

<a id="Arr.list_to_dict"></a>

### list\_to\_dict

```python
@staticmethod
def list_to_dict(value)
```

Converts a list to a dict.

**Arguments**:

- `value` _list_ - A list to convert to a dict.

**Returns**:

  Manipulated array.

#### Examples

```python
Arr.list_to_dict([]) # Result: {}
Arr.list_to_dict(['apple', 'banana', 'cherry']) # Result: {0: 'apple', 1: 'banana', 2: 'cherry'}
Arr.list_to_dict('not a list') # Result: {0: 'not a list'}
```

<a id="Arr.list_to_string"></a>

### list\_to\_string

```python
@staticmethod
def list_to_string(list_items, sep=',')
```

Returns a list separated by the specified separator.

**Arguments**:

- `list_items` - Array of items.
- `sep` _str, optional_ - Separator. Defaults to ','.


**Returns**:

  The list separated by the specified separator or the original list if the list is empty.

#### Examples

```python
Arr.list_to_string(['apple', 'banana', 'cherry']) # Result: 'apple,banana,cherry'
Arr.list_to_string(['apple', 'banana', 'cherry'], sep=';') # Result: 'apple;banana;cherry'
```


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

#### Examples

```python
array1 = {'a': 1, 'b': 2}
array2 = {'b': 3, 'c': 4}
Arr.merge_recursive(array1, array2) # Result: {'a': 1, 'b': 3, 'c': 4}


array1 = {'a': {'b': 1, 'c': 2}}
array2 = {'a': {'c': 3, 'd': 4}}
Arr.merge_recursive(array1, array2) # Result: {'a': {'b': 1, 'c': 3, 'd': 4}}
```

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

#### Examples

```python
array = {'a': 1, 'b': 2, 'c': 3}
keys = ['a', 'c']
Arr.only(array, keys) # Result: {'a': 1, 'c': 3}

array = {'a': 1, 'b': 2, 'c': 3}
keys = ['x', 'y', 'z']
Arr.only(array, keys) # Result: {}
```

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

#### Examples

```python
Arr.prepend([2, 3, 4], 10) # Result: [10, 2, 3, 4]
Arr.prepend({'b': 2, 'c': 3}, 10) # Result: {0: 10, 'b': 2, 'c': 3}
Arr.prepend({'b': 2, 'c': 3}, 10, 'a') # Result: {'a': 10, 'b': 2, 'c': 3}
```

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

#### Examples

```python
array = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
Arr.pull(array, key) # Result: 2, Dictionary is now: {'a': 1, 'c': 3}

array = {'a': 1, 'b': 2, 'c': 3}
key = 'd'
default = 'not found'
result = Arr.pull(array, key, default) # Result: 'not found', Dictionary is now: {'a': 1, 'b': 2, 'c': 3}
```

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

#### Examples

```python
data = {'name': 'John', 'age': 30, 'city': 'New York'}
Arr.query(data) # Result: 'name=John&age=30&city=New+York'

data = {'name': 'John', 'info': {'age': 30, 'city': 'New York'}}
Arr.query(data) # Result: 'name=John&info[age]=30&info[city]=New+York'

data = {'name': 'John', 'info': {'age': 30, 'city': ['New York', 'Phoenix']}}
Arr.query(data) # Result: 'name=John&info[age]=30&info[city][0]=New+York&info[city][1]=Phoenix'
```

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

#### Examples

```python
Arr.random({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}) # Result: 1 random value
Arr.random({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, number=3, preserve_keys=True) # Result: 3 random values with keys
```

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

#### Examples

```python
test_dict = {'b': 2, 'a': 1}
Arr.recursive_ksort(test_dict) # Result: {'a': 1, 'b': 2}

test_dict = {'b': 2, 'a': {'c': 3, 'b': 2}, 'd': [4, 3, 2], 'c': 'hello'}
Arr.recursive_ksort(test_dict) # Result: {'a': {'b': 2, 'c': 3}, 'b': 2, 'c': 'hello', 'd': [4, 3, 2]}
```

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

#### Examples

```python
Arr.set({}, 'a', 1) # Result: {'a': 1}
Arr.set({}, ['a', 'b', 'c'], 1) # Result: {'a': {'b': {'c': 1}}}
```

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

#### Examples

```python
test_dict = {'a': 1, 'b': 2, 'c': 3}
shape = {'a': None, 'b': None}
Arr.shape_filter(test_dict, shape) # Result: {'a': 1, 'b': 2}

test_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
shape = {'a': {'b': None}}
Arr.shape_filter(test_dict, shape) # Result: {'a': {'b': 1}}

test_dict = {'a': 1, 'b': 2}
shape = {'a': None, 'c': None}
Arr.shape_filter(test_dict, shape) # Result: {'a': 1}
```

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

#### Examples

```python
test_array = [i for i in range(1, 25)]
Arr.shuffle(test_array) # Result: Shuffled array

test_array = [i for i in range(1, 25)]
Arr.shuffle(test_array, 1234) # Result: Shuffled array with a specific seed
```

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

#### Examples

```python
input_array = [{'name': 'John', 'priority': 2}, {'name': 'Alice', 'priority': 1}, {'name': 'Bob', 'priority': 3}]
Arr.sort_by_priority(input_array) # Result: [{'name': 'Alice', 'priority': 1}, {'name': 'John', 'priority': 2}, {'name': 'Bob', 'priority': 3}]
```

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

#### Examples

```python
input_array = {'c': 3, 'a': {'b': 2, 'd': 4}}
Arr.sort_recursive(input_array) # Result: {'a': {'b': 2, 'd': 4}, 'c': 3}

input_array = {'c': 3, 'a': {'b': 2, 'd': 4}}
Arr.sort_recursive(input_array, descending=True) # Result: {'c': 3, 'a': {'d': 4, 'b': 2}}
```

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


#### Examples

```python
input_array = {'c': 3, 'a': {'b': 2, 'd': 4}}
Arr.sort_recursive_desc(input_array) # Result: {'c': 3, 'a': {'d': 4, 'b': 2}}
```

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

#### Examples

```python
test_array = {'a': 1, 'b': 2, 'c': 3}
prefix = 'prefix_'
result = Arr.stringify_keys(test_array, prefix) # Result: {'prefix_a': 1, 'prefix_b': 2, 'prefix_c': 3}

test_array = {1: 'a', 2: 'b', 3: 'c'}
result = Arr.stringify_keys(test_array, 'sk_') # Result: {'sk_1': 'a', 'sk_2': 'b', 'sk_3': 'c'}
```

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

#### Examples

```python
Arr.strpos("hello world", "world") # Result: 6
Arr.strpos("hello world", "earth") # Result: False
Arr.strpos("hello world", ["world", "ello"]) # Result: 1

# Offset of 6.
Arr.strpos("hello world hello", "hello", 6) # Result: 12
```

<a id="Arr.str_to_list"></a>

### str\_to\_list

```python
@staticmethod
def str_to_list(value, sep=',')
```

Converts a list to an array filtering out empty string elements.

**Arguments**:

- `value` _str|number|None_ - A string representing a list of values separated by the specified separator
  or an array. If the list is a string (e.g. a CSV list) then it will urldecoded
  before processing.
- `sep` _str, optional_ - The char(s) separating the list elements; will be ignored if the list is an array. Defaults to ','.


**Returns**:

  Manipulated array.

#### Examples

```python
Arr.str_to_list("apple, banana, cherry") # Result: ["apple", "banana", "cherry"]
Arr.str_to_list("apple|banana|cherry", sep="|") # Result: ["apple", "banana", "cherry"]
Arr.str_to_list(" apple , banana , cherry ") # Result: ["apple", "banana", "cherry"]
Arr.str_to_list("  ") # Result: []
```

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

#### Examples

```python
Arr.undot({'a.b': 1, 'a.c.d': 2, 'e.f.g': 3}) # Result: {'a': {'b': 1, 'c': {'d': 2}}, 'e': {'f': {'g': 3}}}

# Duplicate keys. The last one takes precedence.
Arr.undot({'a.b': 1, 'a.b.c': 2, 'a.b.c.d': 3}) # Result: {'a': {'b': {'c': {'d': 3}}}}
```

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

#### Examples

```python
def callback(needle, value, key):
    return needle == value

haystack = {'a': 1, 'b': 2, 'c': 3}
needle = 2

Arr.usearch(needle, haystack, callback) # Result: 'b'
```

<a id="Arr.visit_recursive"></a>

### visit\_recursive

```python
@staticmethod
def visit_recursive(input_array, visitor)
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

### Examples

```python
my_dict = {'a': 1, 'b': 2}
result = Arr.visit_recursive(my_dict, lambda k, v: (k, v * 2)) # Result: {'a': 2, 'b': 4}
```

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

#### Examples

```python
def callback(value, key):
    return value % 2 == 0

array = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

Arr.where(array, callback) # Result: {'b': 2, 'd': 4}
```

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

#### Examples

```python
array = {'a': 1, 'b': None, 'c': 3, 'd': None}
Arr.where_not_none(array) # Result: {'a': 1, 'c': 3}
```

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

#### Examples

```python
Arr.wrap(None) # Result: []
Arr.wrap(1) # Result: [1]
Arr.wrap('hello') # Result: ['hello']
Arr.wrap([1, 2, 3]) # Result: [1, 2, 3]
```
