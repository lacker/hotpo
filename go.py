# A cellular automaton representation of the
# hotpo problem.
# C(n) is the hotpo algorithm
# D(n) = 2n
# E(n) = 2n+1
# T(n) = 3n
# U(n) = 3n+1
# V(n) = 3n+2
# Z(n) = 0
# Concatenation means composition.
# So a string like CTE means C(T(E(n)))

RULES = {
	"CD": "C",
	"CE": "CV",
}

def step(s):
	pass

print("hello")
