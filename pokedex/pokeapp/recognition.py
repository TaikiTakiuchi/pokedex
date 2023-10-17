#画像を入力してそれが何の画像か判定する
import numpy as np
from tensorflow import keras
import cv2
from pokedex.settings import BASE_DIR
import os
#画像の読込
def recognition_poke(img_path):
    BASE=str(BASE_DIR).replace(os.sep,'/')
    target_path=BASE+img_path
    #print(BASE_DIR)
    print(target_path)
    print(type(target_path))


    img_array = cv2.imread(target_path) 
    print(img_array) # 画像読み込み
    img_resize_array = cv2.resize(img_array, (100, 100))
    img_resize_array = np.array(img_resize_array, dtype=np.float)
    img_resize_array/=255
    x=np.array(img_resize_array)
    pic=x.reshape([1,100,100,3])#1つの画像を選び、reshapeする。頭に1をつけないとエラーになる。
    #モデルの準備
    model=keras.models.load_model(BASE+'/cnn_pokemon_fine.h5')
    label=[i for i in range(1,151)]#表示したいクラス名（任意設定）


    #モデルの準備
    label=[i for i in range(1,151)]#表示したいクラス名（任意設定）
    #予測
    pred = model.predict(pic, batch_size=64,verbose=0)
    score = np.max(pred)#判別結果で最も高い数値を抜き出し
    pred_label = label[np.argmax(pred[0])]#判別結果の配列から最も高いところを抜きだし、そのクラス名をpred_labelへ

    return [pred_label,score]


