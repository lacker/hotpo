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
	# Hotpo rules
	"CD": "C",
	"CE": "CV",
	
	# Modular rules
	"TD": "DT",
	"TE": "EU",
	"UD": "ET",
	"UE": "DV",
	"VD": "DU",
	"VE": "EV",
	
	# Finiteness rules
	"TZ": "Z",
	"UZ": "EZ",
	"VZ": "DEZ",
}

def step(s):
	pass

print("hello")
