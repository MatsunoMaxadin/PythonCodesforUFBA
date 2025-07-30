from math import *
A, B, C, D, E, F = map(int, input().split())

Luther = abs(2023-A) * 2
Diego = abs(2023-B) * 2
Alisson = abs(2023-C) * 2
Klaus = abs(2023-D) * 2
Ben = abs(2023-E) * 2
Viktor = abs(2023-F) * 2
Five = Luther + Diego + Alisson + Klaus + Ben + Viktor 	
print("Luther", Luther)
print("Diego", Diego)
print("Alisson", Alisson)
print("Klaus", Klaus)
print("Five", Five)
print("Ben", Ben)
print("Viktor", Viktor)
