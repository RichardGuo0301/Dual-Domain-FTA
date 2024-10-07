import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/exp/yolov8s-SOEP-GLSA.yaml')
    # model = YOLO('ultralytics/cfg/models/v8/yolov8s.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/visdrone.yaml',
                cache=False,
                imgsz=640,
                epochs=150,
                batch=4,
                close_mosaic=0,
                workers=4,
                device='0',
                optimizer='SGD', # using SGD
                amp=False,
                seed=3407, 
                # patience=0, # close earlystop
                # resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/visdrone',
                name='yolov8s-SOEP-GLSA',
                )