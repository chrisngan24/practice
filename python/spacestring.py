def space_string(string, dict):
	for i in range(0,len(dict)):		
		if string.find(dict[i]) == 0:
			
			sub = string[0:len(dict[i])]
			
			if len(string)== len(sub):
				return sub
			else:
				
				return sub + space_string(string[len(sub):len(string)], dict)
		
		
	return ""




if __name__ == "__main__":
	dict = ['apple','a','bee']
	string = 'aapplebee'
	print space_string(string, dict)
