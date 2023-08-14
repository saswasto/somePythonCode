# Python program to swap two elements in a list
a = 20
b = 30
#a = temp
#a = b
#temp = b
a,b=b,a
print("a =",a)
print("b =",b)
# <<<< another way >>>
def swapPositions(list, pos1, pos2):

  list[pos1], list[pos2] = list[pos2], list[pos1]
  return list

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))
