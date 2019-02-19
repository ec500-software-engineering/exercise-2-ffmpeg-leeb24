
# import os
# import signal
import subprocess
# import timeit
import time
import multiprocessing as mp

vidQ = []


def convert_video(video_input):
	parsed = video_input.split('.')
	output_vid = parsed[0]+'res.'+parsed[1]
	print(output_vid)
	cmds =['ffmpeg', '-i',video_input ,'-r' ,'30', '-s','hd720',output_vid]
	sub1 = subprocess.Popen(cmds)

	sub1.wait()
	sub1.kill()
	print("Sub1 killed")
 	

# Set-up Muti pool 
pool = mp.Pool(processes=2) ## 2 cores CPU

vidQ.append("test.mp4")
vidQ.append("test2.mp4")

start_time = time.time()
results = [pool.apply(convert_video, args=(video,)) for video in vidQ]

print("--- %s seconds ---" % (time.time() - start_time))
