import cv2
import numpy as np

def generate_heatmap(event_data):
    """
    Generate heatmap from event data.

    This function assumes that the event data is a 2D matrix, where the value of each cell represents 
    the frequency of events at the corresponding location.

    Parameters:
        event_data: 2D numpy array with event frequencies.

    Returns:
        2D numpy array representing the heatmap.
    """

    # Normalize the event data to the range [0, 255] for image processing
    heatmap = ((event_data - np.min(event_data)) / (np.max(event_data) - np.min(event_data))) * 255
    return heatmap.astype(np.uint8)


def find_blur_regions(heatmap, threshold_ratio=0.5):
    """
    Find blur regions in heatmap.

    This function uses a threshold to separate high-frequency areas (potential blur regions) 
    and low-frequency areas. The threshold is calculated as the mean value of the heatmap 
    multiplied by threshold_ratio.

    Parameters:
        heatmap: 2D numpy array representing the heatmap.
        threshold_ratio: float, threshold = mean(heatmap) * threshold_ratio.

    Returns:
        List of tuples, where each tuple represents a blur region in the format (x, y, w, h).
    """

    # Threshold the heatmap
    _, thresh = cv2.threshold(heatmap, np.mean(heatmap)*threshold_ratio, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded heatmap
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Generate bounding boxes for the contours
    blur_regions = [cv2.boundingRect(contour) for contour in contours]

    return blur_regions


def crop_blur_regions(image, blur_regions):
    """
    Crop blur regions from image.

    Parameters:
        image: 2D numpy array representing the image.
        blur_regions: List of tuples, where each tuple represents a blur region in the format (x, y, w, h).

    Returns:
        List of 2D numpy arrays, each representing a cropped blur region.
    """

    cropped_regions = [image[y:y+h, x:x+w] for x, y, w, h in blur_regions]
    return cropped_regions

# Suppose `event_data` is your 2D event frequency data and `image` is your image
heatmap = generate_heatmap(event_data)
blur_regions = find_blur_regions(heatmap)
cropped_regions = crop_blur_regions(image, blur_regions)
