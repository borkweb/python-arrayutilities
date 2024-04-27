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
        return isinstance(value, (list, dict, UserDict))

    @staticmethod
    def add(array, key, value):
        if Arr.get(array, key) is None:
            Arr.set(array, key, value)
        return array

    @staticmethod
    def add_prefixed_keys_to(array, recursive=False):
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
        return [item for sublist in array for item in sublist]

    @staticmethod
    def dot(array, prepend=''):
        result = {}
        for key, value in array.items():
            if isinstance(value, dict):
                result.update(Arr.dot(value, prepend + key + '.'))
            else:
                result[prepend + key] = value
        return result

    @staticmethod
    def exists(array, key):
        if isinstance(key, float):
            key = str(key)
        return key in array

    @staticmethod
    def filter_prefixed(array, prefix):
        pattern = re.compile(f"^{prefix}")
        return {key: value for key, value in array.items() if pattern.search(key)}

    @staticmethod
    def first(array, callback=None, default=None):
        if callback is None:
            return next(iter(array.values()), default)
        for key, value in array.items():
            if callback(value, key):
                return value
        return default

    @staticmethod
    def flatten(array, depth=float('inf')):
        result = []
        for item in array:
            if isinstance(item, list) and depth >= 1:
                result.extend(Arr.flatten(item, depth - 1))
            else:
                result.append(item)
        return result

    @staticmethod
    def forget(array, keys):
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
        keys = Arr.wrap(keys)
        for key in keys:
            try:
                array = array[key]
            except (KeyError, TypeError, IndexError):
                return default
        return array

    @staticmethod
    def has(array, keys):
        keys = Arr.wrap(keys)
        for key in keys:
            if key not in array:
                return False
        return True

    @staticmethod
    def insert_after_key(key, source_array, insert):
        if not isinstance(insert, list):
            insert = [insert]
        index = next((i for i, k in enumerate(source_array) if k == key), len(source_array))
        return source_array[:index+1] + insert + source_array[index+1:]

    @staticmethod
    def insert_before_key(key, source_array, insert):
        if not isinstance(insert, list):
            insert = [insert]
        index = next((i for i, k in enumerate(source_array) if k == key), len(source_array))
        return source_array[:index] + insert + source_array[index:]

    @staticmethod
    def is_assoc(array):
        return isinstance(array, dict)

    @staticmethod
    def is_list(array):
        return isinstance(array, list)

    @staticmethod
    def join(array, glue, final_glue=''):
        if not array:
            return ''
        if final_glue:
            if len(array) > 1:
                return glue.join(map(str, array[:-1])) + final_glue + str(array[-1])
            return str(array[0])
        return glue.join(map(str, array))

    @staticmethod
    def last(array, callback=None, default=None):
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
        if not value:
            return []
        if isinstance(value, str):
            value = value.split(sep)
        return [v.strip() for v in value if v.strip()]

    @staticmethod
    def merge_recursive(array1, array2):
        for key, value in array2.items():
            if isinstance(value, dict) and key in array1 and isinstance(array1[key], dict):
                array1[key] = Arr.merge_recursive(array1[key], value)
            else:
                array1[key] = value
        return array1

    @staticmethod
    def only(array, keys):
        keys = Arr.wrap(keys)
        return {key: array[key] for key in keys if key in array}

    @staticmethod
    def prepend(array, value, key=None):
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
        value = Arr.get(array, key, default)
        Arr.forget(array, key)
        return value

    @staticmethod
    def query(data):
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
        for key, value in array.items():
            if isinstance(value, dict):
                array[key] = Arr.recursive_ksort(value)
        return dict(sorted(array.items()))

    @staticmethod
    def set(array, keys, value):
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
        result = {}
        for shape_key, subshape in shape.items():
            if isinstance(subshape, dict):
                result[shape_key] = Arr.shape_filter(array.get(shape_key, {}), subshape)
            elif shape_key in array:
                result[shape_key] = array[shape_key]
        return result

    @staticmethod
    def shuffle(array, seed=None):
        array = copy.copy(array)
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()  # Use system time as seed
        random.shuffle(array)
        return array

    @staticmethod
    def sort_by_priority(array):
        return sorted(array, key=lambda x: x.get('priority', 0))

    @staticmethod
    def sort_recursive(array, options=None, descending=False):
        for key, value in array.items():
            if isinstance(value, dict):
                array[key] = Arr.sort_recursive(value, options, descending)
        sorted_items = sorted(array.items(), key=lambda x: str(x[1]), reverse=descending)
        if not descending:
            sorted_items = sorted(sorted_items, key=lambda x: x[0])
        return dict(sorted_items)

    @staticmethod
    def sort_recursive_desc(array, options=None):
        return Arr.sort_recursive(array, options, True)

    @staticmethod
    def stringify_keys(input_array, prefix=None):
        prefix = '' if prefix is None else f'{prefix}'
        return {f'{prefix}{key}': value for key, value in input_array.items()}

    @staticmethod
    def strpos(haystack, needles, offset=0):
        needles = Arr.wrap(needles)
        min_position = len(haystack)  # Initialize with a value larger than any possible position
        for needle in needles:
            position = haystack.find(needle, offset)
            if position != -1 and position < min_position:
                min_position = position
        return min_position if min_position != len(haystack) else False

    @staticmethod
    def to_list(list_items, sep=','):
        if not list_items:
            return list_items
        if isinstance(list_items, list):
            return sep.join(map(str, list_items))
        return str(list_items)

    @staticmethod
    def undot(obj):
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
        for key, value in haystack.items():
            if callback(needle, value, key):
                return key
        return False

    @staticmethod
    def where(array, callback):
        return {k: v for k, v in array.items() if callback(v, k)}

    @staticmethod
    def where_not_none(array):
        return {k: v for k, v in array.items() if v is not None}

    @staticmethod
    def wrap(value):
        if value is None:
            return []
        return value if isinstance(value, list) else [value]
