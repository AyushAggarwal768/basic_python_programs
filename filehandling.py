f = open('xyz.txt','r')

print (type(f))
print (f.node)
print (f.name)
print (f.readable())
print (f.writable())
print (f.closed)
f.close()