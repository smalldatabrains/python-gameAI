import keras
import numpy as np
import cv2
import os
import subprocess
import time
import mss
import pyautogui
from directkeys import PressKey, W, A, S, D



games=sorted(os.listdir(os.getcwd()))

#launch game
# emulator="snes9x-gtk"
# os.system(emulator+' '+'--window-size=600x600'+' '+'"'+games[1]+'"' )



#capture game

with mss.mss() as sct:
	while True:
		last_time=time.time()
		monitor_number=2
		mon=sct.monitors[monitor_number]
		monitor = {'top': mon['top'] + 10,'left': mon['left'],'width': 550,'height': 600,'mon': monitor_number}
		img = np.array(sct.grab(monitor))
		cv2.imshow('Game',img)
		print('fps: {0}'.format(1 / (time.time()-last_time)))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break


#building training


