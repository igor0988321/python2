# Right angled trangel

# for i in range(1,7):
#     print('* ' *i)

# inverted right angled trangel
#
# for i in range(7,0, -1):
#     print( '* ' *i)

# pyramid pattern

# for i in range(1, 11, 2):
#     print('* ' *i)

# inverted pyramid pattern

# for i in range(10,0, -2):
#     print('* ' *i)

# Diamond pattern

# for i in range(1,7):
#     print('* ' *i)
#
# for j in range(5,0, -1):
#     print('* ' *j)


# square pattern


# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# full square pettren

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print('*', end=' ')
#         else:
#             print('*', end=' ')
#     print()


# right angle trangel by using numbers

# for i in range(0, 7):
#     print(' '.join(str(x) for x in range(1, i + 1)))



# inverse right angle trangel by using numbers

# for i in range(7, 0 , -1):
#     print(' '.join(str(x) for x in range(1, i+1)))


# floyd*d trangel

# num = 1
# for i in range(5):
#     for j in range(1, i+1):
#         print(num, end=' ')
#         num+= 1
#     print()


# hallo right angel trangel
#
# for i in range(1, 7):
#     for j in range(1, i+1):
#         if j == 1 or j == i or j == 6:
#             print('*', end='  ')
#         else:
#             print('  ', end=' ')
#     print()

# hallo pyramid pattern

# for i in range(1,6):
#     for j in range(5 - i):
#         print(' ', end=' ')
#
#     for j in range(2 * i -1):
#         if j == 0 or j == 2 * i - 2 or i ==5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# hallo diamond pattern


# n = 5
# for i in range(1, n+1):
#     for j in range(5 - i):
#         print(' ', end=' ')
#
#     for j in range(2 * i - 1):
#         if j==0 or j==2 * i - 2:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()
#
# for i in range(n-1,0,-1):
#     for j in range(5 -  i):
#          print(' ', end=' ')
#
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * i - 2 or i == 5:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# hallo diamond
#
# n = 5
# for i in range(1, n+1):
#     for j in range(n-1):
#         print(' ', end=' ')
#     for j in range(2 *i - 1):
#         if j == 0 or j == 2 * i - 2 or i == 5:
#             print(i,end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# hallo diamond numbers

# n = 5
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(' ', end=' ')
#     for  j in range(2*i-1):
#         if j ==  0 or j == 2* i -2:
#             print(i, end=' ')
#
#         else:
#             print(' ', end=' ')
#
#     print()
#
# for i in range(n-1, 0, -1):
#     for j in range(n-i):
#         print(' ', end=' ')
#     for j in range(2*i-1):
#         if j == 0 or j == 2*i-2:
#             print(i, end=' ')
#         else:
#             print(' ', end=' ')
#
#     print()


# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for j in range(2*(n-i)):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()



# butterfly

# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for j in range(2*(n-i)):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
#
# for i in range(n-1, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     for j in range(2*(n-i)):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()


# butterfly

# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     for j in range(2*(n-i)):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()
#
# for i in range(n-1, 0, -1):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     for j in range(2*(n-i)):
#         print(' ', end=' ')
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()