"""
Stable
Time: O(n+k), k: range
Auxiliary Space: O(n+k)
"""

def counting_sort(array, floor, ceiling):
    counting_array = [0]*(ceiling+1) # remember +1 b/c index starts at 0!
    
    # --- get counts ---
    # doesn't work b/c counting_array isn't updated till the end!
    # counting_array = [counting_array[val]+1 for val in array]
    for val in array:
        counting_array[val] += 1

    # --- get running sum of counts ---
    # * there are "value" numbers <= "index"
    # Ex: for [0, 2, 4, 4, 5, 6, 6, 7, 7, 7], 
    # there are 5 values <= 4
    # * Represents last position that value can occur 
    # Ex: 4 can't appear after (5-1, or 4th index)
    for i in range(1, ceiling+1):
        counting_array[i] += counting_array[i-1]
        
    print('counting_array:', counting_array)
    # --- placement ---
    final = [None]*len(array)
    for i in range(len(array)-1, -1, -1): # counter must start at end
        print("{} being placed at index {}".format(array[i], counting_array[array[i]]-1))
        final[counting_array[array[i]]-1] = array[i]
        counting_array[array[i]] -= 1

    return final


if __name__ == "__main__":
    # array = [1, 4, 1, 2, 7, 5, 2]
    array = [6, 2, 1, 3, 5, 8, 2, 9, 4]
    sorted_array = counting_sort(array, min(array), 9)
    print(sorted_array)


