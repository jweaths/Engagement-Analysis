#!/bin/bash

# Script to collect ALMood data and log it in a MATLAB-friendly format

# Specify the output file
OUTPUT_FILE="almood_data.csv"

# Header for the CSV file to denote data columns
echo "Timestamp,MoodValue" > $OUTPUT_FILE

# Interval in seconds between data collections
INTERVAL=2

# Function to collect ALMood data
collect_data() {
    # Replace this command with the actual qicli command to get mood data
    

    MOOD_DATA=$(qicli call ALMood.currentPersonState)

    # Assuming MOOD_DATA directly gives a numerical mood value
    # Get the current timestamp in seconds since the epoch, which MATLAB can easily convert
    TIMESTAMP=$(date +%s)

    # Log the data with timestamp
    echo "$TIMESTAMP,$MOOD_DATA" >> $OUTPUT_FILE
}

# Main loop
$qicli call 
while true; do
    collect_data
    sleep $INTERVAL
done
