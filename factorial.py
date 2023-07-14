#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

# Call the factorial function
result = factorial(num)

print("The factorial of", num, "is", result)


# In[ ]:




