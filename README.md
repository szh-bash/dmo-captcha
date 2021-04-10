# IShield
> 任务：验证码识别
>
> 数据源：GDMO 举报验证码
> 
> 作者：Immortal.S

## 数据介绍
包含 "#@![0-9][A-Z]" 一共 39 类待识别字符

## 模型构成
* 训练阶段
  * 图片切分为六块 64x42 矩形制作数据集
  * 数据集在线增广
    * 空白填充 (64x64)
    * 旋转变换
    * 平移变换
  * EffNet 网络，输出一维特征
  * arcface loss (s=32, m=0.3)
  * adam 优化器
* 测试阶段
  * 导入模型至 CPU
  * 对齐测试数据
    * 填充 (64x64)
  * 依次通过 EffNet、arcface 得到分类成绩，最大成绩类别为识别结果。

## 发布日志

### V3.2 --- Final Version
Modify：取消 resize，固定输入为 64x64，arcface margin 扩大至 0.3

Acc：用先前两个模型清洗数据集，去除重复数据。最终训练集、测试集准确率均为 100%

Speed：0.2~0.3s (Sever) | <0.1s (Local)

Cpu: 25% (Sever)

Model: 8M

Test：3000+ 次连续举报全部成功拦截。

### V3.1
Modify：随机变化 (112~128)，延长训练

Acc：单字符准确率 99.85%，单次答题准确率 99.12%

others: 监控记录中加入答题编号、时间信息，优化排版

### V3.0

Modify: 填充单词图像为 64x64，引入平移变换、旋转变换、白色填充

Acc: 单字符准确率提高至 99.73%，单次答题准确率为 98.39%

others: 优化部署代码结构

### V2.3
Bug-Fixed: try-catch 解决非法文件导致识别模型崩溃 bug，同时过滤非 .jpg 文件

others: 规定后续部署模型命名为 'AImodel.tar'

### V2.2
Modify: 调整 arcface 参数

Acc: 单字符准确率提高至 99%

### V2.1
Backbone: EffNet

Acc: 单字符准确率为 97%

Model: 20M

Speed: 0.5s (sever)

CPU: <100% (Sever)

### V1.0
Backbone: resnet50

Acc: 单字符准确率 99.99%

Model: 300M

Speed: 5s (sever)

CPU: 100% (sever)

others: 基础版本发布

### V0.0
采用 VGG16 ，模型 1.6G，准确率一般，识别速度慢
