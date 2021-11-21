# Speech Emotion Recognition

<div align="center">
<Img src="/Imgs/robotfeelings.gif" width="54%"/>
</div>
  
## Objective
As emotions play a vital role in communication, the detection and analysis of the same is of vital importance in today’s digital world of remote communication. Emotion detection is a challenging task, because emotions are subjective. There is no common consensus on how to measure or categorize them. 

There are three classes of features in a speech :

- The lexical features (the vocabulary used)
- The visual features (the expressions the speaker makes) 
- The acoustic features (sound properties like pitch, tone, jitter, etc.)

The problem of speech emotion recognition can be solved by analysing one or more of these features. Choosing to follow the lexical features would require additional step of text extraction from speech,similarly analysing visual features would require the excess to video of the conversations which might not be feasible in every case.

While the analysis on the acoustic features can be done in real-time while the conversation is taking place as we’d just need the audio data for accomplishing our task.The main goal of this project is to build a speech emotion detection system,which can optimally classify a user's speech by analysing the patterns in audio.


## Data collection

For this project we would need a bunch of sample audio files with varying emotional intensities. We'll we use the RAVDESS dataset which contains 1440 files: 60 trials per actor x 24 actors = 1440 audio files . The RAVDESS contains 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. 

<div align="center">
<Img src="/Imgs/ravdess.png" width="85%"/>
</div>
<br>

Speech emotions includes : (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised)
The entire dataset is 24.8GB from 24 actors, but we’ll use a dataset with lowered the sample rate on all the files, you can download it [here](https://drive.google.com/file/d/1wWsrN2Ep7x6lWqOXfr4rpKGYrJhWc8z7/view).


## Model Training



## To run (Locally)


## Web Interface


### References :
























