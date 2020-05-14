#tuple in tuple
a = ((1,2), (3,4))
print('tuple in tuple:', a)

#list in tupleㅎ
b = ([1,2], [3,4])
print('\nlist in tuple:', b)
#안쪽에 있는 리스트의 원소만 변경 가능
b[0][0] = 5
print('After:', b)

#tuple in list
c = [(1,2), (3,4)]
print('\ntuple in list:', c)
#바깥쪽에 있는 리스트의 원소만 변경 가능
c[0] = (5,6)
print('After:', c)
