# Long-Distance Pedestrian Detection for Early Warning Systems

Detecting pedestrians on the road is a crucial skill for both human and AI drivers. In PH, about **7 pedestrians die** every day from traffic accidents. [[1](https://www.manilatimes.net/2025/04/29/business/real-estate-and-property/pedestrians-are-asking-for-a-more-walkable-ncr/2100738)]

## Different priorities...

Self-driving systems:
* Skill levels are still low.
* Priority is to detect pedestrians that are up close (ex. LiDAR for point clouds).

Human drivers:
* Already good at detecting things nearby.
* Benefits from **early warning systems** for pedestrians far away.

## What datasets are out there?

* Examples of pedestrians are almost always up-close.
* Some examples are not from realistic driving POVs.
* Some examples are not from traffic-based scenarios at all.

<img src=".github\assets\old_examples.png">

Images from an existing Roboflow dataset [[2](https://universe.roboflow.com/human-v2/human-dataset-v2)].

## Something new:

* 288 Google Street View images from within and around UP Diliman.
* Identifies both pedestrians & cyclists.
* Has both close-up and far-away examples for detection.

<img src=".github\assets\new_examples.png">

Images from this dataset, available at the `dataset` directory or at Roboflow [[3](https://universe.roboflow.com/human-v2/human-dataset-v2)].

## Results

<img src=".github\assets\old_results.png">

* **Model**: Roboflow 2.0 Object Detection (Fast)
* **Dataset**: [Human Dataset v2](https://universe.roboflow.com/human-v2/human-dataset-v2) (13,659 images)

<img src=".github\assets\new_results.png">

* **Model**: YOLO11s
* **Dataset**: This Dataset (288 images)

## Details

* **Data splits**: 256 train / 16 valid / 16 test
* **Model**: YOLO11s (small)
* **Training**:
  * 100 epochs
  * Data augmentation (HSV, flip, etc.)
  * Cosine LR
  * 960x960 images

<img src=".github\assets\training_stats.png">

## Citation

```bibtex
@misc{ long-distance-pedestrian-detection-from-a-driver-pov-mkmsn_dataset,
  title = { Long-Distance Pedestrian Detection from a Driver POV Dataset },
  type = { Open Source Dataset },
  author = { jpsalvahan },
  howpublished = { \url{ https://universe.roboflow.com/jpsalvahan/long-distance-pedestrian-detection-from-a-driver-pov-mkmsn } },
  url = { https://universe.roboflow.com/jpsalvahan/long-distance-pedestrian-detection-from-a-driver-pov-mkmsn },
  journal = { Roboflow Universe },
  publisher = { Roboflow },
  year = { 2025 },
  month = { nov },
  note = { visited on 2026-07-29 },
}
```