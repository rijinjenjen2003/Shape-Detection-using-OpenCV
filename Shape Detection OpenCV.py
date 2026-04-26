import cv2
img=cv2.imread(r"C:\Users\rijin\Downloads\images.png")
cv2.imshow("orginal",img)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.Canny(blur, 50, 150)
cv2.imshow("Edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()
contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

    sides = len(approx)

    if sides == 3:
        shape = "Triangle"
    elif sides == 4:
        shape = "Rectangle"
    else:
        shape = "Circle"

    # DRAW INSIDE LOOP ✅
    cv2.drawContours(img, [cnt], -1, (0,255,0), 2)

    x, y, w, h = cv2.boundingRect(cnt)

    cv2.putText(img, shape, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()