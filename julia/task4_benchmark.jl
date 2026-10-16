using Printf
using Statistics

const SIZES = [1000, 10000, 100000, 1000000]
const WARMUPS = 5
const REPEATS = 10

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

mkpath("results")

csv_path = "results/timing_julia.csv"
open(csv_path, "w") do file
    println(file, "language,order,n,run,batch_size,per_call_ms,returned_sum")

    println("TASK 4: JULIA BENCHMARK")
    println("Warm-ups: $WARMUPS, timed runs: $REPEATS\n")

    for n in SIZES
        for reverse in (false, true)
            order_name = reverse ? "reverse" : "forward"

            # Warm-up calls are not timed.
            for _ in 1:WARMUPS
                calculate_sum(n, reverse)
            end

            times_ms = Float64[]
            result = 0.0

            for run in 1:REPEATS
                start_ns = time_ns()
                result = calculate_sum(n, reverse)
                end_ns = time_ns()

                elapsed_ms = (end_ns - start_ns) / 1.0e6
                push!(times_ms, elapsed_ms)

                println(
                    file,
                    "Julia,$order_name,$n,$run,1,",
                    @sprintf("%.9f", elapsed_ms), ",",
                    repr(result)
                )
            end

            median_ms = median(times_ms)
            min_ms = minimum(times_ms)
            max_ms = maximum(times_ms)

            @printf(
                "n=%7d, order=%-7s, median=%.6f ms, min=%.6f ms, max=%.6f ms, sum=%.17g\n",
                n, order_name, median_ms, min_ms, max_ms, result
            )
        end
    end
end

println("\nRaw timing measurements saved to $csv_path")