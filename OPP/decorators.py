""" s  = "67"
def func():
    #global s
    s = 50
    print("s :"+str(s))

func()
print(s) """

def new_decorator(func):
    def wrap_func():
        print("CODE HER EBEFORE EXECUTING FUNC")
        func()
        print("Func has been called")
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This funs is in need of a decorator")

#func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()