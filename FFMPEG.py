import subprocess
import time
import multiprocessing as mp


def convert_video(video_input):
	parsed = video_input.split('.')
	output_vid = parsed[0]+'res.'+parsed[1]
	cmds =['ffmpeg', '-i',video_input ,'-s','hd720',output_vid]
	sub1 = subprocess.Popen(cmds)

def input_Queue(vidQ):
	start_time = time.time()

	results = [pool.apply(convert_video, args=(video,)) for video in vidQ]

	print("--- %s seconds ---" % (time.time() - start_time))


# Set-up Muti pool 
vidQueue = []
pool = mp.Pool(processes=2) ## 2 cores CPU
vidQueue.append("test.mp4")
vidQueue.append("test2.mp4")


input_Queue(vidQueue)

##Exercise 2 
## Make a code that takes in multiple video inputs and output converted video files.
## Make sure to make the code that does at least 2 videos concurrently
