from script import sparse_search

data_one = ["Liam", "", "", "", "", "", "Nora", "", "", "", "Oliver", "", "Ava", "", "", "", "Sophia"]
search_one = "Sophia"
print("Calling sparse_search.....")

# Call the sparse_search function with the first dataset
ret = sparse_search(data_one, search_one)

'''Check if the returned index is valid (not -1)
If ret is not -1, it means the value was found in the dataset'''
if ret != -1:
    print(f"{search_one} found at index {ret}")
# If ret is -1, the value was not found in the dataset
else:
    print(f"{search_one} not found in dataset")

data_two = ["4", "", "", "7", "", "", "10", "", "14", "", "", "", "21", "30"]
search_two = "7"
print("\nCalling sparse_search.....")

# Call the sparse_search function with the second dataset
ret = sparse_search(data_two, search_two)

'''Check if the returned index is valid (not -1) for the second dataset
If ret is not -1, it means the value was found in the dataset'''
if ret != -1:
    print(f"{search_two} found at index {ret}")
# If ret is -1, the value was not found in the dataset
else:
    print(f"{search_two} not found in dataset")