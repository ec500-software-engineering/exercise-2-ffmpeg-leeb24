# exercise-2-ffmpeg-leeb24
exercise-2-ffmpeg-leeb24 created by GitHub Classroom

# How to Run 
  ```
  $ python3 FFMPEG.py 
  ```
# Libraries Used 
- subprocess <br />
- threading <br />
```
pip2 install pytest
```
# Program Architecture 
  // Since my local enviroment was peaking 100% usage in 2 FFMPEG running, the program is designed to run 2 threads      concurrently. <br />
The main program makes 2 instances of threads which converts the video into hd720 and hd480. When the conversion function is invoked within the thread, it calls an subprocess to execute FFMPEG in the command terminal. ( hd480 conversion is done at the same time ). To make sure the output video is converted correctly, pytest function (test_validation.py) uses FFPROBE to obtain the video length of the original video and the converted video. Once both of the duration is obtained, the assertion method checks if those two values are the same and flags it if it does not pass the test.
