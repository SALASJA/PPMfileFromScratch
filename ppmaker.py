def red(file):
	file.write(bytes(b'\xff\x00\x00'))
	
def blue(file):
	file.write(bytes(b'\x00\xff\x00')) #generalized?
	
def green(file):
	file.write(bytes(b'\x00\x00\xff')) #change it to not be green
	
def main():
	bytes = bytearray(b'P6\n100 100\n225\n') #ppm header is 11 pixels long
	print(bytes)
	file = open('picture.ppm', 'wb')
	height = 100
	length = 100
	print(bytes)
	file.write(bytes)
	state = 0
	count = 0
	ycount = 0
	endstate = 10
	
	for i in range(0, height * length):
		if(state % 3 == 0):
			red(file)
		if(state % 3 == 1):
			blue(file)
		if(state % 3 == 2):
			green(file)
				
		count = count + 1
		ycount = ycount + 1
		
		if (count == 10):
			state = state + 1 #delayed counter        
			count = 0
		
		if (state == endstate):
			state = state - 10   #0 - 10 to do checkered pattern i have to shift the start and end state if i just shift start state its just gonna end
			#i need a theory of ppm files 10 is the number of state elements
		
		if (ycount == 1000):
			endstate = endstate + 1   #shifting the states
			state = state + 1 #start state gets shifted by one 
			ycount = 0 
		
		
	file.close()
		
	
main()