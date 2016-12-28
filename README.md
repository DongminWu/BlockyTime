# BlockyTime

a little side project by Flask(?) and bootstrap

idea from: [BlockyTime - anniapp](http://www.anniapp.com/blockytime/index.html)

---




##requirement

build a easy-using time tracking web application

1. We can switch the date of recording
2. Everyday was divided to \\(24*2=48\\) blocks, 30mins for each
3. Intially, every block was filled by "Sleeping time"
4. Users can choose every block, multiple choosing was supported too.
5. no drag function in first version
6. We can added category to blocky time
7. Everyday's data will be saved on server


##UI


### first version

*main page*

![](./img/2016-12-23-19-20-32.png)




---

## TODO list

1. [ ]front end part
	* [x] main page
2. [ ]back end
	* [x] data base designing
	* [ ] API designing (use REST API?)
	* [ ] programming
		* [x]set up flask server
		* [ ]data base model
		* [ ]programming REST API
		* [ ]control


##Devoloper notes:

## 12.16

- specifying the requiremnt 
- initialized git repo
- Copied a templated from bootstrap


##12.23

Goal:

finish the main UI: select time, set time

Note:

### Check box buttons

> Add data-toggle="button" to activate toggling on a single button

---

for button `<label>` should be contained in `<div>` , otherwise the check box will not perform correctly.

---

if I create a new column, this colum will be splited to 12 columns automatically.

for example, if I created a column `col-xs-6`, and I want to divide this to two parts, I should create two `col-xs-6` columns in that columns.

---

[let block fulfill the height](http://www.webhek.com/css-100-percent-height)

---

I cannot use padding or margin, so I used a placeholder `div` to make the main page shift down some distance.

Avoiding the collapse of mainpage and nav bar

##12.24

Happy X'mas Eve

Learned something about REST API

some useful links:


[Learn REST: A RESTful Tutorial](http://www.restapitutorial.com)

[Node.js RESTful API](http://www.runoob.com/nodejs/nodejs-restful-api.html)

[构建 RESTful Web 服务](http://www.ibm.com/developerworks/cn/education/java/j-rest/j-rest.html)


---

using MVC framework

Model: data base interacting

Controller

Viewer: rendering page,Javascript, connecting with others by REST API

---

funny thing

Vim for python settings:

[VIM and Python - a Match Made in Heaven](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/)

---

get function name in Python


```
import sys
def foo():
	print sys._getframe().f_code.co_name

```

---


[find css files in flask
](http://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python)


---

[jsonify a SQLAlchemy result set in Flask](http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask)

---

we should store following data:

**Primary-Category**

id|Category name | color set		| logo |
|---|------------- | -------------	|---|
0|Sport		  | red|a.png
1|study  | green|b.png

**second-Category**

id|parent_id|category name | color| logo|
|---|---|---|---|---|---|
|0|joging|origin|jog.png|


**date**

|id|date|last-changed-time|
|---|---|---|
|0|12-28-2016|01-01-2016 20:00|

**Block**

|id|date_id|show_time|position|second-category-shid|
|---|---|---|----|----|---|
0|2|12:30|12|3

##12.26

Added a datepicker:

[uxsolutions/bootstrap-datepicker](https://uxsolutions.github.io/bootstrap-datepicker/?markup=input&format=dd%2Fmm%2Fyyyy&weekStart=&startDate=&endDate=&startView=0&minViewMode=0&maxViewMode=4&todayBtn=linked&clearBtn=false&language=en&orientation=auto&multidate=&multidateSeparator=&autoclose=on&todayHighlight=on&forceParse=on#sandbox)

notes:

1. there a lot of useless files in downloaded package for my project. following is useful:
	- bootstrap-datepicker.js
	- bootstrap-datepicker.css
2. I should review the knowledge of jQuery

---

It is better not to put lots of rows in a column..

I found a margin issue, but after cutting down the number of rows from 10+ to 1. That issue has been gone.

Weird.


##12.28

Goal: create database of backend


---

I obtained some class as Singleton, such initialization and datebase model.

tutorial:

[Singleton](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html)

---

Note:

python is a scriping language, actually, the codes on the first line will be executed first.

Totally different from C...

---


Time issue

There are some type of "Time" description in SQL

- DATE
- TIME
- DATETIME

If you set a column to "DATE", you can only write date with `datetime.date(year,mon,date)`

For "DATETIME", using `datetime.datetime(year,mon,date,hour,minus, second)`

if you want to get current time, please use `time.localtime()`

you will get a structure like this:
`time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, tm_hour=18, tm_min=22, tm_sec=7, tm_wday=2, tm_yday=363, tm_isdst=0)`


Each property of that structure is read-only. 

If you want to customize a time structure, you can use `time.strptime("2016-12-28 00:00:00", "%Y-%m-%d %H:%M:%S")`

[detailed document](http://www.runoob.com/python/python-date-time.html)


---














