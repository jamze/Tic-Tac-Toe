sequence = int(input())

sequence = [int(x) for x in str(sequence)]

len_seq = len(sequence)
sum_seq = sum(sequence)

print(sum_seq / len_seq)
