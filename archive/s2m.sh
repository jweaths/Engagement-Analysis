#!/bin/bash

# Script to tell the story of the Misadventure of a Clumsy Robot and collect ALMood data

# Specify the output file
OUTPUT_FILE="almood_data_s1a.csv"

# Header for the CSV file to denote data columns
echo "Timestamp,MoodValue" > $OUTPUT_FILE

# Interval in seconds between data collections
INTERVAL=2

# Estimated story duration in seconds
STORY_DURATION=60

# Function to tell the story
tell_story() {
    # Command to make Pepper tell the first story here
    qicli call ALTextToSpeech.say "\\VCT=50\\ 
In a quiet little town, lived Penelope, a penguin with a grand culinary ambition. Unlike her friends, who were content with fish, Penelope dreamed of creating the perfect pizza.
On her big day, Penelope set out to assemble her masterpiece. But in her excitement, she confused the tomato sauce with strawberry jam. As she slid the pizza into the oven, she hummed a tune, oblivious to the sweet mistake. 
When the timer dinged, Penelope, with a flourish, presented her creation to her friends. One bite, and there was a pause, then an eruption of laughter. Strawberry pizza was, surprisingly, not the worst thing they'd ever tasted.
Penelope's pizza adventure became the talk of the town, proving that sometimes, the best discoveries are accidents. And maybe, just maybe, penguins could be gourmet chefs after all."

}

# Function to collect ALMood data
collect_data() {
    END_TIME=$((SECONDS+STORY_DURATION))
    while [ $SECONDS -lt $END_TIME ]; do
        MOOD_DATA=$(qicli call ALMood.currentPersonState)
        TIMESTAMP=$(date +%s)
        echo "$TIMESTAMP,$MOOD_DATA" >> $OUTPUT_FILE
        sleep $INTERVAL
    done
}

# Start the story and data collection
tell_story &
collect_data
