
def hi() :
    global val
    val = 'hi!'
    return val

def hello() :
    print(val)

print(hi())
print(val)
hello()
