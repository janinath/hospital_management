

    
x=6

y=7

def myfun():
    global x
    x+=10
    y=9
    print('inside',x,y)
    
myfun()
x=2
print('outside',x,y)


