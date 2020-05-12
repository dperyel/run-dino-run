import cv2

def find_edges(img):
    return cv2.Canny(img, threshold1=0, threshold2=255)

def group_features(binary_canvas, grouping_diapason=10):
    # list of (x, width)
    location_group = []
    step = grouping_diapason
    _, region_w = binary_canvas.shape
    located_group = False
    steps = region_w // step

    for i in range(steps):
        start = step * i
        area_to_check = binary_canvas[:, start:start+step]
        if area_to_check.max() > 0:
            if located_group:
                index = len(location_group) - 1
                group_start, group_width = location_group[index]
                location_group[index] = (group_start, group_width + step)
            else:
                group_start = start
                group_width = step
                # trim a front of the group
                for c_index, column in enumerate(area_to_check.T):
                    if column.max() > 0:
                        group_start += c_index
                        group_width -= c_index
                        break
                
                located_group = True
                location_group.append((group_start, group_width))
        else:
            located_group = False
    
    return location_group
