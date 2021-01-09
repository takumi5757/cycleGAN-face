# CycelGANのPytorch実装
CtcleGANのモデルは以下の記事を参考に作成

https://qiita.com/raglag/items/cfbe89b87335237c5ff2



# 実行方法

```
 python train.py -g 0 -m "model_name"
```

```
 python test.py -g 0 -m "model_name"
```

# その他
* identity mapping lossを用いる場合は，実行オプションで"--lambda_identity"を指定してください．

# 画像の取得と顔の切り出し

```
python collect_image.py -t インディアンス -n 100 -d ./data/indians_comedian
```

```
python crop_face.py -i ./data/indians_comedian/ -o ./data/indians_comedian/face/
```