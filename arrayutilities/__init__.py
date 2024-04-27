from collections import UserDict
from collections.abc import Iterable
from urllib.parse import urlencode
from urllib.parse import quote_plus
import re
import random
import time
import copy

class Arr:
    @staticmethod
    def accessible(value):
        """
        Determines if the given value is a list, dict, or UserDict.

        Args:
            value (Any): Value to determine if it is accessible.

        Returns:
            boolean: Whether the the value is a list, dict, or UserDict.
        """
        return isinstance(value, (list, dict, UserDict))

    @staticmethod
    def add(array, key, value):
        """
        Add an element to an array if it doesn't exist.

        Args:
            array: Array to manipulate.
            key: Key to use.
            value: Value to inject.

        Returns:
            Manipulated array
        """
        if Arr.get(array, key) is None:
            Arr.set(array, key, value)
        return array

    @staticmethod
    def add_prefixed_keys_to(array, recursive=False):
        """
        Duplicates any key not prefixed with '_' creating a prefixed duplicate one.

        Args:
            array: Array to manipulate.
            recursive (bool, optional): Whether to recursively change the array. Defaults to False.

        Returns:
            Manipulated array.
        """
        if not isinstance(array, dict):
            return array

        prefixed = {}
        for key, value in array.items():
            if recursive and isinstance(value, dict):
                value = Arr.add_prefixed_keys_to(value, True)
                array[key] = {**array[key], **value}

            if not key.startswith('_'):
                prefixed[f'_{key}'] = value

        return {**array, **prefixed}

    @staticmethod
    def add_unprefixed_keys_to(array, recursive=False):
        """
        Duplicates any key prefixed with '_' creating an un-prefixed duplicate one.

        Args:
            array: Array to manipulate.
            recursive (bool, optional): Whether to recursively change the array. Defaults to False.

        Returns:
            Manipulated array.
        """
        if not isinstance(array, dict):
            return array

        to_update = {}
        for key, value in array.items():
            # Handle recursion for nested dictionaries
            if recursive and isinstance(value, dict):
                value = Arr.add_unprefixed_keys_to(value, True)
                array[key] = value  # Update the original with the new value, which now includes unprefixed keys

            # Remove prefix and add the new key to to_update dictionary
            if key.startswith('_'):
                new_key = key[1:]
                to_update[new_key] = value

        # Update the array with unprefixed keys at the current level
        array.update(to_update)
        return array

    @staticmethod
    def array_visit_recursive(input_array, visitor):
        """
        Recursively visits all elements of an array applying the specified callback to each element key and value.

        Args:
            input_array: The input array whose nodes should be visited.
            visitor: A callback function that will be called on each array item; the callback will
                        receive the item key and value as input and should return an array that contains
                        the update key and value in the shape [ &lt;key&gt;, &lt;value&gt; ]. Returning a null
                        key will cause the element to be removed from the array.

        Returns:
            Manipulated array.
        """
        if not isinstance(input_array, dict):
            return input_array

        result = {}
        for key, value in input_array.items():
            if isinstance(value, dict):
                value = Arr.array_visit_recursive(value, visitor)
            updated_key, updated_value = visitor(key, value)
            if updated_key is not None:
                result[updated_key] = updated_value

        return result

    @staticmethod
    def collapse(array):
        """
        Collapse an array of arrays into a single array.

        Args:
            array: Array of arrays to collapse.

        Returns:
            Collapsed array.
        """
        return [item for sublist in array for item in sublist]

    @staticmethod
    def dot(array, prepend=''):
        """
        Flatten a multi-dimensional associative array with dots.

        Args:
            array: Array to manipulate.
            prepend (str, optional): Value to prepend to dict keys. Defaults to ''.

        Returns:
            Manipulated array.
        """
        result = {}
        for key, value in array.items():
            if isinstance(value, dict):
                result.update(Arr.dot(value, prepend + key + '.'))
            else:
                result[prepend + key] = value
        return result

    @staticmethod
    def exists(array, key):
        """
        Determine if the given key exists in the provided array.

        Args:
            array: Array to check.
            key: Key to look for.

        Returns:
            boolean: Whether or not the key exists.
        """
        if isinstance(key, float):
            key = str(key)
        return key in array

    @staticmethod
    def filter_prefixed(array, prefix):
        """
        Filters an associative array non-recursively, keeping only the values attached to keys starting with the specified prefix.

        Args:
            array: Array to filter.
            prefix (str|list): The prefix or prefixes of the keys to keep.

        Returns:
            Filtered array.
        """
        pattern = re.compile(f"^{prefix}")
        return {key: value for key, value in array.items() if pattern.search(key)}

    @staticmethod
    def first(array, callback=None, default=None):
        """
        Return the first element in an array passing a given truth test.

        Args:
            array: Array to look at.
            callback (Callable, optional): Callback function that returns a boolean of whether to match or not. Defaults to None.
            default (optional): Default value if no other value is found. Defaults to None.

        Returns:
            Found value or default.
        """
        if callback is None:
            return next(iter(array.values()), default)
        for key, value in array.items():
            if callback(value, key):
                return value
        return default

    @staticmethod
    def flatten(array, depth=float('inf')):
        """
        Flatten a multi-dimensional array into a single level.

        Args:
            array: Array to flatten.
            depth (number, optional): Number of nestings deep that should be flattened. Defaults to float('inf').

        Returns:
            Flattened array.
        """
        result = []
        for item in array:
            if isinstance(item, list) and depth >= 1:
                result.extend(Arr.flatten(item, depth - 1))
            else:
                result.append(item)
        return result

    @staticmethod
    def forget(array, keys):
        """
        Remove one or many array items from a given array using "dot" notation.

        Args:
            array: Array to manipulate.
            keys (str|array): Key or keys to remove.
        """
        keys = Arr.wrap(keys)
        for key in keys:
            parts = key.split('.')
            last_key = parts.pop()
            temp_array = array
            for part in parts:
                temp_array = temp_array.get(part, {})
            temp_array.pop(last_key, None)

    @staticmethod
    def get(array, keys, default=None):
        """
        Find a value inside of an array or object, including one nested a few levels deep.

        Args:
            array: Array to search
            keys (str|array): Key or keys to get.
            default (optional): Value to return if none found. Defaults to None.

        Returns:
            _type_: _description_
        """
        keys = Arr.wrap(keys)
        for key in keys:
            try:
                array = array[key]
            except (KeyError, TypeError, IndexError):
                return default
        return array

    @staticmethod
    def has(array, keys):
        """
        Check if an item or items exist in an array using "dot" notation.

        Args:
            array: Array to check.
            keys (str|array): The indexes to search; in order the function will look from the first to the last.

        Returns:
            boolean: Whether the key exists or not.
        """
        keys = Arr.wrap(keys)
        for key in keys:
            if key not in array:
                return False
        return True

    @staticmethod
    def insert_after_key(key, source_array, insert):
        """
        Insert an array after a specified key within another array.

        Args:
            key (str|number): The key of the array to insert after.
            source_array (array): The array to insert into.
            insert (Any): Value or array to insert.

        Returns:
            Manipulated array.
        """
        if not isinstance(insert, list):
            insert = [insert]
        index = next((i for i, k in enumerate(source_array) if k == key), len(source_array))
        return source_array[:index+1] + insert + source_array[index+1:]

    @staticmethod
    def insert_before_key(key, source_array, insert):
        """
        Insert an array before a specified key within another array.

        Args:
            key (str|number): The key of the array to insert before.
            source_array (array): The array to insert into.
            insert (Any): Value or array to insert.

        Returns:
            Manipulated array.
        """
        if not isinstance(insert, list):
            insert = [insert]
        index = next((i for i, k in enumerate(source_array) if k == key), len(source_array))
        return source_array[:index] + insert + source_array[index:]

    @staticmethod
    def is_dict(array):
        """
        Returns whether the array is a dict or not.

        Args:
            array (array): Array to check.

        Returns:
            boolean: Whether the array is a dict or not.
        """
        return isinstance(array, dict) or isinstance(array, UserDict)

    @staticmethod
    def is_list(array):
        """
        Returns whether the array is a list or not.

        Args:
            array (array): Array to check.

        Returns:
            boolean: Whether the array is a list or not.
        """
        return isinstance(array, list)

    @staticmethod
    def join(array, glue, final_glue=''):
        """
        Join all items using a string. The final items can use a separate glue string.

        Args:
            array: Array to join.
            glue (str): String to inject between elements.
            final_glue (str, optional): String to inject between the final two elements. Defaults to ''.

        Returns:
            str: Joined string.
        """
        if not array:
            return ''
        if final_glue:
            if len(array) > 1:
                return glue.join(map(str, array[:-1])) + final_glue + str(array[-1])
            return str(array[0])
        return glue.join(map(str, array))

    @staticmethod
    def last(array, callback=None, default=None):
        """
        Return the last element in an array passing a given truth test.

        Args:
            array: Array to look at.
            callback (Callable, optional): Callback function that returns a boolean of whether to match or not. Defaults to None.
            default (optional): Default value if no other value is found. Defaults to None.

        Returns:
            Found value or default.
        """
        if not array:
            return default

        if callback is None:
            return array[-1]

        for element in reversed(array):
            if callback(element):
                return element

        return default

    @staticmethod
    def list_to_array(value, sep=','):
        """
        Converts a list to an array filtering out empty string elements.

        Args:
            value (str|number|None): A string representing a list of values separated by the specified separator
                            or an array. If the list is a string (e.g. a CSV list) then it will urldecoded
                            before processing.
            sep (str, optional): The char(s) separating the list elements; will be ignored if the list is an array. Defaults to ','.

        Returns:
            Manipulated array.
        """
        if not value:
            return []
        if isinstance(value, str):
            value = value.split(sep)
        return [v.strip() for v in value if v.strip()]

    @staticmethod
    def merge_recursive(array1, array2):
        """
        Recursively merge two arrays preserving keys.

        Args:
            array1: Starting array.
            array2: Array to merge into the first.

        Returns:
            Merged array.
        """
        for key, value in array2.items():
            if isinstance(value, dict) and key in array1 and isinstance(array1[key], dict):
                array1[key] = Arr.merge_recursive(array1[key], value)
            else:
                array1[key] = value
        return array1

    @staticmethod
    def only(array, keys):
        """
        Get a subset of the items from the given array.

        Args:
            array: Array to search.
            keys (str|array): Key or keys to include in the final array.

        Returns:
            Array subset.
        """
        keys = Arr.wrap(keys)
        return {key: array[key] for key in keys if key in array}

    @staticmethod
    def prepend(array, value, key=None):
        """
        Push an item onto the beginning of an array.

        Args:
            array: Array to manipulate.
            value (Any): Value to prepend.
            key (string|number, optional): Key value for the prepended item. Defaults to None.

        Returns:
            Manipulated array.
        """
        if isinstance(array, list):
            array.insert(0, value)
        elif isinstance(array, dict):
            if key is None:
                array = {**{0: value}, **array}
            else:
                array = {key: value, **array}
        return array

    @staticmethod
    def pull(array, key, default=None):
        """
        Get a value from the array, and remove it.

        Args:
            array: Array to search and manipulate.
            key (str|number): Key to look for and fetch.
            default (Any, optional): Default value if none found. Defaults to None.

        Returns:
            Any: The found value or default.
        """
        value = Arr.get(array, key, default)
        Arr.forget(array, key)
        return value

    @staticmethod
    def query(data):
        """
        Convert the array into a query string.

        Args:
            data: Array to convert.

        Returns:
            str: URL query string.
        """
        def flatten_dict(d, parent_key='', sep='_'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}[{k}]" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        items.append((f"{new_key}[{i}]", item))
                else:
                    items.append((new_key, v))
            return dict(items)

        if isinstance(data, (list, tuple)):
            data = dict(enumerate(data))

        flat_data = flatten_dict(data)
        return '&'.join(k + '=' + quote_plus(str(v)) for k, v in flat_data.items())

    @staticmethod
    def random(array, number=None, preserve_keys=False):
        """
        Get one or a specified number of random values from an array.

        Args:
            array: Array to search through.
            number (number, optional): Number of items to randomly grab. Defaults to None.
            preserve_keys (bool, optional): Whether the keys should be preserved or not. Defaults to False.

        Raises:
            ValueError

        Returns:
            Array with the random values.
        """
        if number is None:
            return random.choice(list(array.values()))

        if number == 0:
            return []

        if number > len(array):
            raise ValueError(f"Requested {number} of elements but the array has only {len(array)} items.")

        keys = random.sample(list(array.keys()), number)

        if preserve_keys:
            return {key: array[key] for key in keys}

        return [array[key] for key in keys]

    @staticmethod
    def recursive_ksort(array):
        """
        Recursively key-sort an array.

        Args:
            array: The array to sort.

        Returns:
            Sorted array.
        """
        for key, value in array.items():
            if isinstance(value, dict):
                array[key] = Arr.recursive_ksort(value)
        return dict(sorted(array.items()))

    @staticmethod
    def set(array, keys, value):
        """
        Set key/value within an array, can set a key nested inside of a multidimensional array.

        Args:
            array: The array containing the key this sets.
            keys (array): To set a key nested multiple levels deep pass an array
                specifying each key in order as a value.
                Example: array( 'lvl1', 'lvl2', 'lvl3' );
            value (Any): 	The value.

        Returns:
            The manipulated array.
        """
        keys = Arr.wrap(keys)
        target = array
        for key in keys[:-1]:
            if key not in target or not isinstance(target[key], dict):
                target[key] = {}
            target = target[key]
        target[keys[-1]] = value
        return array

    @staticmethod
    def shape_filter(array, shape):
        """
        Shapes, filtering it, an array to the specified expected set of required keys.

        Args:
            array: The input array to shape.
            shape (array): The shape to update the array with. It should only define keys
                or arrays of keys. Keys that have no values will be set to null.
                To add the key only if set, prefix the key with ?, e.g. ?foo.

        Returns:
            The manipulated array.
        """
        result = {}
        for shape_key, subshape in shape.items():
            if isinstance(subshape, dict):
                result[shape_key] = Arr.shape_filter(array.get(shape_key, {}), subshape)
            elif shape_key in array:
                result[shape_key] = array[shape_key]
        return result

    @staticmethod
    def shuffle(array, seed=None):
        """
        Shuffle the given array and return the result.

        Args:
            array: Array to shuffle.
            seed (Any, optional): The random number generator seed. Defaults to None.

        Returns:
            The shuffled array.
        """
        array = copy.copy(array)
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()  # Use system time as seed
        random.shuffle(array)
        return array

    @staticmethod
    def sort_by_priority(array):
        """
        Sort based on Priority.

        Args:
            array: A dict with priority keys.

        Returns:
            Sorted dict.
        """
        return sorted(array, key=lambda x: x.get('priority', 0))

    @staticmethod
    def sort_recursive(array, descending=False):
        """
        Recursively sort an array by keys and values.

        Args:
            array: Array to sort
            descending (bool, optional): Whether to sort in descending order or not. Defaults to False.

        Returns:
            Sorted array.
        """
        array = copy.copy(array)
        for key, value in array.items():
            if isinstance(value, dict):
                array[key] = Arr.sort_recursive(value, descending)
        sorted_items = sorted(array.items(), key=lambda x: str(x[1]), reverse=descending)
        if not descending:
            sorted_items = sorted(sorted_items, key=lambda x: x[0])
        return dict(sorted_items)

    @staticmethod
    def sort_recursive_desc(array):
        """
        Recursively sort an array by keys and values in descending order.

        Args:
            array: Array to sort

        Returns:
            Sorted array.
        """
        return Arr.sort_recursive(array, True)

    @staticmethod
    def stringify_keys(input_array, prefix=None):
        """
        Stringifies the numeric keys of an array.

        Args:
            input_array: Array to manipulate.
            prefix (str, optional): Prefix for array keys. Defaults to None.

        Returns:
            Manipulated array.
        """
        prefix = '' if prefix is None else f'{prefix}'
        return {f'{prefix}{key}': value for key, value in input_array.items()}

    @staticmethod
    def strpos(haystack, needles, offset=0):
        """
        Behaves exactly like the native PHP's strpos(), but accepts an array of needles.

        Args:
            haystack (str): String to search through.
            needles (str|array): Needle or needles to look for in the haystack.
            offset (int, optional): Starting position of search. Defaults to 0.

        Returns:
            _type_: _description_
        """
        needles = Arr.wrap(needles)
        min_position = len(haystack)  # Initialize with a value larger than any possible position
        for needle in needles:
            position = haystack.find(needle, offset)
            if position != -1 and position < min_position:
                min_position = position
        return min_position if min_position != len(haystack) else False

    @staticmethod
    def to_list(list_items, sep=','):
        """
        Returns a list separated by the specified separator.

        Args:
            list_items: Array of items.
            sep (str, optional): Separator. Defaults to ','.

        Returns:
            The list separated by the specified separator or the original list if the list is empty.
        """
        if not list_items:
            return list_items
        if isinstance(list_items, list):
            return sep.join(map(str, list_items))
        return str(list_items)

    @staticmethod
    def undot(obj):
        """
        Convert a flatten "dot" notation array into an expanded array.

        Args:
            obj: Array to undot.

        Returns:
            Manipulated array.
        """
        result_dict = {}

        def recursively_undot(obj, current):
            for key, value in obj.items():
                parts = key.split('.')
                sub_dict = current
                for part in parts[:-1]:
                    if part not in sub_dict or not isinstance(sub_dict[part], dict):
                        sub_dict[part] = {}
                    sub_dict = sub_dict[part]
                final_key = parts[-1]
                if isinstance(value, dict):
                    if final_key not in sub_dict:
                        sub_dict[final_key] = {}
                    recursively_undot(value, sub_dict[final_key])
                else:
                    sub_dict[final_key] = value

        recursively_undot(obj, result_dict)
        return result_dict

    @staticmethod
    def usearch(needle, haystack, callback):
        """
        Searches an array using a callback and returns the index of the first match.

        Args:
            needle (Any): The element to search in the array.
            haystack: The array to search.
            callback (function): A callback function with signature def x(needle, value, key) :bool
                that will be used to find the first match of needle in haystack.

        Returns:
            Either the index of the first match or False if no match was found.
        """
        for key, value in haystack.items():
            if callback(needle, value, key):
                return key
        return False

    @staticmethod
    def where(array, callback):
        """
        Filter the array using the given callback.

        Args:
            array: Array to filter.
            callback (function): Function that returns True if the element should be retained, False otherwise.

        Returns:
            The filtered array.
        """
        return {k: v for k, v in array.items() if callback(v, k)}

    @staticmethod
    def where_not_none(array):
        """
        Filter items where the value is not None.

        Args:
            array: Array to filter.

        Returns:
            The filtered array.
        """
        return {k: v for k, v in array.items() if v is not None}

    @staticmethod
    def wrap(value):
        """
        If the given value is not a list, dict, or UserDict and not None, wrap it in one.

        Args:
            value (Any): Value to wrap.

        Returns:
            Wrapped value.
        """
        if value is None:
            return []
        return value if isinstance(value, list) or isinstance(value, dict) or isinstance(value, UserDict) else [value]
