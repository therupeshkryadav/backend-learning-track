# WAP to ask to enter names of three favourite movies and store them in a list.Then print the list.
print("Welcome to the Movie List App!")
movies = []
print("Enter the names of three favourite movies: ")
mov1 = input("Movie 1: ")
mov2 = input("Movie 2: ")
mov3 = input("Movie 3: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# WAP to check whether a list contains a palindrome of elements  ( Hint : Use copy() method) 
print("Welcome to the Palindrome Checker!")
list1 = [1, 2, 3, 2, 1]
print("list1: ", list1)
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("The list is a palindrome.")
else:    print("The list is not a palindrome.")

# WAP to print the elements of the list using a loop
print("Welcome to the List Printer!")
print("The elements of the list are: ")
numbers = [10, 20, 30, 40, 50]
counter = 0
while counter < len(numbers):
    print(numbers[counter])
    counter += 1

# WAP to search for an element in a list and print its index if found, otherwise print "Element not found".
print("Welcome to the List Searcher!")
search_tuple = (10, 20, 30, 40, 50)
print("The elements in the tuple are: ", search_tuple)
search_element = int(input("Enter an element to search: "))
if search_element in search_tuple:
    index = search_tuple.index(search_element)
    print(f"Element found at index: {index}")
else:    print("Element not found.")    