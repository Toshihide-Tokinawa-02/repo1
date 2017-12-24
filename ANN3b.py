def div(x1, x2):
	return x1 / x2

def ANN():
	
	print("layers?")
	layers = int(input("n:"))
	if(layers <= 4):
			print("ok")
	else:
			print("reduce layer number")
			
	
ANN()


def B2():
	print("input units?")
	iunits = int(input("n:"))
	if(iunits <= 10):
			print("ok - NN set-up")
	else:
			print("reduce i-units number")

B2()

print("layers:")
print(layers)
print("iunits:")
print(iunits)

x1 = layers
x2 = iunits

div(x1, x2)

div(x2, x1)

