# LISTS

str = 'hello there greetings'
str.split(' ')

fib1 = [1,1,2,3,5,8,13]
fib1[2]
fib1[-1]

fib1[0:4]

fib2 = [21, 34, 55]

fib1 + fib2

fib1[0] = 9

fib1[0] = 1


fib1 = [1,1,2,3,5,8,13]
fib2 = [21,34,55]
fib = fib1 + fib2

fib.append(89)
fib

fib.pop()

fib.append(89)
fib.append(89)

fib.remove(89) ## removes one instance of given element

del(fib[2])

chars = ['mario', 'luigi', 'bowser']
chars.append(5)

nums = [chars, fib1, [1,2,3,4]]
nums[2][1]