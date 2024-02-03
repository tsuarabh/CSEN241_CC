#!/bin/bash

# First CPU Test Case: High Prime Number Calculation
echo "Running First CPU Test: High Prime Number Calculation"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=cpu --cpu-max-prime=20000 run
    echo ""
done

# Second CPU Test Case: Multiple Threads
echo "Running Second CPU Test: Multiple Threads"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=cpu --num-threads=4 --cpu-max-prime=10000 run
    echo ""
done

echo "all CPU tests are completed."
