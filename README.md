# Long-Distance Pedestrian Detection for Early Warning Systems

This repository contains the code and dataset used in a mini-project on object detection for UP Diliman's CS 176 Computer Vision class.

## Motivation

Detecting pedestrians on the road is a crucial skill for both human and AI drivers. In the Philippines, around **7 pedestrians die** every day from traffic accidents [[1](https://www.manilatimes.net/2025/04/29/business/real-estate-and-property/pedestrians-are-asking-for-a-more-walkable-ncr/2100738)]. All drivers struggle with **long-distance pedestrian detection**, due to the limits of either eyesight or hardware (i.e. LiDAR in self-driving cars).

While this could be solved with computer vision, existing datasets are limited by examples where:
* Pedestrians are almost always up-close.
* POV is not from a driver's perspective.
* Scenarios are not traffic-based at all.

<figure>
  <img src="assets\old_examples.png">
  <figcaption style="text-align: center;">Examples from a Roboflow dataset [<a href="https://universe.roboflow.com/human-v2/human-dataset-v2">2</a>].</figcaption>
</figure>

To address this gap, we construct a new dataset composed of 288 Google Street View images from within and around UP Diliman. It identifies both pedestrians and cyclists, and has both close-up and far-away examples for detection.

<figure>
  <img src="assets\new_examples.png">
  <figcaption style="text-align: center;">Examples from this dataset.
</figure>

## Dataset

The dataset used in the project is available in this repository, as well as in Roboflow: https://universe.roboflow.com/jpsalvahan/long-distance-pedestrian-detection-from-a-driver-pov-mkmsn. The dataset is split into:
* **Training**: 256 images
* **Validation**: 16 images
* **Test**: 16 images

## Training

We compare Ultralytics' YOLO11s trained on this dataset (256 images) and a model trained on the Human Dataset v2 (10,939 images) [<a href="https://universe.roboflow.com/human-v2/human-dataset-v2">2</a>] with an image from the test split:

<figure>
  <img src="assets\old_results.png">
  <figcaption style="text-align: center;">Result with Roboflow 2.0 Object Detection trained on Human Dataset v2.
</figure>

<figure>
  <img src="assets\new_results.png">
  <figcaption style="text-align: center;">Result with YOLO11s trained on this dataset.
</figure>

The weights for this YOLO11s model can be found in this repository. To train the model from scratch, simply run all cells in `trainer.ipynb`. Some additional training details:
  * 100 epochs
  * Data augmentation (HSV, flip, etc.)
  * Cosine LR schedule
  * 960 x 960 images

## Demo

`app.py` launches a live demo of the YOLO11s model in Gradio. This, along with OBS Studio, was used to showcase the model's capability on Google Street View.

## Citation

```bibtex
@misc{
    salvahan2025longdistance,
    title        = {Long-Distance Pedestrian Detection for Early Warning Systems},
    author       = {John Paul B. Salvahan},
    howpublished = {\url{https://github.com/JPSalvahan/LongDistancePedestrian}},
    year         = {2026},
    note         = {Project originally created in 2025.}
}
```
