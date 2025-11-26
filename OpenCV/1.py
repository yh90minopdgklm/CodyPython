import cv2 as cv
import datetime
import sys

def generate_filename(extension):
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d_%H-%M-%S') + extension
    return filename

def display_image(filename):
    img = cv.imread(filename)
    
    if img is None:
        print(f'Could not read the image: {filename}')
        return False
    
    cv.imshow('Display window', img)
    
    while True:
        key = cv.waitKey(33) & 0xFF
        if key == 27:  # ESC
            break
    
    cv.destroyAllWindows()
    return True

def play_video(filename):
    cap = cv.VideoCapture(filename)
    
    if not cap.isOpened():
        print(f'Could not open the video file: {filename}')
        return False
    
    is_recording = False
    video_writer = None
    recording_filename = None
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            print('Cannot receive frame (stream end?). Exiting ...')
            break
        
        if is_recording and video_writer is not None:
            video_writer.write(frame)
        
        cv.imshow('frame', frame)
        
        key = cv.waitKey(33) & 0xFF
        
        if key == 27:  # ESC
            break
        elif key == 122:  # z
            capture_filename = generate_filename('.png')
            cv.imwrite(capture_filename, frame)
            print(f'Image captured: {capture_filename}')
        elif key == 120:  # x
            if not is_recording:
                recording_filename = generate_filename('.mp4')
                fourcc = cv.VideoWriter_fourcc(*'mp4v')
                fps = int(cap.get(cv.CAP_PROP_FPS))
                width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
                video_writer = cv.VideoWriter(recording_filename, fourcc, fps, (width, height))
                is_recording = True
                print(f'Recording started: {recording_filename}')
        elif key == 99:  # c
            if is_recording:
                if video_writer is not None:
                    video_writer.release()
                    video_writer = None
                is_recording = False
                print(f'Recording stopped: {recording_filename}')
    
    if is_recording and video_writer is not None:
        video_writer.release()
    
    cap.release()
    cv.destroyAllWindows()
    return True

def main():
    print('OpenCV Image/Video Player')
    print('1. Display Image')
    print('2. Play Video')
    
    choice = input('Select option (1 or 2): ').strip()
    
    if choice == '1':
        filename = input('Enter image filename: ').strip()
        display_image(filename)
    elif choice == '2':
        filename = input('Enter video filename: ').strip()
        play_video(filename)
    else:
        print('Invalid choice. Exiting.')
        sys.exit(1)

if __name__ == '__main__':
    main()

