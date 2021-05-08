# Super Smash Bros. Ultimate Image Recognition

For an in depth overview of this project watch my video:
https://youtu.be/zjRzunCeB0s

ssbu_image_recognition is used to detect what fighters are doing in smash. There is a lot of work to be done still but when fully developed this will be a great tool for learning habits of different players and improving in the game.

It is currently using Opencv tools for image recognition and training models. I'm not sure that I made the right choice in going with opencv. I think the next step in this project is to do some experimentation with Tensorflow and see if that gives me better results. 

I also need to optimize the method of collecting data. My current method did not turn out as streamlined as I was hoping for. Being able to quickly collect quality data would be super helpful in training accurate models.

## Installation

There are three parts to this project:
- Collect good training data
- Train Cascade models
- Apply models to do image recognition

#### Clone Repository

Run this command in your command prompt or terminal.

```bash
git clone https://github.com/pngsavvy/ssbu_image_recognition.git
```

### Data Collection

Enter the collect training images folder and run the program. You can use tools in this folder to collect good data for training. For more detail watch my video https://youtu.be/zjRzunCeB0s.

### Training Models

To train the models you will need to download open cv version 3.4.3 from here: 

https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.4.3/

Run the .exe file to extract the contents. It will extract an opencv folder. The files that we will be using from this folder are:

opencv\build\x64\vc15\bin\opencv_createsamples.exe
opencv\build\x64\vc15\bin\opencv_annotation.exe
opencv\build\x64\vc15\bin\opencv_traincascade.exe

The first step to training the models is to runthe opencv_annotations.exe file. Here is the command that I used for this:

c:\Projects\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=right_smash.txt --images=Screenshots/Attacks/Smashes/Right_Smash/

Watch my video for more details on how this works.

You will then need to run:
c:\Projects\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info right_smash.txt -w 24 -h 24 -num 10000 -vec right_smash.vec

and then:
c:\Projects\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascades/right_smash/ -vec right_smash.vec -bg right_smash_neg.txt -w 24 -h 24 -numPos 100 -numNeg 200 -numStages 10 -precalcValBufSize 6000 -recalcIdxBufSize 6000 -maxFalseAlarmRate .001 -minHitRate .999

I explain all of these commands in my video.

### Image Recognition

You can either use screen capture or a video file to do image recognition on. This is up to you. When you run the program first select the character that you would like to track and then click the space bar or enter. If the tracker looses track of the character, the next time that Mario jabs it will reset the tracker to where the jab is recognized at.

#### If you have any questions let me know. Leave a comment on my video.
