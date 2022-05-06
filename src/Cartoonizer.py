import cv2


class Cartoonizer:
	"""Cartoonizer effect
		A class that applies a cartoon effect to an image.
		The class uses a bilateral filter and adaptive thresholding to create
		a cartoon effect.
	"""
	def __init__(self):
		pass

	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		img_rgb = cv2.resize(img_rgb, (255,255))
		numDownSamples = 2	 # number of downscaling steps
		numBilateralFilters = 50 # number of bilateral filtering steps

		# -- STEP 1 --

		# downsample image using Gaussian pyramid
		img_color = img_rgb
		for _ in range(numDownSamples):
			img_color = cv2.pyrDown(img_color)
		# repeatedly apply small bilateral filter instead of applying
		# one large filter
		for _ in range(numBilateralFilters):
			img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

		# upsample image to original size
		for _ in range(numDownSamples):
			img_color = cv2.pyrUp(img_color)

		# -- STEPS 2 and 3 --
		# convert to grayscale and apply median blur
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		img_blur = cv2.medianBlur(img_gray, 3)

		# -- STEP 4 --
		# detect and enhance edges
		img_edge = cv2.adaptiveThreshold(img_blur, 255,
										cv2.ADAPTIVE_THRESH_MEAN_C,
										cv2.THRESH_BINARY, 9, 2)

		# -- STEP 5 --
		# convert back to color so that it can be bit-ANDed with color image
		(x,y,z) = img_color.shape
		img_edge = cv2.resize(img_edge,(y,x))
		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
		#cv2.imwrite("edge.png",img_edge)
		return cv2.bitwise_and(img_color, img_edge)

# tmp_canvas = Cartoonizer()

# file_name = "Screenshot.png" #File_name will come here
# res = tmp_canvas.render(file_name)
