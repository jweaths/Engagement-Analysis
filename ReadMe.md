# Tales From a Tin Heart: A Human-Robot Interaction Experiment

## Description

This project uses several Python libraries to connect to Pepper 2.9 and execute AL commands from LibQi. The main libraries used are Qi, OpenCV, Numpy, Pandas, and Wordcloud. We utlize ALMood, ALVideoDevice, ALTextToSpeech, and ALAnimatedSpeech from Naoqi to perfrom the Human-Robot interaction. The dependency on the Qi library needs to be built and installed on Ubuntu.


## Installation

To install the required Python libraries and other dependencies, please run the following command:

```bash
pip install -r requirements.txt

```

### Important: For the Qi library dependency and learning how to connect to Pepper using Qi methods, please refer to the instructions in Qi_Install_Guide.docx 


## Running

### To Run Bash Scripts (Ex: run0.sh)
For detailed experiment steps. see 'exeriment_steps.docx' in the root directory.
For running the bash scripts, which connect Pepper to a qi session and run the necessary packages:

ensure the current file is executable and then run using these commands:

```bash
chmod +x <current executable>
./<current executable>

```

For each experiement session, one of the 4 run#.sh scripts is chosen in sequential order. Each run#.sh script runs a different order of the two stories in alternating styles (for example, run2.sh runs Robbie's story in Animated style first, and then Penelope's story in Monotone style second. ) 


## Acknowledgements

To connect to the Pepper robot using the qi library, we referenced this stack overflow post:

https://stackoverflow.com/questions/77987028/how-can-i-connect-to-pepper-naoqi-2-9-via-libqi-python

## Self-Evaluation:

Our initial proposal was to conduct a real-time adaptive storytelling experiment with Pepper, tracking a participant’s social signals and adjusting the story using a GPT in real-time to see if we could produce a significant improvement in the storytelling experience. However, after being introduced to Pepper we realized this was out of scope. We created a new proposal which was approved by Dr. Lim in-person (attached as ‘Proposal 2’). In this iteration, our idea was to measure the mirroring response from the human participant, but upon further refinement we decided to focus strictly on valence and affect. We chose to simplify things because connecting to Pepper was initially giving us major difficulties and the goal of measuring “human engagement” rather than “mirroring response” was clearer and more straightforward. We believe this was the correct choice because we ended up with statistically significant conclusions that were measurable. Ultimately, we did not use the video data and instead used Pepper’s built-in functions to measure the human participant’s response due to time constraints. While this was an overall simpler idea, we believe our findings are valuable and contribute to the knowledge surrounding human-robot interaction.
