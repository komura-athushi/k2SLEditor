import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import glob
import constant

class MyImage():
    def __init__(self):
        self.item_id = -1
        self.image_position = None
        self.image_size = None
        self.tkimg = None
        self.file_name = None
        self.name = None
        self.scale= [1.0,1.0]
        self.position = [constant.CANVAS_WIDTH/2 * constant.CANVAS_SMALLER + constant.ADD_CANVAS_SIZE,
        constant.CANVAS_HEIGHT/2 * constant.CANVAS_SMALLER + constant.ADD_CANVAS_SIZE]

        self.img = None
        self.tkimg = None
        self.width=None
        self.height=None
        self.tag = None

        self.false_width = None
        self.false_height = None

        self.number_layer = 10
    
    #自身の情報を相手にコピーする
    #oppがコピー元
    def copy_image_infromation(self,canvas,opp):
        self.name = opp.name
        position=opp.get_position()
        self.set_position(canvas,position[0],position[1])
        self.scale=opp.scale
        self.number_layer = opp.number_layer

    #画像の座標を取得
    #戻り値はキャンバス内の座標
    def get_position(self):
        return self.position
    
    #画像を特定の座標に移動させる
    #引数はキャンバス内の座標
    def set_position(self,canvas,position_x,position_y):
        canvas.coords(self.item_id,position_x,position_y)
        self.position=[position_x,position_y]

    #画像を移動量分動かす
    #移動量はキャンバス上での移動量
    def move_position(self,canvas,delta_x,delta_y):
        self.position = [self.position[0]+delta_x,self.position[1]+delta_y]
        canvas.coords(self.item_id,
        self.position[0],
        self.position[1]
        )

    #座標を設定するだけ
    def set_position_no_move(self,position_x,position_y):
        self.position=[position_x,position_y]

    #画像を上に持ってくる
    def raise_image(self,canvas):
        canvas.tag_raise(self.item_id)

    #画像をリサイズする
    def resize(self):
        
        self.false_width = int(self.image_size[0]*self.scale[0])
        self.false_height = int(self.image_size[1]*self.scale[1])
        self.width=int(self.false_width*constant.CANVAS_SMALLER)
        self.height=int(self.false_height*constant.CANVAS_SMALLER)
        self.img = self.img.resize((self.width,self.height))
        #このImageTk?は保持しておかないといけないらしい
        self.tkimg = ImageTk.PhotoImage(self.img)
        
    def set_scale(self,scale):
        if scale[0] < constant.MYIMAGE_MiN_SIZE or scale[1] < constant.MYIMAGE_MiN_SIZE:
            return
        self.scale=scale

    #画像のを取得する
    def get_width(self):
        return self.width

    #画像の高さを取得する
    def get_height(self):
        return self.height

    #画像を読み込む
    def load_image(self,canvas,file,tag='img'):
        self.file_name = file
        #画像読み込み
        self.img = Image.open(file)
        
        #画像のサイズを取得
        self.image_size = self.img.size
        

        #名前が既に付いていたら処理しない
        if self.name==None:
    
            #ファイルの名前を抽出していく、/と.を除いていく
            slash_number = file.rfind('/')
            number = file.rfind('.')
            extension = None
            if slash_number == -1:
                extension = file
                self.name = file[:number]
            else:
                extension = file[slash_number + 1:]
                self.name = file[slash_number + 1:number]

            if self.name != 'rect':
                pass
                #print(self.file_name)
                #file_path = glob.glob('Assets/sprite/')
                #a =file_path[0]+extension
                #self.img.save(a)
                #self.file_name = a
                #print(a)

        self.resize()

        
        self.item_id = canvas.create_image(self.position[0],
        self.position[1],
        image=self.tkimg,
        tags=tag)
        self.tag = tag
        
        
        


    