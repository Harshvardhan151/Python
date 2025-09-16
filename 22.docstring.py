# docstring is like a definition for a class, method, module
# it's different from comments as it is not ignored by the code
# it needs to be the first thing after def a class or else it will become none

def square(n):
    '''this is docstring , this class will square any number'''
    return(n**2)

print(square(4))
print(square.__doc__)

# if there is anything before doc

def ok():
    print("ok")
    ''' code wont recognise this docstring'''
    return 0

print(ok.__doc__)