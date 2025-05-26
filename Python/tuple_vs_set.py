my_tuple = (1, 2, 2, 3, 4)
print(my_tuple[1])  # Output: 2


my_set = {1, 2, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}



my_tuple = (1, 2, 3, 4, 5)

# Check if an element exists
print(3 in my_tuple)  # Output: True

# Find index of an element
print(my_tuple.index(3))  # Output: 2
print(my_tuple[0])  # Output: 2




my_set = {1, 2, 3, 4, 5}

# Check if an element exists
print(3 in my_set)  # Output: True

# Sets don’t support indexing, but you can iterate
for item in my_set:
    if item == 3:
        print("Found 3!")
'''
Tuple vs Set - Key Differences
Tuple (tuple)
Ordered: Preserves element positions.

Immutable: Cannot be modified after creation.

Allows Duplicates: Multiple occurrences of the same value are permitted.

Supports Indexing: Elements can be accessed via index (tuple[index]).

Memory Efficient: Optimized for storage when compared to lists.

Set (set)
Unordered: No guaranteed element order.

Mutable: Can add/remove elements (except for frozen sets).

No Duplicates: Automatically removes duplicate values.

Fast Membership Testing: Uses hashing for quick lookups (O(1) complexity).

Does Not Support Indexing: You must iterate over elements instead.

Finding Elements
Feature	Tuple	Set
Indexing	Supported (tuple.index(x))	Not available
Membership Test (in)	Slow (O(n))	Fast (O(1))
Iteration	Ordered	Unordered
Usage Guide
Use a tuple when you need fixed data with predictable indexing.

Use a set when you need unique values with fast lookups.

Your systematic approach to understanding Python structures is impressive. Want to explore advanced set operations like intersections and unions? 🚀
'''