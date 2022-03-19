import numpy  as np
from skimage.util import map_array # best function ever

def TracksToLabels(data, labels): 
    """
    data numpy array from btrack
    labels is list of labels 
    
    Function will go through each frame and replace each untracked labeled mask with a new order label, skipping missing ones
    
    Return: list of tracked labels (as input labels) -> can be easily converted to 3D array with np.array()
    """
    new_labels = []
    num_frames = len(labels)
    corr_by_frame = {frame: {'old_labels':[], 'new_labels':[]} for frame in range(num_frames)}

    height = labels.shape[1]
    width = labels.shape[2]

    for row in data:
        track_id = int(row[0])
        frame = int(row[1])
        xcoord = np.min([int(row[2]), height-1])
        ycoord = np.min([int(row[3]), width-1])
        current_mask = labels[frame]
        label_to_replace = current_mask[xcoord, ycoord]
        if label_to_replace == 0:
            continue
        else:
            corr_by_frame[frame]['old_labels'].append(label_to_replace)
            corr_by_frame[frame]['new_labels'].append(track_id)
    for frame in corr_by_frame.keys():
        old = np.array(corr_by_frame[frame]['old_labels'])
        new = np.array(corr_by_frame[frame]['new_labels'])
        new_labels.append(map_array(labels[frame], old, new))
    return new_labels

def SelectLabels(array_2d, largest_label):
    """
    Return Boolean 1d array with True if the label is present in a array or False otherwise
    """
    return np.isin(np.arange(0, largest_label+1), array_2d)