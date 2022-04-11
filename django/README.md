能够调用baiduocr接口进行图片文字识别，可以将微信小程序下载下来的订单统计表格转换成一个个特定格式的PDF订单。

第二个功能是当时家里在做微商，顺手写了一个。

感觉首页配色奇奇怪怪。

然后部署的时候发现django的static完全不能用，部署的时候要使用nginx存储静态文件进行配合。

需要使用的话，要更改templates中模板一些静态请求设置

需要更改imagerecognition中baiduocr的key

然后要在web文件夹中的settings.py中将debug设置为True，并设置hosts

运行:

```powershell
python manage.py [面向网段的IP]:[端口]
```

