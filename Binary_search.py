# -*- coding: utf-8 -*-
def binary_search(numbers, number_to_find, low, high):
    
    if low > high:
        return False
    
    mid = int((low+high)/2)
    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid-1)
    
    else:
        return binary_search(numbers, number_to_find, mid+1, high)

if __name__ == '__main__':
    numbers = [4, 5 , 8 , 10 , 15, 19, 20, 35, 50, 84, 90, 100]
    number_to_find = int(input('Type a number: '))
    result  = binary_search(numbers, number_to_find, 0, len(numbers)-1)

    if result is True:
        print('The number is in the list')
    
    else:
        print('The number is not in the list')