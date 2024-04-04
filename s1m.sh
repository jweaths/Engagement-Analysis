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
Once-upon-a-time-in-a-world-not-too -different from ours, lived Robbie, 
a robot with a peculiar problem. Unlike his precise peers, Robbie had two left feet, figuratively speaking, making him the most clumsy robot in town. One sunny day, Robbie decided to bake a cake, a task that should have been simple. As he danced around the kitchen, mixing ingredients with a flourish only he could manage, things took a hilarious turn. With a twirl too many, he accidentally launched the flour bag into the ceiling fan, turning his kitchen into a winter wonderland. Robbie, covered in flour from head to toe, could only laugh at his snowy mishap. He realized then, maybe he wasn't cut out for baking, or twirling, but he definitely had a knack for making the best snow angels indoors. And so, Robbie's misadventure left everyone chuckling, reminding them that sometimes, it's our quirks that make the best stories. Who knew robots could be so... human?"

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
