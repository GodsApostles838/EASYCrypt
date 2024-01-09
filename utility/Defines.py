
def c_blocksize(blocksize):
    return ("Block size is missing" 
            if blocksize is None else f"Error: Block size must be greater than 16 (provided: {blocksize})" if blocksize <= 16 else None)

def c_key_size(key_size):
    return ("Key size is missing" 
            if key_size is None else f"Error: Key size must be greater than 16 (provided: {key_size})" if key_size <= 16 else None)

def c_plaintext(plaintext):
    return ("Error: Plaintext cannot be empty"
            if plaintext is None or plaintext == "" else None)
    
    
    
def swap_elements(arr: list, element1: str, element2: str, reverse: bool = False) -> list:
  """
  Swaps two elements in a list.

  Args:
      arr: The list to modify.
      element1: The first element to swap.
      element2: The second element to swap.
      reverse: Whether to swap the elements in reverse order.

  Returns:
      The swapped list.
  """

  for i, element in enumerate(arr):
    if element == element1: index1 = i
    elif element == element2: index2 = i

  if element1 not in arr or element2 not in arr:
    print(f"Error: {element1} or {element2} not found in the list.")
    return arr

  if reverse: arr[index1], arr[index2] = arr[index2], arr[index1]
  else: arr[index1], arr[index2] = arr[index2], arr[index1]

  return arr


# Example usage
# my_list = ['x', 'f', 'g', 'h', 'd']
# result = swap_elements(my_list, 'x', 'd')
# print(result)

# # Example usage with reverse swap
# my_list_reverse = ['d', 'f', 'g', 'h', 'x']
# result_reverse = swap_elements(my_list_reverse, 'x', 'd', reverse=True)
# print(result_reverse)


