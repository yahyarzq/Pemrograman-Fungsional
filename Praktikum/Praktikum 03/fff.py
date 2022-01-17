def tri_recursion(k):
  print("LL",k)
  if(k > 0):
    result = tri_recursion(k - 1)
    print(k)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
