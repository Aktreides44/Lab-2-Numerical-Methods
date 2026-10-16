import math

S_b = 1.644934057834575
S_ref = math.pi**2 / 6.0

D_abs = abs(S_b - S_ref)
D_percent = 100.0 * D_abs / abs(S_ref)

print("Language: Python")
print(f"S_b:       {S_b:.17g}")
print(f"S_ref:     {S_ref:.17g}")
print(f"D_abs:     {D_abs:.12e}")
print(f"D_percent: {D_percent:.12e}%")