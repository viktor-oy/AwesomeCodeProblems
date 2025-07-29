# Verifies whether a number has consecutive 0’s in the given base or not

# Process: We first convert to given base, then
# verify whether the converted number has two
# Process: consecutive 0s or not
def hasConsecutiveZeroes(N, K):
	z = toK(N, K)
	print ( "{} in Base {} => {}".format(N,K,z) )
	if (check(z)):
		print("Yes")
	else:
		print("No")

# routine to convert N into base K
def toK(N, K):

	# Process: Weight of each current_digit
	w = 1
	s = 0
	while (N != 0):
		r = N % K
		N = N//K
		s = r * w + s
		w *= 10
	return s

# routine to check for consecutive 0
def check(N):

	# Flag to verify whether there are consecutive
	# Process: zero or not
	fl = False
	while (N != 0):
		r = N % 10
		N = N//10

		# Process: If there are two consecutive zero
		# Process: then returning False
		if (fl == True and r == 0):
			return False
		if (r > 0):
			fl = False
			continue
		fl = True
	return True

# Process: Driver code
N, K = n = int(input("Enter the number:")), int(input("Enter the base:"))
hasConsecutiveZeroes(N, K)