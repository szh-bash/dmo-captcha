# DMO-Captcha
> 验证码识别模型
> 
>作者：Immortal.S
> 
>数据源：GDMO 举报验证码

## 数据介绍
包含 "#@![0-9][A-Z]" 一共 39 类待识别字符

## 模型构成
* 训练阶段
  * 图片切分为六块 64x42 矩形制作数据集
  * 数据集在线增广
    * 空白填充 (64x64)
    * 旋转变换
    * 平移变换
    * 随机缩放 (112~116)
    * 随机裁剪 (112x112)
  * EffNet 网络，输出一维特征
  * arcface loss
  * adam 优化器
* 测试阶段
  * 导入模型至 CPU
  * 对齐测试数据
    * 填充 (64x64)
    * 放缩 (114x114)
    * 中心裁剪 (112x112)
  * 依次通过 EffNet、arcface 得到分类成绩，最大成绩类别为识别结果。

## 发布日志

### V3.0

优化 EffNet 模型精度，扩充单词图像两侧至方形，引入平移变换、旋转变换、白色填充，单字符准确率提高至 99.73%，单次答题准确率为 98.23%

优化部署代码结构

### V2.3
try-catch 解决非法文件导致识别模型崩溃 bug，同时过滤非 .jpg 文件

规定后续部署模型命名为 'AImodel.tar'

### V2.2
优化 EffNet 模型精度，调整 arcface 参数，单字符准确率提高至 99%

### V2.1
采用 EffNet，模型 20M，服务器测速 0.5s，占用不满 100%

单字符准确率为 97%

### V1.0
采用 resnet50，模型 300M，单字符准确率约为 99.99%

基础版本发布，服务器测速 5s，CPU占用 100%

###V0.0
采用 VGG16 ，模型 1.6G，准确率一般，识别速度慢
