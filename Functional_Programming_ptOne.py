# -*- coding: utf-8 -*-
"""
Created on Sat May 12 17:22:11 2018

"""
#some exercises to create functions

def my_first_function(x, y):
    z = y * x
    r = y / x
    print('Args multiplied are: ' + str(z) + ' while Args divided are: ' + str(r))

my_first_function(10, 15)

import functools

def do_pure(data):
    #returns copy times two
    return data * 2
#overload * that modifies data or causes other
#sides effects would make this function unpure
#no guarantee of pureness

#in Python functions are objects
def func1():
    return 1
def func2():
    return 2

#which can be sticked in a dictionary as follow
my_funcs = {'a': func1, 'b': func2}
#and called as
my_funcs['a']()

#there are also closures

def outer(outer_arg):
    def inner(inner_arg):
        return inner_arg + outer_arg
    return inner

func = outer(10)
func(5)
func.__closure__[0].cell_contents
                
#partials from functools
def func(a, b, c):
    return a, b, c
#very common concept as in Askell
p_func = functools.partial(func, 10)
p_func(3, 4)                

#recursion vs loops
def loop(n):
    for x in xrange(int(n)):
        a = 1 + 1
# use the timeit to check     
def recurse(n):
    if n<=0:
        return
    a = 1 + 1
    recurse(int(n) - 1)

#lambda allows very limited anonymous functions
def use_callback(callback, arg):
    return callback(arg)

use_callback(lambda arg: arg * 2, 10)
#lambda is not always necessary is always possible
#to add two extra lines
def double(arg):
    return arg * 2
use_callback(double, 10)
#list comprehension instead of map
#typical use of map
map(lambda arg: arg * 2, range(2, 6))
#which in list comprehension is
[x * 2 for x in range(2, 6)]

#or to replace filter too
filter(lambda x: x > 10, range(5,16))
[x for x in range(5, 16) if x >10]

#decorators from functools
def decorator(func):
    @functools.wraps(func)
    def new_func(*arg, **kwargs):
        print 'decorator was here'
        return func(*arg, **kwargs)
    return new_func
@decorator
def add(a, b):
    return(a + b)
add(2, 3)

