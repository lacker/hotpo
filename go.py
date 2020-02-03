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

TOP_DOWN = {
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

# Do a single replacement on the string
def step(s, rules=TOP_DOWN):
	for i, ch in enumerate(s):
		pair = s[i:i+2]
		if pair in rules:
			result = rules[pair]
			return s[:i] + result + s[i+2]
	return s
		
def fixed(s, rules):
	while True:
		new_s = step(s, rules)
		if s == new_s:
			return s
		s = new_s
