# :::: how to find average in n numbers :::::
num = int(input("how many numbers: "))
total_sum = 0
for n in range(num):
    numbers = float(input("Enter the number: "))
    total_sum += numbers
    avg = total_sum/num
    print("num is ", avg)
