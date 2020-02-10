#     x_index:     *   /
mult_table = {0: [1, 2, 3],
			  1: [0, 3, 2],
			  2: [0, 3, 1],
			  3: [1, 2, 0]}

def __tokenise(exp):
	parts = exp.split('=')
	terms = parts[0].split(':') + parts[1].split(':')
	terms = [float(x) if x != 'x' else 'x' for x in terms]
	return terms

def __execute(tokens):
	x_index = tokens.index('x')
	operations = mult_table[x_index]
	return tokens[operations[0]] * tokens[operations[1]] / tokens[operations[2]]

def result(string):
	"""Returns the value of x for a given ratio in the form of A:B=x:C or similar"""
	return __execute(__tokenise(string))

if __name__ == "__main__":
	while True:
		expression = input("Please type your ratio (A:B=x:C or similar): ")
		print(result(expression))
