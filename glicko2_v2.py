import math

class Glicko2():
	def __init__(self): 
		# step 1 
		self.mu = 0
		self.phi = 2
		self.sigma = 0.06
		self.tau = 0.3
		self.rating = 20
		self.epsilon = 0.000001

	def update(self, other_mu, other_phi, score):
 #i don't know python arrays (they're probably the same but it's currently late and idk) so this is js in ?? idek what lang
 #but i might do this if i wanted to do the multiple player iterations
# m = # of players
# mu, phi, score_other etc [m]
# intialise all the values with input/arbituary ones
# calc the self and constant values
# i = range(m)
# for i in range:
# other.something[i] does python work this way i have no clue processed using the same eqn
# v or E or delta or whatever += other.something[i]
# tada then u can have m players the benefits of which i dont even know

 
		# step 3
		g = 1 / math.sqrt(1 + (3 * (other_phi ** 2)) / (math.pi ** 2))
		E = 1 / (1 + math.exp((-g) * (self.mu - other_mu)))
		#v = 1 / ((g ** 2) * E / (1 - E))  hi cadence i think u made a mistake which is like seems like you did division when there was curly braces, which the person who wrote the algo didn't intend seeing from their example working? i feel like that's probably somewhere where you might've went wrong
        v = 1 / ((g ** 2) * E * (1 - E))
        
        
 
		print("v: " + str(v))

		# step 4
		#delta = v * g / (score - E)
        delta = v * g * (score - E) #here too i highlighted on your ?? algo pdf u can go see the worked eg thingy

		# step 5 
		# 1
		a = math.log(self.sigma ** 2)
		A = a
        

		# 2
		if (delta ** 2) > (self.phi ** 2 + v):
			B = math.log(delta ** 2 - self.phi ** 2 - v)
		else:
			k = 1
			while self.update_volatility(a - k * self.tau, v, delta, a) < 0:
				k += 1
			B = a - k * self.tau

		# 3
		fA = self.update_volatility(A, v, delta, a)
		fB = self.update_volatility(B, v, delta, a)

		# 4
		while math.fabs(B - A) > self.epsilon:
			# (a) 
			C = A + (A - B) * fA / (fB - fA)
			fC = self.update_volatility(C, v, delta, a)
			# (b)
			if fC * fB < 0:
				A = B
				fA = fB
			else:
				fA /= 2
			# (c)
			B = C
			fB = fC

		# 5
		# print("Final value of A: " + str(A))
		new_sigma = math.exp(A / 2)

		# 6
		new_phi = math.sqrt(self.phi ** 2 + new_sigma ** 2)

		# 7
		new_phi = 1 / math.sqrt(1 / (new_phi ** 2) + 1 / v)
		new_mu = self.mu + (new_phi ** 2) * g / (score - E)
		self.mu = new_mu
		self.phi = new_phi
		self.sigma = new_sigma

		# 8
		self.rating = 50 + 7.5 * (new_mu - 2 * new_phi) 
            


	def update_volatility(self, x, v, delta, a):
		ans = math.exp(x) * (delta ** 2 - self.phi ** 2 - v - math.exp(x))
		ans /= (2 * (((self.phi ** 2) + v + math.exp(x)) ** 2))
		ans -= ((x - a) / (self.tau ** 2))
		return ans

person_1 = Glicko2()
person_2 = Glicko2()

while 1:
	mu1 = person_1.mu
	phi1 = person_1.phi
	mu2 = person_2.mu
	phi2 = person_2.phi
	winner = int(input("Who won: 1 or 2? "))
	if winner == 1:
		person_1.update(mu2, phi2, 1)
		person_2.update(mu1, phi1, 0)
	else:
		person_1.update(mu2, phi2, 0)
		person_2.update(mu1, phi1, 1)
	# update_rating()
	print(str(person_1.rating) + " - " + str(person_1.mu) + "μ, " + str(person_1.phi) + "Φ, " + str(person_1.sigma) + "σ")
	print(str(person_2.rating) + " - " + str(person_2.mu) + "μ, " + str(person_2.phi) + "Φ, " + str(person_2.sigma) + "σ")
	print()
