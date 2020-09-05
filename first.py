import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

source_image = imageio.imread('Adolf-Hitler-1933.jpg')
#driving_video = imageio.mimread('shwetabh.mp4',memtest=False)
driving_video = imageio.mimread('jadoo.mp4',memtest=False)


#Resize image and video to 256x256

source_image = resize(source_image, (256, 256))[..., :3]
driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]


from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='vox-adv-cpk.pth.tar')
                            
from demo import make_animation
from skimage import img_as_ubyte

predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

#save resulting video
imageio.mimsave('generated.mp4', [img_as_ubyte(frame) for frame in predictions])
#video can be downloaded from /content folder
                            
