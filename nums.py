num_of_even = 0






# def even_nums(x,y):
#     # global num_of_even
#     num_of_even=0
#     if 2%x == 0:
#         num_of_even += 1
#     if 2%y == 0:
#         num_of_even += 1

# print(even_nums(2,3))
# print(num_of_even)


def printers():
    print(num_of_even + 1)

def changenum():
    global num_of_even
    num_of_even = 9

printers()
print(num_of_even)
changenum()
print(num_of_even)
