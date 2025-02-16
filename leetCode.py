nums = int(input())
num = nums
hasil = 0
while nums > 0:
    c = nums%10
    hasil += c
    nums = nums//10
if num%hasil == 0:
    print(True)
else:
    print(False)