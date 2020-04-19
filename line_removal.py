'''importing the liraries file'''
from lib import*

class open:
    def __init__(self,path,name):
    #  super().__init__(*args, **kwargs)
        self.file_path = path #takes apramter from flask_api.py
        self.name = name  #takes apramter from flask_api.py
    '''path function performs morphological operations on image'''
    '''to detect the boxed image and apply countour plotting on them.....'''
    '''it returns the image inside the box'''
    def path(self):
        img = self.file_path
        img = cv2.imread(img, 0)

        # Thresholding the image
        (thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|     cv2.THRESH_OTSU)

        # Invert the image
        img_bin = 255-img_bin 
        cv2.imwrite("Image_bin.jpg",img_bin)


        # Defining a kernel length
        kernel_length = np.array(img).shape[1]//80
        
        # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
        # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
        # A kernel of (3 X 3) ones.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        ''''Erosion and dilution is applied on the image.....'''
        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)

        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)

        # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
        alpha = 0.5
        beta = 1.0 - alpha
        # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
        img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
        img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
        (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


        # Find contours for image, which will detect all the boxes
        contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Sort all the contours by top to bottom.
        # contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")

        name = self.name
        dir= './'
        for c in contours:
                # Returns the location and width,height for every contour
                x, y, w, h = cv2.boundingRect(c)
                if (w > 10 and h > 10) and w > 1*h:
        #             idx += 1
                    new_img = img[y:y+h, x:x+w]
        return cv2.imwrite(dir+name+'_' + '.png', new_img)
