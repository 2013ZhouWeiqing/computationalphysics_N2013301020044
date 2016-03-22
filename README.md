*

**欢迎来到周巍青的作业**
=

----------



第一次作业
-

##Day 2016.3.2


**OK,let me have a try**
>It is my **first** time to edit the file in the github,so I am a little nervous.
It is hard for me to do something cool by using computer because of less practice.
 <i class="icon-clock">
It is 23:20 now
Going to sleep early is a good habit that can make me energetic,so I decide to stop to sleep and revert tomorrow.


----------


## Day 2016.3.8
>Thanks to my good friend Bi Ruike,I have installed **Linux** successful.It is my first time to run my computer without **windows**,making me so excited.After that,I learn something basic about **Linux** from Bi.I have known some very primate operation in **Linux**.

 >1. *Ctrl+Alt+T*——I can open the terminal interface.In terminal interface,I can do lots of things.
> 2. *sudo*——I can have root right.
 >3. *sudo apt-get install+software* ——If I want to install some software,like VIM,I just need to input **sudo apt-get install vim**.
 >4. *sudo shutdown now*-——I can input this command to turn off my computer very quickly.
  
  > I know that I still am a fish and have a long way to go.Nevertheless,I 
have fun and want to learn more about computer recently. 

----------
第二次作业
-
感谢好朋友[曹一](https://github.com/breakingDboy/computational_physics_2013301020120)对于自己程序的**耐心讲解**以及**分享的精神**，作为一个从来没有接触过任何计算机语言的小白，本次作业是在曹一同学的指导下完成的，自己对于原程序理解之后进行了一些删减，虽然功能和效果比曹一同学的原程序打了一些折扣，但是仍然满足了作业的要求。
下面我简单说下对于原[程序](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/homework2_level_1.py)的理解：

 - 这个程序的基础是[ASC码表](http://baike.baidu.com/link?url=8hO0SV49PPsV326d1cRd8bReE13rGwrBZj_yMTFOG-YQWYYd4gTxEC8jRNwnMOYZyhobq13MYqCXQXZ4KDoeU_),该表将各种字母和算符用十六进制的数进行了定义，这次作业我们只运用其中26个大写字母。
 - 这个程序要做的就是准确地取出字母对应的码表，定位后数字**1**
 输出空格，数字**0** 输出“#”，相当于用“#”充当像素点去表示出所需字母。
 - 每一个字母对应着5×7的定义数组（如大写字母A：0x7E, 0x11, 0x11, 0x11, 0x7E），故用两个**for**循环语句，取遍这个35个数字，遇到数字**1** 输出空格，数字**0** 输出“#”。取点需要进行移位，移位用一个和“0000 0001”的**与运算**实现（如1010 1101和0000 0001进行**与运算**就只取出了最后一位数字，然后依次取遍所有数字。）
 - “**raw_input**”是一个定义的输入函数，方便用户和系统进行交互。

>本次作业把程序从简单一直到复杂，拆分依次实现了3个level。具体作业程序如下：

 >1.[  level_1](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/homework2_level_1.py)
 >2.[   level_2](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/homework2_level_2.py)
>3.[  level_3](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/homework2_level_3.py)
 
----------
第三次作业
-
因为觉得自己对于计算机语言太过陌生，老师又鼓励我们多解决问题，把计算机用起来，所以这次作业我将Chapter1后面的六道题目都进行了练习，其中将第一，二题将进行了画图练习。
作业的程序如下：

 

> 1. [第一题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.1.py)
 >2. [第二题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.2.py)
 >3. [第三题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.3.py)
 >4. [第四题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.4.py)
 >5. [第五题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.5.py)
 >6. [第六题](https://github.com/2013ZhouWeiqing/computationalphysics_N2013301020044/blob/master/computational_physics/1.6.py)

对于所用程序的思路进行一下解释:

 - 首先创建一个空的list
 - 然后不断地将运算结果append打入list
 - 用 for 语句进行循环运算
 - 最后运用 list 中定位的功能print结果
 
因为不了解 list和循环语句,所以做作业之前进行了一些针对性的学习,在此分享一些总结的笔记:
一，list 和 tuple 是python内置的有序集合，区别在于 list 内元素可变，但是 tuple 内元素不可变。
关于元素的定位，定义一个 list
For example：
c=['zhouweiqing']
定位 c[1] or c[-1]
c.append('hahhhhaah')#加入到 list 的最后一位
c.insert(1,love)#插入
c.pop()# 删除最后一个元素
tuple 与 list 类似
二，条件判断和循环
条件判断： if，else，elif（else if）
if 语句是从上往下判断的，如果某个判断是 True 则会执行对应语句，忽略其他
循环 有两种
第一种 for...in 循环，依次把 list 或 tuple 中的元素进行操作。
For example:求0-100的求和
sum = 0
for i in range(101)
    sum = sum + i
print sum
第二种 while 循环，只要条件满足则不断循环，直至条件不满足，例子(计算100内奇数之和)：
sum = 0
n = 99
while n >0
    sum = sum + n
    n = n - 2
print sum
 
本次作业尝试运用 raw_input  增强程序的交互性,学习到:
raw_input()括号内的输入永远是字符串，如果想用数字进行操作，必须进行 int操作.

 因为图片上传出了点问题,持续更新中.



