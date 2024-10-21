## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x):
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	
	i = int("1")
	u = int("0")
	while i <= x:
		if x % i == 0:
			u = u + int("1")
		i = i + int("1")

	t = int("0")
	p = x - int("1")

	while p >= int("1") and t < u:
		f = int("1")
		t = int("0")
		while f <= p:
			if p % f == 0:
				s = s + int("1")
			f = f + int("1")
		p = p - int("1")

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

	if s >= u:
		res=("not anti-prime")
	else: 
		res=("anti-prime")
	return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	import sys
	x = int(sys.argv[1]) 
	print(main(x))