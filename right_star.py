

n = int(input('Please enter any single number: '))   # n = 5


for i in range(1,n+1):   # i = 1,2,3,4,5
    print(' '*(n-i),end='')
    print('*'*(2*i-1))

print('*')  



#     *
#    ***
#   *****
#  *******
# *********


# 별은 홀수 1, 3, 5, 7, 9

# 공백은 4, 3, 2, 1, 0
