# -------- Closures ----------

def func():
    
    def helper():
        return x+y

    x = 5
    y = 3
    
    return helper()

r = func()

def enclosing():
    x = 'closure'
    y = 'another lcosure'
    def local_func():
        print(x)
        print(y)
    return local_func

lf = enclosing()
lf()

print(lf.__closure__[0].cell_contents) # variable in earlier scope

class Enclosing:
    class Local:
        def func():
            pass
            # def local():
            #   python doesn't have nested functions 
            #     pass

print(Enclosing.Local.func)

# x = "hi"
# def envelope():
#     x = "hello"
#     def letter():
#         # global x
#         nonlocal x
#         x = "hey"
#         print('from letter', x)
    
#     letter()
#     print('from envelope', x)

# print(x)
# envelope()
# print(x)