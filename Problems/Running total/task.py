sequence = int(input())

sequence = [int(x) for x in str(sequence)]

len_seq = len(sequence)
new_seq = []

new_seq.append(sequence[0])
sum = sequence[0]

for i in range (1, len_seq):
    sum = sum + sequence[i]
    new_seq.append(sum)


print (new_seq)

