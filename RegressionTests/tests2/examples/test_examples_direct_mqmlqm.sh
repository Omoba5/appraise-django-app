#!/usr/bin/env bash -x

# Exit on error
set -eo pipefail

prefix=example_direct_mqmesa

# Create campaign from Examples/DirectMQM
$APPRAISE_MANAGE StartNewCampaign $APPRAISE_EXAMPLES/DirectMQM/manifest_esa.json \
    --batches-json $APPRAISE_EXAMPLES/DirectMQM/batches_wmt23_en-de.json \
    --csv-output $prefix.users.csv

# Check generated credentials
test -e $prefix.users.csv
diff $prefix.users.csv $prefix.users.csv.expected > $prefix.diff

# Make a few annotations
for score in $( seq 10 10 50 ); do
    $APPRAISE_MANAGE MakeAnnotation engdeu0f01:56719686 Document $score --mqm '[{"start_i": 0, "end_i": 50, "severity": "major"}]'
done

# Export scores without timestamps and compare with the expected output
# Escape quotes in MQM fields
$APPRAISE_MANAGE ExportSystemScoresToCSV example15esa | sed "s/, /| /g" | cut -f-10 -d, | sed "s/| /, /g" > $prefix.scores.csv
diff $prefix.scores.csv $prefix.scores.csv.expected

# Exit with success code
exit $EXIT_CODE_SUCCESS
