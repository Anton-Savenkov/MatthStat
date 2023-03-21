from math import factorial, exp

def funk_Bernoulli (n, k, p):  # формула Бернулли
    x = factorial(n) / (factorial(k) * factorial(n-k))
    return x * (p**k) * (1-p)**(n-k)

n = 100
k = 85
p = 0.8
result_bernoulli = funk_Bernoulli(n, k, p)
#print(round(result_bernoulli, 5))

def funk_Puasone(m, p, n):
    λ = p * n
    return exp(-λ) * (λ ** m) / factorial(m)

result_puasone = funk_Puasone(2, 0.0004, 5000)
#print(result_puasone)

def funk_Probability(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))

#print(funk_Probability(52, 10))
