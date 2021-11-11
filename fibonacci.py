#fibonacci.py

#returns the Fibonacci sequence from fib(0)=0 to fib(n) in a list(using iteration)
def fib_it(n):
  if n==0:
    return [n]
  lst = [0,1]
  for i in range(n-1):
    lst.append(lst[-1]+lst[-2])  
  return lst

#print the Fibonacci sequence from fib(0)=0 to fib(45)
print("\nThe Fibonacci sequence from fib(0)=0 to fib(45) is:")
print(fib_it(45))

#returns the nth Fibonacci number
def nth_fib(n):
  fib = fib_it(n)[-1]
  return fib

#print the 12th Fibonacci number
print("\nThe 12th Fibonacci number is: " + str(nth_fib(12)))

#returns the first Fibonacci number with ord of mag m and its position
def fib_ord(m):
  i = 0
  while len(str(nth_fib(i))) < m+1:
    i += 1
  fib = fib_it(i)[-1]
  return fib, i

#priint the first Fibonacci number larger than 1 billion(1.0 * 10^9) and its position
print("\nThe first Fibonacci number larger than 1 billion is " + str(fib_ord(9)[0]) + " and is the " + str(fib_ord(9)[1]) + "th number in the sequence.")


