
using Printf

function find_stagnation(limit::Int = 200_000_000)
    total = 0.0
    reference = pi^2 / 6.0

    start = time_ns()

    for k in 1:limit
        x = Float64(k)
        term = 1.0 / (x * x)
        updated = total + term

        if updated == total
            elapsed = (time_ns() - start) / 1e9

            absolute_difference = abs(reference - total)
            relative_difference =
                absolute_difference / abs(reference) * 100.0

            println("Status: stagnation detected")
            println("First attempted index: ", k)
            println("Last successful addition: ", k - 1)
            @printf("Stored sum: %.17g\n", total)
            @printf("Absolute difference: %.10e\n", absolute_difference)
            @printf("Relative difference: %.10e%%\n", relative_difference)
            @printf("Elapsed time: %.6f seconds\n", elapsed)

            return
        end

        total = updated
    end

    elapsed = (time_ns() - start) / 1e9

    println("Status: limit reached (", limit, ")")
    println("Last completed index: ", limit)
    @printf("Stored sum: %.17g\n", total)
    @printf("Elapsed time: %.6f seconds\n", elapsed)
end

find_stagnation()
