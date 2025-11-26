import cv2 as cv

def flip_vertical(img):
    return cv.flip(img, 0)

def flip_horizontal(img):
    return cv.flip(img, 1)

def rotate_90(img):
    return cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

def rotate_180(img):
    return cv.rotate(img, cv.ROTATE_180)

def display_transformations(filename):
    img = cv.imread(filename)
    
    if img is None:
        print(f'Could not read the image: {filename}')
        return False
    
    img_flipped_v = flip_vertical(img)
    img_flipped_h = flip_horizontal(img)
    img_rotated_90 = rotate_90(img)
    img_rotated_180 = rotate_180(img)
    
    images = [
        (img, 'Original'),
        (img_flipped_v, 'Flipped Vertical'),
        (img_flipped_h, 'Flipped Horizontal'),
        (img_rotated_90, 'Rotated 90 degrees'),
        (img_rotated_180, 'Rotated 180 degrees')
    ]
    
    for img_display, title in images:
        cv.imshow(title, img_display)
        
        while True:
            key = cv.waitKey(33) & 0xFF
            if key == 27:  # ESC
                break
        
        cv.destroyWindow(title)
    
    cv.destroyAllWindows()
    return True

def main():
    filename = input('Enter image filename: ').strip()
    display_transformations(filename)

if __name__ == '__main__':
    main()

