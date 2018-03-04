#Program to compress the strings by the number of characters within the string

def compress(msg):
	msg_list = list(msg)
	comp_str=[]
	prev= msg_list[0]
	count=1
	for i in range(1,len(msg_list)):
		if msg_list[i]==prev:
			count +=1
		else:
			comp_str.append(prev)
			comp_str.append(str(count))
			prev= msg_list[i]
			count=1
			
	#add the last character
	comp_str.append(prev)
	comp_str.append(str(count))
	return ''.join(comp_str)
	
mes=input("Enter the message: ")
print("The compressed message is : ", compress(mes))
			