""" Friedman interview testing"""
n = 5
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        if i == j or i + j == n - 1:
            matrix[i].append('x')
        else:
            matrix[i].append('_')

for i in range(n):
    print(matrix[i].__str__())

myArray = ['a','b','c','d','d','c','b','a']

def isPalindrome(myArray):
    for i in range(len(myArray)):
        if myArray[i] != myArray[len(myArray) - 1 - i]:
            return False
    return True

print(isPalindrome(myArray))


myArray = [1,2,2,4,5,6,7,8,8,8]

def occurrence(array):
    longest = 0
    number = 0
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count > longest:
            longest = count
            number = array[i]
    print('Longest: {}Number{}\n'.format(longest, number))

occurrence(myArray)

myArray = [1,2,1,3,3,1,2,1,5,1]

def hist(array):
    elem = []
    for i in array:
        if i not in elem:
            elem.append(i)
    for i in elem:
        count = 0
        for j in array:
            if i == j:
                count += 1
        print('{}: {}'.format(i, '*' * count))

hist(myArray)

