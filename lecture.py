import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

##############
# Algorithms #
##############

# An algorithm is a set of instructions for solving a problem
# Used to solve all types of problems e.g. sorting data or searching for information
# Being able to write efficient algorithms is key to becoming a great programmer


# Looking at Time Complexity

def linear_loop(a_list):
    for item in a_list:
        print(item)

def quadratic_loop(a_list):
    for item_a in a_list:
        for item_b in a_list:
            print(item_a, item_b)


nums = [1, 2, 3, 4]

linear_loop(nums)
line_break()
quadratic_loop(nums)

line_break()

# Space Complexity

# Swapping Function - a function that will take in a list, and then 2 indices to swap

def swap_out_of_place(a_list, index_a, index_b): # O(n) Space Complexity
    # Create a new list that is a copy of a_list
    b_list = a_list[:]
    # Assign the index values
    b_list[index_a] = a_list[index_b]
    b_list[index_b] = a_list[index_a]
    # Return the new list with swapped values
    return b_list

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

swapped = swap_out_of_place(colors, 1, 4)
print(colors)
print(swapped)

line_break()

def swap_in_place(a_list, index_a, index_b): # O(1) Space Complexity
    temp = a_list[index_a]
    a_list[index_a] = a_list[index_b]
    a_list[index_b] = temp
    return a_list

subjects = ['math', 'science', 'history', 'english', 'language', 'computer']

swapped = swap_in_place(subjects, 0,1)
print(subjects)
print(swapped)

# Multiple Item Assignment

def swap(a_list, a, b):
    a_list[a], a_list[b] = a_list[b], a_list[a]
    # return a_list

nba_teams = ['Wolves', 'Mavs', 'Nuggets', 'Celtics', 'Knicks', 'Pacers', 'Thunder', 'Cavs']

swap(nba_teams, 1, 5)
print(nba_teams)

line_break()


# builtin sorted() vs. list.sort()

print('Sorted Function:') # O(n) - Out Of Place - Linear Space Complexity
continents = ['North America', 'Australia', 'South America', 'Europe', 'Asia', 'Africa', 'Antarctica']

print('Before:', continents)
sorted_return = sorted(continents)
print('After:', continents)
print('Return Value:', sorted_return)

print()

print('list.sort:')
continents = ['North America', 'Australia', 'South America', 'Europe', 'Asia', 'Africa', 'Antarctica']

print('Before:', continents)
sort_return = continents.sort()
print('After:', continents)
print('Return Value:', sort_return)


line_break()


# Write a function that will reverse a list in place
def reverse_list(lst):
    left = 0 # Start at the far left end of the list - index 0
    right = len(lst) - 1 # Start at the far right end of the list
    while left < right: # While the left pointer is to the left of the right pointer
        lst[left], lst[right] = lst[right], lst[left] # Swap the values at the left and right index
        left += 1 # Move the left pointer to the right 1 spot
        right -= 1 # Move the right pointer to the left 1 spot
    # Once the left is right of right, we can return the original list (now reversed)
    return lst


# Out of place
def reverse_out(lst):
    reversed_list = []
    for idx in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[idx])
    return reversed_list

line_break()
line_break()

from random import randint

unsorted_list = [randint(1,50) for _ in range(10)]


# Bubble Sort - 
# Worst Case - O(n**2) Time Complexity
# Best Case - O(n) Time Complexity
# Space Complexity - O(1) Constant

print('Bubble Sort: ')

def bubble_sort(lst):
    # when we first start, set up a variable (swapped) to true to begin the while loop
    swapped = True
    i = 1
    while swapped:
        # Begin the loop with the assumption (hope?) that we don't have to make any swaps (aka the list already sorted)
        swapped = False
        # Start at the 0-index and loop to the second to last item (because we check the item and the item to its right)
        for idx in range(len(lst)-i):
            # Check if the value at idx is greater than the value to its right (idx+1)
            if lst[idx] > lst[idx+1]:
                # Swap those values
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                # Because we made a swap, set the flag to say we did in fact swap
                swapped = True
        i += 1
    # Once we loop through without having to make a swap, out list is sorted and we can retun
    return lst

print(unsorted_list)
bubble_sort(unsorted_list)
print(unsorted_list)

line_break()

# Merge Sort - 
# Worst Case - O(n log n) Time Complexity
# Best Case - O(n log n) Time Complexity
# Space Complexity - O(n) Linear

print('Merge Sort:')
unsorted_list = [randint(1,50) for _ in range(8)]

def merge_sort(lst):
    # Check if our list can be split in half
    if len(lst) > 1:
        # Find the midway point
        mid = len(lst) // 2
        # Split the list into a left and right
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Call merge_sort on left half
        merge_sort(left_half)
        # Call merge_sort on right half
        merge_sort(right_half)

        # Merge the left and right half lists back into the original list
        # index pointers for the three lists
        l = 0 # pointer for left half
        r = 0 # pointer for right half
        m = 0 # pointer for main list (lst)

        # While the left and right pointers are still pointing at valid indices
        while l < len(left_half) and r < len(right_half):
            # Compare the value at left pointer vs right pointer 
            if left_half[l] < right_half[r]:
                # Copy the left half value into the main list
                lst[m] = left_half[l]
                # Move the left pointer right one spot
                l += 1
            else:
                # Copy the right half value into the main list
                lst[m] = right_half[r]
                # Move the right pointer right one spot
                r += 1
            # Either way, we always increse the main pointer one spot
            m += 1

        # When one half finishes (either left or right), copy the rest of the other half into the original
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1
    return lst

print(unsorted_list)
merge_sort(unsorted_list)
print(unsorted_list)


line_break()

# Quick Sort - 
# Worst Case - O(n**2) Time Complexity
# Best Case - O(n log n) Time Complexity
# Space Complexity - O(log n) Linear

print('Quick Sort:')
unsorted_list = [randint(1,50) for _ in range(10)]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    # Find a pivot value - can be any of the elements - we will choose the middle
    mid_idx = len(lst)//2
    pivot = lst[mid_idx]
    # Get all of the elements that are less than the pivot
    left = [x for x in lst if x < pivot]
    # Get all of the elements that are equal to the pivot
    middle = [x for x in lst if x == pivot]
    # Get all of the elements that are greater than the pivot
    right = [x for x in lst if x > pivot]

    # Sort the left in the same way
    sorted_left = quick_sort(left)
    # Sort the right in the same way
    sorted_right = quick_sort(right)

    return sorted_left + middle + sorted_right


print(unsorted_list)
sorted_list = quick_sort(unsorted_list)
print(unsorted_list)
print(sorted_list)


line_break()
# Timsort - sorted()
# Worst Case - O(n log n) Time Complexity
# Best Case - O(n) Time Complexity
# Space Complexity - O(n) Linear

print('Tim Sort:')
unsorted_list = [randint(1,50) for _ in range(10)]

print(unsorted_list)
sorted_list = sorted(unsorted_list)
print(sorted_list)