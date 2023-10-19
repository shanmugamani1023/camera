import cv2
import os
from datetime import datetime

def main():
    # Create image directory
    image_dir = "images"
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
        print(f"Directory '{image_dir}' created")

    vid_obj = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    vid_obj.set(3, 1920)
    vid_obj.set(4, 1080)
    vid_obj .set(cv2.CAP_PROP_FOCUS, 100)
    vid_obj.set(cv2.CAP_PROP_AUTOFOCUS, 1)

    try:
        while True:
            ret, frame = vid_obj.read()
            if not ret:
                print("Error: Camera not available.")
                break

            now = datetime.now()
            current_data_time = now.strftime("%d_%m_%Y_%H_%M_%S")
            filename = os.path.join(image_dir, f"{current_data_time}.jpg")

            cv2.imshow("frame", frame)
            key = cv2.waitKey(1)

            if key == ord("s"):
                cv2.imwrite(filename, frame)
                print(f"{filename} image saved")
            elif key == ord("q"):
                break

    except KeyboardInterrupt:
        print("stopped by user")
        pass
    finally:
        vid_obj.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


# git add -- . ':!<C:\Users\shan\PycharmProjects\Data_collection\images>'