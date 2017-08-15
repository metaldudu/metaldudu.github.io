---
layout: post
title: "JS练习：口算题生成器"
description: ""
category: geek
tags: [git]
---

小学一年级打好口算基础很重要，通常学校会发一本口算卡，每天做一页。去年女儿上一年级，我尝试用python写了一段程序，输出加法和减法的口算题。我用的方法很笨，用print语句输出，然后粘贴到word里打印。

前几天想到改进一下这个小程序，搜索了一下发现有好几个windows下的应用程序，还有Excel写的，原来广大家长的需求还是很明显的。我想能改用web应用，用JS要比python更合适，于是经过一些学习（拼凑），完成了这个小工具，算是我第一个前端学习成果。地址在：[http://mrdu.me/ks](http://mrdu.me/ks)。

因为是单文件的html文件，所以可以保存这个网页到本机，然后打印就可以了。后续，会跟着孩子的学习进度进行更新，加入更多功能。

以下是代码：

````
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>口算题生成器</title>
<style type="text/css">
body {
    font-family: Verdana, Arial, Helvetica, sans-serif;
    font-size: 15px;
    color:#333
    background: #333;
}

p {
    padding: 10px;
}
hr { height:2px;border:none;border-top:1px solid  #333;}

#wrapper {
    margin: 0 auto;
    width: 85%;
}

#content {
    float: left;
    background: #fff;
    width: 100%;}

.three-col {
       -moz-column-count: 3;
       -moz-column-gap: 20px;
       -webkit-column-count: 3;
       -webkit-column-gap: 20px;
      column-count:3;
      column-gap: 20px;
}
.bluebut {
  position: relative;
  vertical-align: top;
  width: 160px;
  height: 50px;
  padding: 0;
  font-size: 22px;
  color: white;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  background: #1abc9c;
  border: 0;
  border-bottom: 2px solid #12ab8d;
  cursor: pointer;
  -webkit-box-shadow: inset 0 -2px #12ab8d;
  box-shadow: inset 0 -2px #12ab8d;
}
.bluebut:active {
  top: 1px;
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}

#head {
  font-size: 22px;
}
#printnotes {
padding:0px;
margin:0px;
}
#qr {
display: inline;
float:left;
}
#keys {
padding-left:78px;
}

input {
  font-size: 22px;
  width:50px;
}
.radioclass {
  width:50px;
}

