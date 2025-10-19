#!/bin/bash

BINFILE="$1"

echo "Running Dieharder test suite on $BINFILE..."
echo "Started at: $(date)"

# Run all tests and save results
#dieharder -g 201 -f "$BINFILE" -a | tee dieharder_full_results.txt

# Monitor with progress
dieharder -g 201 -f $BINFILE -a 2>&1 | \
    while IFS= read -r line; do
        echo "$(date '+%H:%M:%S') $line"
    done | tee dieharder_results.txt

DATE=$(date)
echo "Completed at: $DATE"
cp dieharder_results.txt dieharder_results_$DATE.txt
echo "Results saved to: dieharder_full_results_$DATE.txt"

# Extract summary
echo ""
echo "=== SUMMARY ==="
grep -E "(PASSED|WEAK|FAILED)" dieharder_full_results_$DATE.txt | tail -20
