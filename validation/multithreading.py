# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# # wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")

def second_occurrence_index(lst, element):
    try:
        first_index = lst.index(element)  # Find the first occurrence index
        second_index = lst.index(element, first_index + 1)  # Find the second occurrence index
        return second_index
    except ValueError:
        return -1  # Return -1 if the element doesn't occur twice
my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_find = 2
second_index = second_occurrence_index(my_list, element_to_find)
print("Index of the second occurrence:", second_index)
