def sparse_search(data, search_val):
  print("\nData: " + str(data))
  print("\nSearch Value: " + str(search_val))
  
  # Initialize the starting and ending index of the search range
  first = 0
  last = len(data) - 1

  # Helper function to compare values correctly
  # Allows searching both names and numbers automatically
  def compare(a, b):
      if a.isdigit() and b.isdigit():
          return int(a) - int(b)
      if a < b:
          return -1
      if a > b:
          return 1
      return 0

  # Loop while the search range is valid
  while first <= last:
      # Calculate the middle index
      mid = (first + last) // 2

      # If the element at mid is empty, find the nearest non-empty string
      if not data[mid]:
          # Initialize pointers to move left and right from mid
          left = mid - 1
          right = mid + 1
          # Continue searching until a non-empty string is found
          while True:
              # If both pointers are out of bounds, the value is not in the dataset
              if left < first and right > last:
                  print("\n" + str(search_val) + " is not in the dataset")
                  return -1
              # Check the right pointer for a non-empty element
              elif right <= last and data[right]:
                  mid = right
                  break
              # Check the left pointer for a non-empty element
              elif left >= first and data[left]:
                  mid = left
                  break
              # Move the right pointer one step outward
              right += 1
              # Move the left pointer one step outward
              left -= 1

      # Check if the middle element matches the search value
      if data[mid] == search_val:
          print("\n" + str(search_val) + " found at position " + str(mid))
          return mid

      # If the search value is smaller than mid, search the left half
      if compare(search_val, data[mid]) < 0:
          last = mid - 1
      # If the search value is larger than mid, search the right half
      elif compare(search_val, data[mid]) > 0:
          first = mid + 1

  # If the loop ends without finding the value, print not found
  print("\n" + str(search_val) + " is not in the dataset")
  return -1