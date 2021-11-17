# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
#
#    https://docs.python.org/3/library/stdtypes.html#string-methods

def addnumber(word):
    if word.isnumeric():
        word = word +1
    for i in word:
        if i.isnumeric():

addnumber("foo")
        

   

