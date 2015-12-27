#! /usr/bin/env python
# -*- coding: utf-8 -*-

html_data_head = '''<!DOCTYPE html>\
<html lang="en"> \
<head>
    <meta charset="UTF-8">
    <title>C语言</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
        <script type="text/javascript">
            $(document).ready(function(){
                $(".input").click(function(){
                //跳转至选择页的地方
                self.location="../html/" + $("select").val() + ".html";
                })
            ;})
        </script>
	</head>
	<body>
	<object id="forfun" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width=100% height=90%
    		codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0">
    		<param name="movie" id="movie" value="../videos/%s.swf">
    		<embed id="forfunex" src="../videos/%s.swf"
        	width=100%
        	height=90%
        	align="middle"
        	quality="high"
        	bgcolor="#f0fff8"
        	menu="false">
    		</embed>
	</object><br><br>
        <label>选择课程：</label>
        <select id="select" >
            <optgroup id="ops-1" label="第一章">
                <option id="1-01" name="1-01">1-01</option>
                <option id="1-02" name="1-02">1-02</option>
                <option id="1-03" name="1-03">1-03</option>
                <option id="1-04" name="1-04">1-04</option>
                <option id="1-05" name="1-05">1-05</option>
                <option id="1-06" name="1-06">1-06</option>
                <option id="1-07" name="1-07">1-07</option>
                <option id="1-08" name="1-08">1-08</option>
                <option id="1-09" name="1-09">1-09</option>
                <option id="1-10" name="1-10">1-10</option>
                <option id="1-11" name="1-11">1-11</option>
                <option id="1-12" name="1-12">1-12</option>
                <option id="1-13" name="1-13">1-13</option>
                <option id="1-14" name="1-14">1-14</option>
                <option id="1-15" name="1-15">1-15</option>
                <option id="1-16" name="1-16">1-16</option>
            </optgroup>
            <optgroup id="ops-2" label="第二章">
                <option id="2-01" name="2-01">2-01</option>
                <option id="2-02" name="2-02">2-02</option>
                <option id="2-03" name="2-03">2-03</option>
                <option id="2-04" name="2-04">2-04</option>
                <option id="2-05" name="2-05">2-05</option>
                <option id="2-06" name="2-06">2-06</option>
                <option id="2-07" name="2-07">2-07</option>
                <option id="2-08" name="2-08">2-08</option>
                <option id="2-09" name="2-09">2-09</option>
                <option id="2-10" name="2-10">2-10</option>
                <option id="2-11" name="2-11">2-11</option>
                <option id="2-12" name="2-12">2-12</option>
                <option id="2-13" name="2-13">2-13</option>
                <option id="2-14" name="2-14">2-14</option>
                <option id="2-15" name="2-15">2-15</option>
                <option id="2-16" name="2-16">2-16</option>
                <option id="2-17" name="2-17">2-17</option>
            </optgroup>
            <optgroup id="ops-3" label="第三章">
                <option id="3-01" name="3-01">3-01</option>
                <option id="3-02" name="3-02">3-02</option>
                <option id="3-03" name="3-03">3-03</option>
                <option id="3-04" name="3-04">3-04</option>
                <option id="3-05" name="3-05">3-05</option>
                <option id="3-06" name="3-06">3-06</option>
                <option id="3-07" name="3-07">3-07</option>
                <option id="3-08" name="3-08">3-08</option>
                <option id="3-09" name="3-09">3-09</option>
                <option id="3-10" name="3-10">3-10</option>
                <option id="3-11" name="3-11">3-11</option>
                <option id="3-12" name="3-12">3-12</option>
                <option id="3-13" name="3-13">3-13</option>
                <option id="3-14" name="3-14">3-14</option>
                <option id="3-15" name="3-15">3-15</option>
                <option id="3-16" name="3-16">3-16</option>
                <option id="3-17" name="3-17">3-17</option>
                <option id="3-18" name="3-18">3-18</option>
                <option id="3-19" name="3-19">3-19</option>
                <option id="3-20" name="3-20">3-20</option>
                <option id="3-21" name="3-21">3-21</option>
                <option id="3-22" name="3-22">3-22</option>
            </optgroup>
            <optgroup id="ops-4" label="第四章">
                <option id="4-01" name="4-01">4-01</option>
                <option id="4-02" name="4-02">4-02</option>
                <option id="4-03" name="4-03">4-03</option>
                <option id="4-04" name="4-04">4-04</option>
                <option id="4-05" name="4-05">4-05</option>
                <option id="4-06" name="4-06">4-06</option>
                <option id="4-07" name="4-07">4-07</option>
                <option id="4-08" name="4-08">4-08</option>
                <option id="4-09" name="4-09">4-09</option>
                <option id="4-10" name="4-10">4-10</option>
                <option id="4-11" name="4-11">4-11</option>
                <option id="4-12" name="4-12">4-12</option>
            </optgroup>
            <optgroup id="ops-5" label="第五章">
                <option id="5-01" name="5-01">5-01</option>
                <option id="5-02" name="5-02">5-02</option>
                <option id="5-03" name="5-03">5-03</option>
                <option id="5-04" name="5-04">5-04</option>
                <option id="5-05" name="5-05">5-05</option>
                <option id="5-06" name="5-06">5-06</option>
                <option id="5-07" name="5-07">5-07</option>
                <option id="5-08" name="5-08">5-08</option>
                <option id="5-09" name="5-09">5-09</option>
                <option id="5-10" name="5-10">5-10</option>
                <option id="5-11" name="5-11">5-11</option>
            </optgroup>
            <optgroup id="ops-6" label="第六章">
                <option id="6-01" name="6-01">6-01</option>
                <option id="6-02" name="6-02">6-02</option>
                <option id="6-03" name="6-03">6-03</option>
                <option id="6-04" name="6-04">6-04</option>
                <option id="6-05" name="6-05">6-05</option>
                <option id="6-06" name="6-06">6-06</option>
                <option id="6-07" name="6-07">6-07</option>
            </optgroup>
        </select>
    	<input id="input" class="input" type="button" value="播  放" />
	</body>
</html>'''

add_data = ' selected="selected"'
import os

os.system("color a")
# 生成的文件存放的目录
filePath = os.getcwd()


def fileWrite(num1, num2):
    if num2 < 10:
        num = str(num1) + '-0' + str(num2)
    else:
        num = str(num1) + '-' + str(num2)
    find_num = '>' + num + '<'
    curr = html_data_head2.find(find_num)
    html_data_head2_ed = html_data_head2[:curr] + add_data + html_data_head2[curr:]
    fileName = filePath + '\\' + num + ".html"
    with open(fileName, 'a') as f:
        f.write(html_data_head + num + html_data_head1 + num + html_data_head2_ed)


def Loop(oneNum, maxNum):
    for n in range(1, maxNum + 1):
        fileWrite(oneNum, n)


# 第一章
Loop(1, 16)
print u"第一章所有网页已生成！"
# 第二章
Loop(2, 17)
print u"第二章所有网页已生成！"
# 第三章
Loop(3, 22)
print u"第三章所有网页已生成！"
# 第四章
Loop(4, 12)
print u"第四章所有网页已生成！"
# 第五章
Loop(5, 11)
print u"第五章所有网页已生成！"
# 第六章
Loop(6, 7)
print u"第六章所有网页已生成！"
