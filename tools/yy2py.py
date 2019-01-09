with open("grammar.yy") as f:
	a = f.read().split(";\n")
for i,p in enumerate(x for x in a if x):
	head = p.split(":")[0].replace("\t","").replace(" ","")
	print("""
def p_%s%d(t):
	'''%s'''
	print("%s_%d")
""" % (head, i, p, head, i))

