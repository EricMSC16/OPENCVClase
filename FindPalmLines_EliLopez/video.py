import cv2

video=cv2.VideoCapture(0)

def finding_edges(vid):
    gray = cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,40,60,apertureSize = 3)
    edges = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    edges = cv2.bitwise_not(edges)
    
    img = cv2.addWeighted(vid, 1, edges, 0.2, 0)
    return edges

while True:

    result, video_frame = video.read()
    if result is False:
        break

    edges =finding_edges(video_frame)

    cv2.imshow("My Face Detection Project", edges)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()