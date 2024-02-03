
#!/bin/bash

# First File I/O Test Case: Sequential Write
echo "Running First File I/O Test: Sequential Write"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=fileio --file-total-size=250M --file-test-mode=seqwr prepare
    sysbench --test=fileio --file-total-size=250M --file-test-mode=seqwr run
    sysbench --test=fileio --file-total-size=250M cleanup
    echo ""
done

# Second File I/O Test Case: Random Read
echo "Running Second File I/O Test: Random Read"
for i in {1..5}
do
    echo "Iteration $i"
    sysbench --test=fileio --file-total-size=300M --file-test-mode=rndrd prepare
    sysbench --test=fileio --file-total-size=300M --file-test-mode=rndrd run
    sysbench --test=fileio --file-total-size=300M cleanup
    echo ""
done

echo "All File I/O tests are completed."
