# hpviton-preprocess
# intorduction
In order to use our uploaded characters for virtual fitting, we need to perform the following steps on the character images, and finally generate the following folders:
![Capture d’écran du 2023-12-27 14-29-17](https://github.com/fcyx/hpviton-preprocess/blob/main/image/total.png)


# openpose_img and  openpose_img
```
cd pytorch_openpose_body_25
python demo.py
```
Place the Human images in image and output them in the folder output

# image-densepose
```
cd detectron2/projects/DensePose
pip install av>=8.0.3 opencv-python-headless>=4.5.3.56 scipy>=1.5.4
python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl image_path dp_segm -v
```

# image-parse-v3
```
cd Human-Parsing
python3 simple_extractor.py --dataset 'lip' --model-restore 'lip_final.pth' --input-dir 'input-folder' --output-dir 'output-folder'
```
# image-parse-agnostic-v3.2
It is worth mentioning that in this step, we need to put all the outputs from the first few steps as inputs into test_hr/test/
```
cd test_hr
python test_ag.py
```
# agnostic-v3.2
we need to put all the outputs from the first few steps as inputs into test_hr/test1/
```
cd test_hr
python test_huar.py
```
