"""
Generate N terms of fibonacci series 
"""

num = int(input("Enter n number of fibonacci series :: "))
a = 0; b = 1
for t in range(num-2):
  c = a+b
  a = b
  b = c
  
