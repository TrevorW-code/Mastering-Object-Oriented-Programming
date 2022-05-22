f = [1,1,2,3]
f += [f[-1] + f[-2]]
print(f)

f_two = [1,1,2,3]
f_two.__iadd__([f_two.__getitem__(-1).__add__(f_two.__getitem__(-2))])
print("f2: "+ str(f_two))

''' 
Today I learned some of the underlying methods that make this statement work.

Lott states that the line above is the same as the line below. Essentially, the list type in python is an object. I had no idea this was the case. Being trained in Data Science, I've only really experienced python notebooks, which is on the more basic side of python. Learning OOP here, I'm excited to dive a little deeper into this.
'''
