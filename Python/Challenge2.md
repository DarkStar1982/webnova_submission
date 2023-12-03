# Exodus Orbital Python SDK for the satellite API

## Second challenge
Can you write the code that identifies the airplanes in the picture?
![tiff file](./img.jpg)

## results 
![results.png](./results.png)
![results-zoom.png](./results-zoom.png)
[data.cvs](./data_filtered.cvs)


# First model object detection with fast-rccn 
## Please refer the ```./challenge2-detectron2.ipynb``` file.
file [challenge2 detectron](./challenge2-detectron2.ipynb)

Used model: [model fast-rcnn](./model_0024999.pth)
you can download it from [RarePlanes repo](https://github.com/jdc08161063/RarePlanes/tree/master/models)

Framework Detectron V2 from [Facebook Research](https://github.com/facebookresearch/detectron2)

The results are relatively good given that we do not have any specific set of data to train the model.

![result](./detectron-raw.png)

A large threshold of  `0.7` was applied since we will use another model to filter false positives.

## Second model classification: classic dense CNN.
## Please refer the ```./challenge2-CCN.ipynb``` file.

file [challenge 2 CCN](./challenge-2-CNN.ipynb)

Using first model as a ROI provider we refine results removing false positives.
Model file [model](./model.keras) Trained on goolgle colab free tier GPU.
This model is very effective since it was trained with data dimilar to the provided image.
Trained on [Planes in Satellite Imagery](https://www.kaggle.com/datasets/rhammell/planesnet/data)

Final result in `result.tiff` and `./data_filtered.csv` files.

## Used tools:
- ML: 
    - Detectron v2 from [Facebook Research](https://github.com/facebookresearch/detectron2) rareplanes dataset and initial model.
    - CCN model with Tensorflow and Keras.
    - [rareplanes data](https://github.com/jdc08161063/RarePlanes)
    - [Planes in Satellite Imagery](https://www.kaggle.com/datasets/rhammell/planesnet/data)
- SDK:
    - Python
    - Jupyter note book
    - Google Colab T4 GPU, free tier

- OS:
    - Ubuntu 
    - Windows 11 with WSL2

## What's next
- Futher train models on more specific dataset
- Merge both model [resulting in a YOLO like final model]
- Improve the docs 
