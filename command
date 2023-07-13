##Changes
setup.py line-50 ON 
yolox/data/data_augments.py line-189 OFF
tools/demo_track.py line-160 OFF

##demo test command
python tools/demo_track.py video -f exps/example/mot/yolox_s_mix_det.py -c pretrained/bytetrack_s_mot17.pth.tar --fuse --save_result
(delete '--fp16'. Why? https://blog.csdn.net/dark5669/article/details/79976015 <GPU架构中的半精度fp16与单精度fp32计算>)

##usb webcam test command
python tools/demo_track.py webcam -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fuse --save_result --camid 1

##my own video in path
python tools/demo_track.py video -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fuse --save_result --path videos/video0.mp4

##my own images in path
python tools/demo_track.py image -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fuse --save_result --path ~/Desktop/EPFL-RLC_dataset/frames/cam0

##multiview videos
python tools/demo_track.py 2videos -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fuse --save_result --video1 videos/video0.mp4 --video2 videos/video1.mp4

##multiview webcams
python tools/demo_track.py 2webcams -f exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --fuse --save_result --cam1 0 --cam2 2

##others
torch2trt has not been installed yet
