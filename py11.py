import re
test_str = "[gfg,is],[best,for],[all,geeks]"
print("The original string is : " + str(test_str))
flat_1 = re.findall(r"\[(.+?)\]", test_str)
res = [sub.split(",") for sub in flat_1]
print("The type of result : " + str(type(res)))
print("Converted Matrix : " + str(res))