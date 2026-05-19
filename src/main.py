import argparse

import cv2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="host on which camera is based", default="192.168.0.1")
    parser.add_argument("--port", help="port on which camera is based", default="8080")
    

    args = parser.parse_args()
    stream_url = "http://" + args.host + ":" + args.port + "/video"
    # stream_url = "http://192.168.0.180:8080/video"
    cap = cv2.VideoCapture(stream_url)

    detector = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()    
        if not ret:
            break

        mask = detector.apply(frame)
        # cv2.findContours(mask, cv2.RETR_TREE)

        cv2.imshow("Frame", mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

print("Activating Script")
main()