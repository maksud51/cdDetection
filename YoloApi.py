import os
import base64
import subprocess
from PIL import Image
def detectDC(pathofimage, imgname, fname):
    mpath = "runs/train/1st_Training2/weights/"
    mname = "best.pt"
    subprocess.run(['python', "detect.py", '--weights',os.path.join(mpath, mname), '--source', str(pathofimage),'--name',str(fname)]) 
    image = open("runs/detect/"+str(fname)+"/"+imgname, 'rb')
    readbytes = image.read()
    encode = base64.b64encode(readbytes)
    return encode
