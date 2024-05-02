x = input("Digite: ")
y = x.split(",")
conty = {}

for z in y:
  if z in conty:
    conty[z] = conty[z] + 1
  else:
    conty[z] = 1

print(conty)