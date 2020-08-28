#

def deco(x,y,z):
	print(f"given {x}{y}{z} in the big deco")
	
	def small_deco(f):
		print("small deco does things")
		return f
	return small_deco
	
# @deco(1,2,3)
def func(x):
	print("adding 1 to x")
	return x+1
	
# func(52)
deco(1,2,3)(func)
func(52)




def nicify(fn):
	def nicify_helper(name):
		return "good morning " + fn(name)
		
	return nicify_helper

# @nicify
def greet(name):
	return name
# print(nicify(greet)("john"))