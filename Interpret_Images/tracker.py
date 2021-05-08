import cv2

class Tracker:
    tracker = None
    bbox = None
    selected_object = False
    success = None 
    bbox = ()

    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()

    def drawBox(self, img, bbox):
        x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255), 3, 1)
        cv2.putText(img, "Tracking", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0), 2)

    def track(self,img):
        if not self.selected_object:
            self.bbox = cv2.selectROI("Tracking",img,False)
            self.tracker.init(img, self.bbox)
            self.selected_object = True

        self.success, self.bbox = self.tracker.update(img)
        
        if self.success:
            self.drawBox(img, self.bbox)
        else:
            cv2.putText(img, "Lost", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255), 2)

    def reset_tracker(self, img, rectangle):

        for (x, y, w, h) in rectangle: 
            colour = (0,0,255)
            stroke = 20
            cv2.rectangle(img,(x,y),(x+w,y+h), colour, stroke)
            self.bbox = (x,y,w,h)
            self.tracker = cv2.TrackerCSRT_create() #overwrite old tracker

        #trace face and draw box around it
        if self.bbox:
            self.tracker.init(img, self.bbox)
            ret, self.bbox = self.tracker.update(img)
            if ret:
                p1 = (int(self.bbox[0]), int(self.bbox[1]))
                p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
                cv2.rectangle(img, p1, p2, (255, 0, 0), 2, 1)


