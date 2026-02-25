def sum_list(numbers):
    #base case
    if len(numbers) == 0:
        return 0
    else:
        #recursive case
        return numbers[0] + sum_list(numbers[1:])
    
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))



def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
    
my_list = [4, 7, 8, 99, 10]
print(find_max(my_list))