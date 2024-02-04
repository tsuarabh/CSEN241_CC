
#!/bin/bash

# First Memory Test Case: Sequential Memory Access
echo "Running First Memory Test: Sequential Access"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=memory --memory-block-size=1K --memory-total-size=250M --memory-access-mode=seq run
    echo ""
done

# Second Memory Test Case: Random Memory Access
echo "Running Second Memory Test: Random Access"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=memory --memory-block-size=1K --memory-total-size=250M --memory-access-mode=rnd run
    echo ""
done

echo "All Memory tests are completed."
