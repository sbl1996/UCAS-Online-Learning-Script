# UCAS-Online-Learning-Script
该脚本用于获取国科大实景教堂的视频的真实播放地址(视频的m3u8文件的URL)，然后可以使用自己喜欢的播放器播放URL进行观看。


## 使用说明
1. 打开课程页面，例如我打开[现代数字信号处理I](http://v.ucas.ac.cn/course/CourseIndex.do?menuCode=2&courseid=24d880f8597e4405a611391cd4b8fbdc)
2. 在课程列表中打开某一节课，例如我打开第12章第1讲[现代数字信号处理I (1)](http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0)
3. 在浏览器地址栏把网址复制下来。例如我得到的网址是http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0
4. 在命令行中使用python运行online_course.py，第一个参数为刚才复制的网址。例如我现在应该运行`python online_course.py "http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=24d880f8597e4405a611391cd4b8fbdc&classcode=1&classid=a92daa3782a44d95961d89f148b79bb2&sectionNumber=12&sectionDisplay=0"`
5. 得到视频以及PPT视频的m3u8链接，使用对应的播放器进行播放。Windows系统可使用迅雷影音，Mac系统可使用IINA，都可以调节播放速度。例如我得到的结果是`{'视频': 'http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/1ced0479-f1fc-4401-a181-0c90fa3b5653/1ced0479-f1fc-4401-a181-0c90fa3b5653.m3u8', 'PPT视频': 'http://210.76.211.10/vplus/m3u8/vplus5/vplus2505/admin/manager/68bf3f4d-d8b8-43c2-a26f-de801751e801/234d57aa-f2de-41a6-8e4b-332494b380a4/234d57aa-f2de-41a6-8e4b-332494b380a4.m3u8'}`
