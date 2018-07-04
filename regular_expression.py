
#1
l = [1,2,3,4]
cube = lambda x:x**3
l2 = [cube(x) for x in l ]
print(l2)

#2
import functools 
l = [1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b,l))

#3
l = [1,2,3,4,5]

def cube(x):
    return x**3
l2 = list(map(cube,l))
print(12)