# binary search 

def binary_search(item, lst):
    end = len(lst) - 1
    start = 0
    mid = (end + start) // 2

    while start <= end:
        mid = start + (end - start)//2
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            end = mid - 1
        elif lst[mid] < item:
            start = mid + 1
            
    return -1
# Linear Search
def linear_search_unsorted(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search_unsorted(arr, target):
    # Your code here
    start = 0
    end = len(arr) -1

    while start <= end:
        mid = start + (end - start)// 2
        if arr[mid] == target:
            return mid
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1 
            

# # Scenario 1 Test
# unsorted_list = [42, 15, 7, 30, 22, 10, 18]
# target_1 = 30
# result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
# result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
# print(result_binary_search_1)
# print(result_linear_search_1)

# Linear Search
# def linear_search_sorted_words(word_list, target_word):
#     # Your code here
#     for i in range(len(word_list)):
#         if word_list[i] == target_word:
#             return i
#     return -1

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    # Your code here
    start = 0
    end = len(word_list) -1

    while start <= end:
        mid = start + (end - start)// 2
        if word_list[mid] == target_word:
            return mid
        elif word_list[mid] < target_word:
            start = mid + 1
        else:
            end = mid - 1
    return -1 

# # Scenario 2 Test
# sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
# target_2 = 'orange'
# result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
# result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(result_linear_search_2)
# print(result_binary_search_2)
# Linear Search
# def linear_search_last_occurrence(arr, target):
#     # Your code here
#     last = 0
#     count = 0
#     for i in range(len(arr)):
#         count += 1
#         if arr[i] == target:
#             last = i
#     if last:
#         return last, count
#     return -1

# Binary Search
def binary_search_last_occurrence(arr, target):
    start = 0
    end = len(arr) - 1
    

    while start <= end:

        mid = start + (end - start)//2
        if arr[mid] == target:
            while arr[mid] == target and mid <= len(arr) - 1:
                mid += 1
            return mid - 1 
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
# Scenario 3 Test
occurrence_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(result_linear_search_3)
print(result_binary_search_3)
# strs = ["act","pots","tops","cat","stop","hat"]
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#         dic = {}
#         for x in strs:
#             word_sum = sum(bytearray(x.encode('ascii')))
            
#             print(word_sum)
#             if word_sum in dic:
#                 dic[word_sum].append(x)
#             else:
#                 dic[word_sum] = [x]

#         print(dic)
#         return [x for x in dic.values()]

# print(groupAnagrams(strs))



20 

20// 2

11 20