import queue
import os
import signal
import subprocess
import timeit
import time
import multiprocessing as mp

vidQ = queue.Queue()


def convert_video(video_input, video_output):

    cmds = ['ffmpeg', '-i',video_input ,'-r' ,'30', '-s','hd720',video_output]
    cmds2 = ['ffmpeg', '-i',video_input ,'-r' ,'30', '-s','hd720','res.mp4']
    sub1 = subprocess.Popen(cmds)
    sub2 = subprocess.Popen(cmds2)

    sub1.wait()
    sub2.wait()


    sub1.kill()
    print("Sub1 killed")
    sub2.kill()
    print("Sub2 killed")



start_time = time.time()
convert_video('test.MP4', 'testres.mp4')
print("--- %s seconds ---" % (time.time() - start_time))
