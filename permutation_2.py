def reverse_string(my_string): 
    for i in range(len(list(my_string)), 0, -1):
        print(my_string[i-1])

reverse_string("prick")