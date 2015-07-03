from stackImplementation import Stack

def infixToPostfix(inp):
	precedence = {}
	precedence['('] = 1
	precedence['+'] = 2
	precedence['-'] = 2
	precedence['*'] = 3
	precedence['/'] = 3
	op_stack = Stack()
	out_list = []
	inp_token = inp.split()

	for token in inp_token:
		if token not in '+-*/()':
			out_list.append(token)
		elif token == '(':
			op_stack.push(token)
		elif token == ')':
			top_token = op_stack.pop()
			while top_token != '(':
				out_list.append(top_token)
				top_token = op_stack.pop()
		else:
			while (not op_stack.is_empty() and \
				   precedence[token] <= precedence[op_stack.peek()]):
				out_list.append(op_stack.pop())
			op_stack.push(token)
	while not op_stack.is_empty():
		out_list.append(op_stack.pop())
	return out_list


if __name__ == "__main__":
	inp1 = "1 * ( 2 + 3 ) * 4"
	inp = "A + B * C"
	print "Input given: %s" %("".join(list(inp.split())))
	print "Postfix output: %s" %("".join(infixToPostfix(inp)))