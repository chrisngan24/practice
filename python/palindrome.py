def long_palindrome(input):
	longest = 0
	start = 0
	end = 0
	for i in range(0,len(input)):
		for j in range(i, len(input)):
			if(is_palindrome(input[i:j])):
				if(j-i+1 > longest):
					longest = j-i 
					start = i
					end = j
	return input[start:end]



def is_palindrome(string):
	for i in range(0, len(string)/2):
		if(string[i] != string[len(string)-1-i]):
			return False
	return True

if __name__ == "__main__":
	print long_palindrome('aaefede')
	print long_palindrome('sssesssssde')
	print is_palindrome('heeh')
	print is_palindrome('a')
	print is_palindrome('helleh')