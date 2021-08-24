import json
import os
from glob import glob

files = glob(os.path.join("output", '*'))
images = []
extension = ".json"
files = [file for file in files if file.lower().endswith(extension)]

print(files)

data = ""
for file in files:
	d= json.load(open(file))["data"]
	for i in d:
		if i["type"]=="text" and i["entity"]:
			data += i["text"]
			if i["label"] == "pan_id--0_0" or i["label"] == "parent_en--0_2" or i["label"] == "name_en--0_2":
				data+= "_"
			else:
				data+=" "
	data+="\n"
	
data = str(data)
file = open("data.txt","w")
file.write(data)
print(data)