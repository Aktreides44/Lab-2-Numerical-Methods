using Printf
S_b = 1.644934057834575
S_ref = π^2 / 6.0

D_abs = abs(S_b - S_ref)
D_percent = 100.0 * D_abs / abs(S_ref)

println("Language: Julia")
println("S_b:       ", repr(S_b))
println("S_ref:     ", repr(S_ref))
println("D_abs:     ", @sprintf("%.12e", D_abs))
println("D_percent: ", @sprintf("%.12e", D_percent), "%")