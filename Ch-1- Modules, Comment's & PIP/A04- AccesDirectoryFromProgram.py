# here we are going to access the files and folders from window.
# this will shhowing the answer in our terminal like a tree in cmd promt which you will type.


import os

def print_directory_contents(directory_path):
    """Prints the contents of a specified directory.

    Args:
        directory_path (str): The path to the directory.
    """

    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        print(item_path)

# Example usage:
directory_to_list= "."  # Current directory
print_directory_contents(directory_to_list)