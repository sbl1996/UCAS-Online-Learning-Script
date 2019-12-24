# UCAS-Online-Learning-Script
该脚本用于获取国科大实景教堂的视频的真实播放地址(视频的m3u8文件的URL)，然后可以使用自己喜欢的播放器播放URL进行观看。


## 使用说明
1. 打开课程页面，例如我打开[现代数字信号处理I](http://v.ucas.ac.cn/course/CourseIndex.do?menuCode=2&courseid=24d880f8597e4405a611391cd4b8fbdc)
2. 在课程列表中打开某一节课，例如我打开第12章第1讲[现代数字信号处理I (1)](http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0)
3. 在浏览器地址栏把网址复制下来。例如我得到的网址是http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0
4. 在命令行中使用python运行online_course.py，第一个参数为刚才复制的网址。例如我现在应该运行`python online_course.py http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0`
5. 得到视频以及PPT视频的m3u8链接，使用对应的播放器进行播放。Windows系统可使用迅雷影音，Mac系统可使用IINA，都可以调节播放速度。例如我得到的结果是`{'视频': 'http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/1ced0479-f1fc-4401-a181-0c90fa3b5653/1ced0479-f1fc-4401-a181-0c90fa3b5653.m3u8', 'PPT视频': 'http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/234d57aa-f2de-41a6-8e4b-332494b380a4/234d57aa-f2de-41a6-8e4b-332494b380a4.m3u8'}`

## 现代数字信号处理I

### 第13章
- 第十三讲_张颢 (2): http://210.76.211.10/vplus/m3u8/vplus3/vplus2503/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/16646452-f38e-47e0-99a7-95c3387356ed/16646452-f38e-47e0-99a7-95c3387356ed.m3u8
- 第十三讲_张颢 (1): http://210.76.211.10/vplus/m3u8/vplus4/vplus2504/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/f8c67a46-0b4c-430e-bfc2-f679dd00d1bd/f8c67a46-0b4c-430e-bfc2-f679dd00d1bd.m3u8

### 第12章
- 现代数字信号处理I (2): http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/77ff2c2c-5994-4f76-be86-60ca4297c522/77ff2c2c-5994-4f76-be86-60ca4297c522.m3u8
- 现代数字信号处理I (1): http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/1ced0479-f1fc-4401-a181-0c90fa3b5653/1ced0479-f1fc-4401-a181-0c90fa3b5653.m3u8

### 第11章
- 现代数字信号处理I (2): http://210.76.211.10/vplus/m3u8/vplus4/vplus2504/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/86e5ae16-f986-4375-b7a7-c56194bf829f/86e5ae16-f986-4375-b7a7-c56194bf829f.m3u8
- 现代数字信号处理I (1): http://210.76.211.10/vplus/m3u8/vplus9/vplus2509/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/5afc521e-d3a9-40df-9f1a-344ac92b3a8f/5afc521e-d3a9-40df-9f1a-344ac92b3a8f.m3u8

### 第10章
- 现代数字信号处理I_第十讲_张颢 (2): http://210.76.211.10/vplus/m3u8/vplus8/vplus2508/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/5e457c78-4f18-4c5b-b5a7-2ee788ecb77e/5e457c78-4f18-4c5b-b5a7-2ee788ecb77e.m3u8
- 现代数字信号处理I_第十讲_张颢 (1): http://210.76.211.10/vplus/m3u8/vplus3/vplus2503/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/d8eca820-4238-4ab4-9657-05f040b33b4b/d8eca820-4238-4ab4-9657-05f040b33b4b.m3u8

### 第9章
- 现代数字信号处理I_第九讲_张颢 (2): http://210.76.211.10/vplus/m3u8/vplus2/vplus2502/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/e0a8ba18-c19b-45cd-a268-51b538991367/e0a8ba18-c19b-45cd-a268-51b538991367.m3u8
- 现代数字信号处理I_第九讲_张颢 (1): http://210.76.211.10/vplus/m3u8/vplus2/vplus2502/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/de02145c-74da-4914-9700-bf60483541d2/de02145c-74da-4914-9700-bf60483541d2.m3u8

### 第8章
- 现代数字信号处理I_第八讲_张颢 (2): http://210.76.211.10/vplus/m3u8/vplus9/vplus2509/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/dad0977f-3df1-4841-93eb-34c989c214bd/dad0977f-3df1-4841-93eb-34c989c214bd.m3u8
- 现代数字信号处理I_第八讲_张颢 (1): http://210.76.211.10/vplus/m3u8/vplus9/vplus2509/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/f13ba7f9-a600-41cd-aea8-bcbeca682c8e/f13ba7f9-a600-41cd-aea8-bcbeca682c8e.m3u8


### 第1-7章
- 建议从B站进行观看https://www.bilibili.com/video/av76003740?p=18