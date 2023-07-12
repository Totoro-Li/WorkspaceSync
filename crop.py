import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

# 读取事件文件
with open('events.txt', 'r') as f:
    lines = f.readlines()

# 读取图像大小
width, height = map(int, lines[0].split())

# 初始化热力图
heatmap = np.zeros((height, width))

# 生成热力图
for line in lines[1:]:
    t, x, y, p = line.split()
    x, y = int(x), int(y)
    heatmap[y, x] += 1

# 显示热力图
plt.imshow(heatmap, cmap='hot')
plt.show()

# 阈值设定为热力图中值的2倍，也可以根据实际情况调整
threshold = 2 * np.median(heatmap)

# 使用阈值分割热力图，生成二值图像
binary_img = (heatmap > threshold).astype(np.uint8)

# 查找连通区域
labeled_img, num = label(binary_img, connectivity=2, return_num=True)

# 读取ground truth和重构图片
gt_img = np.load('a.npy')
recon_img = cv2.imread('b.png', cv2.IMREAD_GRAYSCALE)

# 找到最大的连通区域
max_area = 0
max_region = None
for region in regionprops(labeled_img):
    if region.area > max_area:
        max_area = region.area
        max_region = region

# 对最大的连通区域，生成边界框并计算PSNR
if max_region is not None:
    minr, minc, maxr, maxc = max_region.bbox
    gt_patch = gt_img[minr:maxr, minc:maxc]
    recon_patch = recon_img[minr:maxr, minc:maxc]
    psnr = 10 * np.log10(255**2 / np.mean((gt_patch - recon_patch) ** 2))
    print(f'PSNR for region {max_region.label}: {psnr}')
