<font class=center size=5>**3D-FUTURE: 3D FUrniture shape with TextURE**</font>

## 1. Overview
<font class=center>![enter image description here](https://img.alicdn.com/tfs/TB1HTSfz4v1gK0jSZFFXXb0sXXa-1999-1037.png)</font>

The 3D CAD shapes in current 3D benchmarks are mostly collected from online model repositories. Thus, they typically have insufficient geometric details and less informative textures, making them less attractive for comprehensive and subtle research in areas such as high-quality 3D mesh and texture recovery. We presents 3D Furniture shape with TextURE ([3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-future)): a richly-annotated and large-scale repository of 3D furniture shapes in the household scenario. 3D-FUTURE contains 20,240 clean and realistic synthetic images of 5,000 different rooms. There are 16,563 unique detailed 3D instances of furniture with high-resolution textures. Experienced designers developed the room scenes, and the 3D CAD shapes in the scene are used for industrial production. More details can be found in our <a href='https://arxiv.org/pdf/2009.09633.pdf?spm=5176.14208604.0.0.78253cf77YoOGy&file=2009.09633.pdf'>report</a>.

<br>

## 2. Data Description
3D-FUTURE provides 20,240 realistic indoor images and the associated 16,563 unique 3D furniture models with rich geometry details and informative textures. We render these images via one of the most advanced industrial 3D rendering engines based on 5,000 exquisite room scenes developed by experienced designers. The 3D furniture shapes are used for modern industrial productions and havefine-grained geometry and texture related attributes such as category, style, theme, and material. Further, 3D-FUTURE offers instance segmentation annotation and the rendering information, including six degrees of freedom (6DoF) pose and camera field of view (FoV).

### 2.1. Download
The 3D-FUTURE benchmark is provided by Alibaba Topping Homestyler, and organized by Alibaba Tao Technology Department. If you would like to download the 3D-FUTURE data, please send the [3D-FUTURE Terms of Use](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud202004171628_60052.html?spm=5176.14208604.0.0.26b13cf7ro5iqC) to us at tianchi_open_dataset@alibabacloud.com as an attachment with your name, PI's (or advisor's) name, and affiliation. If you have not received a response within a week, it is likely that your email is bouncing - please check this before sending repeat requests. Please check the [news](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-future?spm=5176.14208320.0.0.46053cf7DVpJBh) for updates to the data release.

### 2.2. Data Format
The 3D-FUTURE dataset includes rendering scenes file (3D-FUTURE-scene.zip) and furniture shapes file (3D-FUTURE-model.zip).

#### 2.2.1 rendering scenes:
The downloaded rendering scenes file should have the following form:
```
3D-FUTURE-scene.zip
├── train
│   ├── image
|   │   ├── 0000000.jpg
|   │   ├── 0000001.jpg
│   │   ├── ...
│   ├── idmap
|   │   ├── 0000000.png
|   │   ├── 0000001.png
│   │   ├── ...
├── test
│   ├── image
|   │   ├── 0000000.jpg
|   │   ├── 0000001.jpg
│   │   ├── ...
│   ├── idmap
|   │   ├── 0000000.png
|   │   ├── 0000001.png
│   │   ├── ...
├── GT
│   ├── model_infos.json
│   ├── train_set.json
│   ├── test_set.json
```


* model_info.json: describes the style, theme, material, and category of each furniture, except lights.
* train_set.json/test_set.json: is based on the [COCO format](https://cocodataset.org/#format-data), as follows:
```
train_set.json / test_set.json:
{
    categories: [
        {
            id: int, 
            category_name: str, 
            fine-grained category name: str, 
        },
        ...
    ]
    images: [
        {
            id: int, 
            width: int, 
            height: int, 
            file_name: str, 
        },
        ...
    ], 
    annotations: [
        {
            id: int, 
            image_id: int, 
            category_id: int, 
            segmentation: RLE or [polygon], 
            area: float, 
            bbox: [x,y,width,height], 
            model_id: str, 
            texture_id: str,
            pose: list
            fov: float,
            style: str,
            theme: str,
            material: str
        },
        ...
    ], 
}
```

#### 2.2.2 furniture shapes:
The downloaded furniture shapes file should have the following form:
```
3D-FUTURE-model.zip
├── categories.py
├── model_info.json
├── 3D-FUTURE-model
│   ├── 209fdbd6-b95d-4d11-a05e-8fcefa32a60d
│   │   ├── image.jpg
│   │   ├── normalized_model.obj
│   │   ├── raw_model.obj
│   │   ├── texture.png
│   │   ├── model.mtl
│   ├── 209fdbd6-b95d-4d11-a05e-8fcefa32a60d
│   │   ├── image.jpg
│   │   ├── normalized_model.obj
│   │   ├── raw_model.obj
│   │   ├── texture.png
│   │   ├── model.mtl
│   │...
```

* categories.py: includes furniture attributes (e.g. style, material, theme) and categories used in 3D-FRONT dataset, which are given by our experienced designers.
* model_info.json: describes the style, theme, material, and category of each furniture, except lights.

<br>

## 3. Citation
If you use our dataset or code, please consider to cite our reports:
```  
@article{fu20203dfuture,
    title={3D-FUTURE: 3D Furniture shape with TextURE},
    author={Fu, Huan and Jia, Rongfei and Gao, Lin and Gong, Mingming and Zhao, Binqiang and Maybank, Steve and Tao, Dacheng},
    journal={arXiv preprint arXiv:2009.09633},
    year={2020}
}
```