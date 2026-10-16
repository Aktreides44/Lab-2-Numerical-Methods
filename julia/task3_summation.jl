using Printf
const N_VALUES = [1000, 10000, 100000, 1000000]

function calculate_sum(n::Int, reverse::Bool)
    total = 0.0

    if reverse
        for k in n:-1:1
            x = Float64(k)
            total += 1.0 / (x * x)
        end
    else
        for k in 1:n
            x = Float64(k)
            total += 1.0 / (x * x)
        end
    end

    return total
end

S_ref = π^2 / 6.0

println("TASK 3: FORWARD AND REVERSE SUMMATION")
println("Reference value: ", repr(S_ref))

for n in N_VALUES
    for reverse in (false, true)
        result = calculate_sum(n, reverse)

        d_abs = abs(S_ref - result)
        d_percent = 100.0 * d_abs / abs(S_ref)

        order = reverse ? "reverse" : "forward"

        println(
            "n=$n, order=$order, ",
            "sum=$(repr(result)), ",
            "D_abs=$( @sprintf("%.12e", d_abs) ), ",
            "D_percent=$( @sprintf("%.12e", d_percent) )%, ",
            "tail=($( @sprintf("%.12e", 1.0/(n+1)) ), ",
            "$( @sprintf("%.12e", 1.0/n) ))"
        )
    end
end

println("\nSmall-case verification:")

expected = [1.0, 1.25, 49.0 / 36.0]

for n in 1:3
    actual = calculate_sum(n, false)
    passed = abs(actual - expected[n]) < 1e-14

    println(
        "n=$n, computed=$(repr(actual)), ",
        "expected=$(repr(expected[n])), passed=$passed"
    )
end