@media print {
body {background-color:#FFFFFF;  font-size: 14px;line-height:26px;}
h1 {font-size:15px;}
#head, #notes {display:none;}
#printnotes {font-size:10px; font-color:#777;}
}
@page {margin: 0.5cm;}
</style>

<script>
//获取题目数量函数
function fmaxti(){
  var temp=document.getElementsByName("maxti");
  for (i=0;i<temp.length;i++){
  //遍历Radio
    if(temp[i].checked)
      {
      maxti=temp[i].value;
      }
  }
}

//检测输入数字为整数
function checknum(ss){
  var ss;
  return typeof ss === 'number' && ss%1 === 0
}

//加法
function add(){
  var max,min,i,x,y;
  max=Number(document.getElementById("max").value);
  min=Number(document.getElementById("min").value);
  x='';y='';
  fmaxti();
  i=1;

if (!(Number.isInteger(max) && Number.isInteger(min) ))
  {alert("输入有误！");return;}

if (min>49)
  {alert("最小数字应小于50");return;}

do
  {
  n1=parseInt((max-min)*Math.random()+min);
  n2=parseInt((max-min)*Math.random()+min);

  if ((n1+n2)<100)
    {
    y=y+(n1+n2)+' ';
    if (n1<10){n1='&ensp;'+n1;}
    if (n2<10){n2='&ensp;'+n2;}
    x= x + n1 + ' + ' + n2 + ' = ' +'______<br/>';
    i++;
    }
  }
while (i<maxti);
document.getElementById("answer").innerHTML= x;
document.getElementById("keys").innerHTML= y;
}

//随机减法函数
function subtract(){
var max,min,i,x;
max=Number(document.getElementById("max").value);
min=Number(document.getElementById("min").value);
  x='';
  fmaxti();

if (!(Number.isInteger(max) && Number.isInteger(min) ))
  {alert("输入有误！");return;}

for (var i=1; i<maxti; i++)
  {
  n1=parseInt((max-min)*Math.random()+min);
  n2=parseInt((max-min)*Math.random()+min);

  if (n1<n2)
    {n1=n1+n2;n2=n1-n2;n1=n1-n2;}
  if (n1<10)
    {n1='&ensp;'+n1;}
  if (n2<10)
    {n2='&ensp;'+n2;}
  x= x + n1 + ' - ' + n2 + ' = ' +'______<br/>';
  }
document.getElementById("answer").innerHTML= x;
}

//三个数加法
function threeadd(){
var max,min,i,x;
max=Number(document.getElementById("max").value);
min=Number(document.getElementById("min").value);
x='';
fmaxti();
i=1;

if (!(Number.isInteger(max) && Number.isInteger(min) ))
  {alert("输入有误！");return;}

if (min>32)
  {alert("最小数字应小于33");return;}

do
  {
  n1=parseInt((max-min)*Math.random()+min);
  n2=parseInt((max-min)*Math.random()+min);
  n3=parseInt((max-min)*Math.random()+min);

  if ((n1+n2+n3)<100)
    {
     if (n1<10){n1='&ensp;'+n1;}
     if (n2<10){n2='&ensp;'+n2;}
     if (n3<10){n3='&ensp;'+n3;}
     x= x + n1 + ' + ' + n2 + ' + ' + n3 + ' = ______<br/>';
     i++;
    }
  }
while (i<maxti);
document.getElementById("answer").innerHTML= x;
}

//三个数减法
function threesubtract(){
var max,min,i,x;
max=Number(document.getElementById("max").value);
min=Number(document.getElementById("min").value);
x='';
fmaxti();
i=1;

if (!(Number.isInteger(max) && Number.isInteger(min) ))
  {alert("输入有误！");return;}

//避免max接近min的2倍，随机结果无法出现
if ((max-2*min)<5)
  {alert("最大和最小数字范围太小");return;}

do
  {
  n1=parseInt((max-min)*Math.random()+min);
  n2=parseInt((max-min)*Math.random()+min);
  n3=parseInt((max-min)*Math.random()+min);

  if ((n1-n2-n3)>0)
    {
     if (n1<10){n1='&ensp;'+n1;}
     if (n2<10){n2='&ensp;'+n2;}
     if (n3<10){n3='&ensp;'+n3;}
     x= x + n1 + ' - ' + n2 + ' - ' + n3 + ' = ______<br/>';
     i++;
    }
  }
while (i<maxti);
document.getElementById("answer").innerHTML= x;
}


//三个数加减混合
function three(){
var max,min,i,x;
max=Number(document.getElementById("max").value);
min=Number(document.getElementById("min").value);
x='';
fmaxti();
i=1;

if (!(Number.isInteger(max) && Number.isInteger(min) ))
  {alert("输入有误！");return;}

do
  {
  n1=parseInt((max-min)*Math.random()+min);
  n2=parseInt((max-min)*Math.random()+min);
  n3=parseInt((max-min)*Math.random()+min);

  if ((n1+n2)<100 && (n1+n2-n3)>0)
    {
     if (n1<10){n1='&ensp;'+n1;}
     if (n2<10){n2='&ensp;'+n2;}
     if (n3<10){n3='&ensp;'+n3;}
     x= x + n1 + ' + ' + n2 + ' - ' + n3 + ' = ______<br/>';
     i++;
    }
  else if ((n1-n2)>0 && (n1-n2+n3)<100)
    {
     if (n1<10){n1='&ensp;'+n1;}
     if (n2<10){n2='&ensp;'+n2;}
     if (n3<10){n3='&ensp;'+n3;}
     x= x + n1 + ' - ' + n2 + ' + ' + n3 + ' = ______<br/>';
     i++;    
    }
  }
while (i<maxti);
document.getElementById("answer").innerHTML= x;
}


//打印
function printit()
  {
  window.print()
  }

</script>
</head>
<body>
    <div id="wrapper">
        <div id="content">
<h1>口算题</h1>
<div id="head">
<br/>
最小数字：<input id="min" value='0'> 最大数字：<input id="max" value='100'> 试题数量：<input type="radio" name="maxti" value="26" class="radioclass">25 <input type="radio" name="maxti" value="51"  class="radioclass">50 <input type="radio" name="maxti" value="101" class="radioclass" checked>100

<br/><br/>
<button onclick="add()" class="bluebut" >加法</button> <button onclick="subtract()" class="bluebut">减法</button> <button onclick="threeadd()" class="bluebut">三个数加法</button> <button onclick="threesubtract()" class="bluebut">三个数减法</button> <button onclick="three()" class="bluebut">三个数加减混合</button><button  style="float:right"  onclick="printit()" class="bluebut">打印</button>

</div>
<hr>
<div class="three-col">
<output id="answer"></output>
</div>
<hr>
<div id="notes">网址：<a href="http://mrdu.me/ks">mrdu.me/ks</a><br/>说明：确定出题范围和数量，结果小于100。推荐使用Chrome浏览器。适用A4纸打印，答案可以撕开。<br/>感谢：<a href="http://goqr.me/#t=url">goQR.me</a> / <a href="http://cssdeck.com/labs/beautiful-flat-buttons">Beautiful Flat Buttons</a></div>

<div id="printnotes">
  <div id="qr"><img src="qrcode.png" width="75px" height="75px" /></div>
  <div id="keys"></div>
</div>

       </div>
    </div>
</body>
</html>

````


`20160927`
