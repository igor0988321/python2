# Reverse the line

def reverse_str(s):
    result = " "
    for char in s:
        result = char + result
    return result

print(reverse_str("hello"))


# FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and  i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# Word count


text = "apple banana apple orange banana apple"

words = text.split()
result = {}

for word in words:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)


# Remove duplicates


def remove_dublicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_dublicates([1,2,3,4,5,5,3,2,1]))



