import subprocess
import time
import multiprocessing as mp
import queue
import threading
import validation as test 

def convert_video_720p(video_input):
	
		parsed = video_input[0].split('.')
		output_vid = parsed[0]+'res.'+parsed[1]
		cmds =['ffmpeg', '-i',video_input[0] ,'-s','hd720',output_vid]
		subprocess.call(cmds)
		test.test_duration(video_input[0],output_vid)

		return print("Conversion Finished")

def convert_video_480p(video_input):

		parsed = video_input[0].split('.')
		output_vid = parsed[0]+'res.'+parsed[1]
		cmds =['ffmpeg', '-i',video_input[0] ,'-s','hd480',output_vid]
		subprocess.call(cmds)

		return print("Conversion Finished")

# def input_Queue(vidQ):
# 	start_time = time.time()
# 	results = [pool.apply(convert_video_720p, args=(video,)) for video in vidQ]
# 	print(results)
# 	print("--- %s seconds ---" % (time.time() - start_time))
# def put_to_Queue720():
# 	vidQueue720.put(["test.mp4",720])
# 	convert_video_720p(vidQueue720)

# def put_to_Queue480():
# 	vidQueue480.put(["test2.mp4",480])
# 	convert_video_480p(vidQueue480)


# Set-up Muti pool 

vidQueue720 = []
vidQueue480 = [] 
pool = mp.Pool(processes=2) ## 2 cores CPU
vidQueue720.append(["test.mp4",720])
vidQueue480.append(["test2.mp4",480])

start_time = time.time()

thread1 =threading.Thread(target=convert_video_720p,args=(vidQueue720))
thread2 =threading.Thread(target=convert_video_480p,args=(vidQueue480))

thread1.start()
thread2.start()


print("--- %s seconds ---" % (time.time() - start_time))


##Exercise 2 
## Make a code that takes in multiple video inputs and output converted video files.
## Make sure to make the code that does at least 2 videos concurrently
