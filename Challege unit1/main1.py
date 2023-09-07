#implement of factorial
def fact_rec(n):
  if (n == 0 and n == 1):
    return 1
  else:
    return n * fact_rec(n - 1)
  num = int(input("Enter the value :"))
  res = fact_rec(num)
  print("The factorial of {} is {}.".format(num, res))
