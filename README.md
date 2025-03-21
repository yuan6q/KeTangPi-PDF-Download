# KeTangPi-PDF-Download

课堂派pdf下载

下载被设置为不可下载的课堂派PDF文档

## 第一步，在课堂派上打开对应的pdf文件，通过F12打开网页源代码，利用ctrl+F搜索到含frame的地方（注意需要是下面截图那个“#document”）

![image](https://github.com/user-attachments/assets/60a154e7-7e32-4052-8ef4-c07c199c3a73)

将链接复制到浏览器打开此时便可以得到原html文件

## 第二步，ctrl+S保存html文件，注意保存前一定要下拉到底，使得所有的图片加载完成

## 第三步，使用仓库中的python脚本，生成pdf文件

（输入的路径为上一步保存后产生的文件夹的位置）

脚本需要依赖img2pdf

可以使用下面的命令来安装依赖

```powershell
pip install img2pdf
```

参考了：https://zhuanlan.zhihu.com/p/422911451
