from .vision import Vision

class InputReader:
    vision_A = Vision('Controler Images\\A.jpg')
    vision_B = Vision('Controler Images\\B.jpg')
    vision_X = Vision('Controler Images\\X.jpg')
    vision_Y = Vision('Controler Images\\Y.jpg')
    vision_Z = Vision('Controler Images\\Z.jpg')
    vision_L = Vision('Controler Images\\L.jpg')
    vision_R = Vision('Controler Images\\R.jpg')

    vision_Up = Vision('Controler Images\\Up.jpg')
    vision_Down = Vision('Controler Images\\Down.jpg')
    vision_Left = Vision('Controler Images\\Left.jpg')
    vision_Right = Vision('Controler Images\\Right.jpg')

    vision_C_Down = Vision('Controler Images\\C Down.jpg')
    vision_C_Left = Vision('Controler Images\\C Left.jpg')
    vision_C_Right = Vision('Controler Images\\C Right.jpg')
    vision_C_Up = Vision('Controler Images\\C Up.jpg')

    vision_up_arrow = Vision('Controler Images\\up arrow.jpg')
    vision_down_arrow = Vision('Controler Images\\down arrow.jpg')
    vision_left_arrow = Vision('Controler Images\\left arrow.jpg')
    vision_right_arrow = Vision('Controler Images\\right arrow.jpg')

    A_clicks = None
    B_clicks = None
    X_clicks = None
    Y_clicks = None
    Z_clicks = None
    L_clicks = None
    R_clicks = None
    Y_clicks = None
    Z_clicks = None
    L_clicks = None
    R_clicks = None
    Y_clicks = None 
    Z_clicks = None 
    L_clicks = None 
    R_clicks = None 
    Y_clicks = None
    Z_clicks = None
    L_clicks = None
    R_clicks = None

    def set_clicks(self, screenshot):
        # display the processed image
        # self.A_clicks = self.vision_A.find(screenshot, 0.98, 'rectangles')
        # self.B_clicks = self.vision_B.find(screenshot, 0.90, 'rectangles')
        # self.X_clicks = self.vision_X.find(screenshot, 0.98, 'rectangles')
        # self.Y_clicks = self.vision_Y.find(screenshot, 0.98, 'rectangles')
        # self.Z_clicks = self.vision_Z.find(screenshot, 0.95, 'rectangles')
        # self.L_clicks = self.vision_L.find(screenshot, 0.90, 'rectangles')
        # self.R_clicks = self.vision_R.find(screenshot, 0.90, 'rectangles')

        # self.Up_clicks = self.vision_Up.find(screenshot, 0.90, 'rectangles')
        # self.Down_clicks = self.vision_Down.find(screenshot, 0.90, 'rectangles')
        # self.Left_clicks = self.vision_Left.find(screenshot, 0.90, 'rectangles')
        # self.Right_clicks = self.vision_Right.find(screenshot, 0.90, 'rectangles')
        
        self.C_down_clicks = self.vision_C_Down.find(screenshot, 0.93, 'rectangles')
        self.C_left_clicks = self.vision_C_Left.find(screenshot, 0.93, 'rectangles')
        self.C_right_clicks = self.vision_C_Right.find(screenshot, 0.93, 'rectangles')
        self.C_up_clicks = self.vision_C_Up.find(screenshot, 0.93, 'rectangles')

        self.vision_C_Right.draw_rectangles_show_img(screenshot, self.C_right_clicks)

        # self.up_arrow_clicks = self.vision_up_arrow.find(screenshot, 0.98, 'rectangles')
        # self.donw_arrow_clicks = self.vision_down_arrow.find(screenshot, 0.98, 'rectangles')
        # self.left_arrow_clicks = self.vision_left_arrow.find(screenshot, 0.98, 'rectangles')
        # self.right_arrow_clicks = self.vision_right_arrow.find(screenshot, 0.98, 'rectangles')
    
    def only_one_button_clicked(self):
            return len(self.buttons_clicked()) == 1
    
    def buttons_clicked(self):
        not_clicked = []
        # if len(self.A_clicks) > 0:
        #     not_clicked.append("A")

        # if len(self.B_clicks) > 0:
        #     not_clicked.append("B")

        # if len(self.X_clicks) > 0:
        #     not_clicked.append("X")

        # if len(self.Y_clicks) > 0:
        #     not_clicked.append("Y")

        # if len(self.Z_clicks) > 0:
        #     not_clicked.append("Z")

        # if len(self.L_clicks) > 0:
        #     not_clicked.append("L")

        # if len(self.R_clicks) > 0:
        #     not_clicked.append("R")

        if len(self.C_down_clicks) > 0:
            not_clicked.append("C_Down")

        if len(self.C_right_clicks) > 0:
            not_clicked.append("C_Right")

        if len(self.C_left_clicks) > 0:
            not_clicked.append("C_Left")

        if len(self.C_up_clicks) > 0:
            not_clicked.append("C_Up")

        return not_clicked
    
    
