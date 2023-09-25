'''
from tensorflow.keras.utils import img_to_array,load_img
def recongnition(pic):
    model=''#モデルの読み込み
    img = img_to_array(load_img(pic, target_size=(224,224)))
  #0-1に変換
    img_nad = img_to_array(img)/255
        #4次元配列に
    img_nad = img_nad[None, ...]


        #表示したいクラス名（任意設定）
    label=[i for i in range(1,152)]
        #判別
    pred = model.predict(img_nad, batch_size=1, verbose=0)

        #判別結果の配列から最も高いところを抜きだし、そのクラス名をpred_labelへ
    pred_label = label[np.argmax(pred[0])]
    return pred_label

'''


