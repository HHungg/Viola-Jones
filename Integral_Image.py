import numpy as np

def to_integral_image(img_arr):
	row_sum = np.zeros(img_arr.shape)
	integral_image_arr = np.zeros((img_arr.shape[0]+1, img_arr.shape[1]+1))
	for y in range(img_arr.shape[1]):
		for x in range(img_arr.shape[0]):
			row_sum[x, y] = row_sum[x,y-1] + img_arr[x, y]
			integral_image_arr[x+1, y+1] = integral_image_arr[x, y+1] + row_sum[x, y]
	return integral_image_arr

def sum_region(integral_image_arr, top_left, bottom_right):
	if top_left == bottom_right:
		return integral_image_arr[top_left]
	top_right = (top_left[0], bottom_right[1])
	bottom_left = (bottom_right[0], top_left[1])
	return integral_image_arr[bottom_right] - integral_image_arr[top_right] - integral_image_arr[bottom_left] + integral_image_arr[top_left]