int_a = 100
int_b = 200

print ('int a = ' + str(int_a))
print ('int b = ' + str(int_b))

suma = 0
for x in range(int_a, int_b):
	if (x % 2 == 1):
		suma = suma + x

print suma
