while True:
  t = int(input("digite um numero"))
  for i in range (1,11):
    s = t * i
    print(f"a multiplicação entre {i} * {s}")
    if t == -1:
      break