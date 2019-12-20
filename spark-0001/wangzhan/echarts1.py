'''
from pyecharts import Bar
from pyecharts import Map, Geo
import os
#data=os.open('/home/hadoop/Desktop/topwce.txt',os.O_RDWR,'w+');
data=[
("France",6),
("China",33),
("india",3),
("Sweden",1),
("United Kingdom",13),
("Germany",4),
("Korea",7),
("Australia",2),
("United States",91),
("Thailand",1),
("Japan",28),
("Italy",5),
("Spain",1),
("Brazil",1)
]
attr, value = Geo.cast(data)

map0 = Map("Movie top 250", width=1500, height=750)
map0.add("world", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
map0.render(path="tw.png")


'''
from pyecharts import Bar

columns = ['肖申克的救赎', '霸王别姬', '阿甘正传', '这个杀手不太冷', '美丽人生', '泰坦尼克号', '千与千寻', '辛德勒的名单', '盗梦空间', '忠犬八公的故事', '海上钢琴师', '机器人总动员']

data1 = ['1723379', '1273976', '1330664', '1524701', '776914', '1267014', '1357107', '684518', '1298126', '879080', '1055387', '858246']
data2 = ['9.7', '9.6', '9.5', '9.4', '9.5', '9.4', '9.3', '9.5', '9.3', '9.3', '9.3', '9.3']

bar = Bar("TOP 250", "-the movie of top 250 -",width=1500, height=750)

bar.add("people", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("score", columns, data2, mark_line=["average"], mark_point=["max", "min"])
bar.render(path="zhuzhuang1.html")
'''
from pyecharts import Pie
attr =["中国香港", "印度", "中国台湾", "瑞典", "英国", "德国", "韩国", "澳大利亚", "伊朗", "美国", "日本", "中国大陆"]
v1 = [15, 3, 6, 1, 13, 4, 7, 2, 1, 91, 28, 12]
pie =Pie("Movie TOP 250",width=1500, height=750)
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render(path="pie.html")
'''