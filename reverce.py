sequence = [11, 22, 33, 44, 55, 66]
k = len(sequence)-1
m = 0
for i in sequence:
    m += i
print(m)


start = 0
stop = int(len(sequence)/2)
for i in range (start, stop):
    print(i)
    temp = sequence[i]
    sequence[i] = sequence[len(sequence) - i - 1]
    sequence[len(sequence) - i - 1] = temp
print(sequence)

#dima


li = [11, 22, 33, 44, 55, 66]
ki = [0 for x in range(len(li))]
n = 1
while n < len(li):
    for i in range(len(li)-n):
        ki[i] = li[len(li)-n]
        n += 1

if n == len(li):
    i+=1
    ki[i] = li[len(li)-n]

print(li)
print(ki)

#while i > -1:
#   print (sequence[i])
#    i = i - 1


#b = list(reversed(sequence))
#print(b)
