def Name():
    name = input()
    print(name)

def ShowType(x):
    print(type(x))

def ShowLenght(x):
    print(len(x))

def UpperCase(x):
    print(x.upper())

def Trim(x):
    substr=x[4:6]
    print(substr)

def S2_a():
    txt = "More results from text..."
    substr = txt[4:12]
    print(substr)
    print(substr.strip()) 

def S2_b():
    txt = "More results from text..."
    print(txt.split())

def S2_c():
    age = 36
    txt = "My name is Mary, and I am {}"
    print(txt.format(age))


var_int=1
var_float=1.1
text="helloworld"
textx="""Lorem Ipsum
Lorem Ipsum
Lorem Ipsum
Lorem Ipsum
Lorem Ipsum
"""

Name()
ShowType(var_int)
ShowType(var_float)
ShowLenght(text)
UpperCase(text)
Trim(textx)
S2_a()
S2_b()
S2_c()