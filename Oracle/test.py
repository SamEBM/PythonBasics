# Python3 program for the above approach

# Function that finds lexicographically
# smallest after removing the
# duplicates from the given string
def getString(input_str):

	char_count = [0] * 26
	char_visited = [0] * 26
	n = len(input_str)

	for i in input_str:
		char_count[ord(i) - ord('a')] += 1

	res = []

	for i in range(n):
		char_count[ord(input_str[i]) - ord('a')] -= 1

		if (not char_visited[ord(input_str[i]) - ord('a')]):

			while (len(res) > 0 and res[-1] < input_str[i] and char_count[ord(res[-1]) - ord('a')] > 0):

				char_visited[ord(res[-1]) - ord('a')] = 0
				del res[-1]

			res += input_str[i]
			char_visited[ord(input_str[i]) - ord('a')] = 1
			
	return "".join(res)

# Driver Code
if __name__ == '__main__':
	
	# Given S
	S = "acbc"

	# Function Call
	print(getString(S))

# This code is contributed by mohit kumar 29

