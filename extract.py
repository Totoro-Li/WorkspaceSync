import os
import cv2
import numpy as np

dataset_dir = "RESBLUR"  # Replace with your path to the RESBlur dataset
output_folder = "RESBLUR_OUT"  # Replace with your desired output directory


def process_resblur_gt(scenario_path, output_folder):
    assert "frame_clip" in os.listdir(scenario_path)
    frame_clip_path = os.path.join(scenario_path, "frame_clip")

    # Create GT folder
    gt_folder = os.path.join(output_folder, 'gt')
    os.makedirs(gt_folder, exist_ok=True)

    # Parse start timestamps from the ground truth image file names
    gt_image_files = sorted(glob.glob(os.path.join(frame_clip_path, '*.png')))
    timestamps = np.array([int(os.path.basename(f).split('_')[0].split('-')[0][1:]) for f in gt_image_files])
    timestamps = timestamps * 1e-9  # Convert to seconds

    # Extract and save ground truth images
    for image_file, timestamp in zip(gt_image_files, timestamps):
        image = cv2.imread(image_file)
        image_path = os.path.join(gt_folder, f"image_{timestamp:.0f}.png")
        cv2.imwrite(image_path, image)

    # Save timestamps to a timestamps.txt in seconds, each line is a timestamp
    timestamps_path = os.path.join(gt_folder, 'timestamps.txt')
    np.savetxt(timestamps_path, timestamps, fmt='%.10f')


if __name__ == "__main__":
    for scenario in os.listdir(dataset_dir):
        scenario_path = os.path.join(dataset_dir, scenario)
        output_folder_path = os.path.join(output_folder, scenario)
        if os.path.isdir(scenario_path):
            process_resblur_gt(scenario_path, output_folder_path)