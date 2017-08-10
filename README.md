# weibo_spider
使用python自动爬取指定微博用户的微博和图片，并对微博进行归类分析。

一、数据准备。
得到uid和cookie具体方法参考我的简书。
http://www.jianshu.com/p/e6bca8407204
将得到的数据填入到weibo.py中。

二、数据爬取。
笔者terminal运行。环境python2.7 / macOS 10.12.3
运行weibo.py
将指定账户的微博的文字和图片爬取，并存储。

三、数据分析。
运行analysis.py
填入uid，对已爬取的数据进行简易分析
暂时分析的内容有微博分类、高频表情、高频词、高频人名
后续有空完善图片的人脸识别。
