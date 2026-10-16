using Printf

function basel_sum(n::Int)::Float64
    total = 0.0

    for k in 1:n
        x = Float64(k)
        term = 1.0 / (x * x)
        total += term
    end

    return total
end

function main()
    reference = pi^2 / 6.0
    test_values = [1, 2, 3, 1000, 10000]

    for n in test_values
        result = basel_sum(n)
        absolute_difference = abs(reference - result)
        relative_difference = absolute_difference / abs(reference) * 100.0

        println("n = ", n)
        @printf("  Sum:      %.17g\n", result)
        @printf("  Abs diff: %.10e\n", absolute_difference)
        @printf("  Rel diff: %.10e%%\n\n", relative_difference)
    end
end

main()
