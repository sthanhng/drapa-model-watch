import os
import sys
import glob
import time
import requests
import schedule


from config.default import cfg
sys.path.insert(0, cfg.WORKSPACE.BASE_DIR)


URL = "https://slack.com/api/files.upload"


def get_latest_file_and_send_to_slack():
	try: 
		list_of_files = glob.glob(cfg.MODELWATCH.DIR + "/*")
		latest_file = max(list_of_files, key=os.path.getctime)
		print("[INFO] Upload the file: {}".format(latest_file))
		data = {
			"channels": cfg.MODELWATCH.CHANNEL
		}
		files = {"file": open(latest_file, 'rb')}
		headers = {
			"Authorization": "Bearer " + cfg.MODELWATCH.TOKEN
		}
		requests.post(URL, data=data, files=files, headers=headers)
	except: 
		print("[INFO] No file to upload")


def run_():
	schedule.every(cfg.MODELWATCH.INTERVAL).minutes.do(get_latest_file_and_send_to_slack)

	while True:
		schedule.run_pending()
		time.sleep(1) 


if __name__ == "__main__":
	run_()
