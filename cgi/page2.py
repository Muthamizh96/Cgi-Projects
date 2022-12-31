#!C:\Program Files\Python310\python.exe
import cgi,cgitb
import random
cgitb.enable()
flight=cgi.FieldStorage()
name1=flight.getvalue('fname')
name2=flight.getvalue('lname')
name3=(name1+" "+name2)
orgin=flight.getvalue('from')
reach=flight.getvalue('to')
cc=flight.getvalue('value1')
age1=flight.getvalue('age')
g=flight.getvalue('gender')
dd=flight.getvalue('depart')
rd=flight.getvalue('return')
if flight.getvalue('mobile') == flight.getvalue('mobile1'):
    ph=flight.getvalue('mobile')
else:
    ph="Number Mismatch"
if flight.getvalue('mail') == flight.getvalue('mail1'):
    em=flight.getvalue('mail')
else:
    em="Mail Mismatch"
flino=random.randint(12151,524568)
seano=random.randint(1,50)
gatno=random.randint(1,6)
print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title>")
print("Download")
print("</title>")
print('''<style>
        body
        {
        background-image:url(https://c4.wallpaperflare.com/wallpaper/577/1005/290/airplane-airplanes-planes-4k-wallpaper-preview.jpg);
        background-size:cover;
        background-repeat:no-repeat;
        }
        #header
        {
            text-align: center;
            font-size: 35px;
            color:#FB2576;
            background-color:#333c83c4;
            background-size: cover;
            height:90px;
            text-shadow: 10px 5px 15px red;
            border-radius: 8px;
            
        }
        ul
        {
        list-style-type:none;
        margin:0;
        padding:0;
        background-color:#5E454B;
        opacity: 0.8;
        overflow:hidden;
        border-radius: 8px;
        }
        li
        {
        float: right;
        border-left:2px solid black;
        }
       .link
        {
        display:block;
        color:rgb(217, 255, 0);
        text-align:center;
        padding:20px;
        font-size: 30px;
        text-shadow: 5px 5px 5px 5px greenyellow;
        text-decoration: none;
        }
        a:hover
        {
            background-color: darkgreen;
            text-shadow: 15px;
            color:orchid;
        }
        body
        {
        background-color:#F7A4A4;
        color:white;
        font-size:25px;
        }
        div
        {
        border;2px;
        border-color:black;
        border-radius:100px;
        border-style:none;
        width:1250px;
        height:800px;
        font-size:30px;
        background-color:#bcead5ab;
        color:#270082;
        }
        h1
        {
        text-align:center;
        color:#2D31FA;
        margin:0px;
        padding:0px;
        margin-bottom:15px;
        text-shadow:5px 5px 10px white;
        animation:header1 1s linear infinite; 
        }
        @keyframes header1
        {
        0%
        {
        opacity:0.5;
        }
        100%
        {
        opacity:1;
        }
        }
        label
        {
        display:block;
        width:700px;
        padding:5px;
        }
        #submit
        {
            font-size: 30px;
            border-radius: 15px;
            background-color: red;
            border-style: solid;
            border-color:black;
            box-shadow: 5px 5px 5px 0px white;
            font-weight:bold;
        }
        #submit:hover
        {
        background-color:#FFFAD7;
        }
        h6
        {
        text-align:left;
        margin:0px;
        margin-left:10px;
        font-size:25px;
        color:#DA0037;
        }
        .all1
        {
        display:inline-block;
        width:400px;
        }
        .all
        {
        display:inline;
        width:350px;
        }
        #age3
        {
        margin-top:30px;
        padding:150px;
        }
        #depart
        {
        margin-left:0px;
        padding:10px;
        }
        #return
        {
        margin-left:160px;
        }
        #mobile
        {
        margin-left:0px;
        padding:10px;
        }
        #email
        {
        margin-left:250px;
        }
        #fno
        {
        text-align:left;
        float:left;
        margin-left:150px;
        }
        #sno
        {
        margin-left:-200px;
        }
        #gno
        {
        margin-left:300px;
        }
         footer
        {
            text-align:left;
            display: inline-block;
            width: 100%;
        }
        .foot1
        {
            font-size: 15px;
            background-color:#F9F9C5;
            border-radius: 10px;
            height: 100px;
            display: inline-block;
            
        }
        .ft
        {
            text-align: left;
            text-decoration: none;
            padding: 10px;
            margin-right: 45px;
            margin-left:80px;
            display: inline-block;
        }
        #lifoot
        {
            border-style: none;
        }
        .hr1
        {
        border:1px solid red;
        }
        ''')
print("</style>")
print("</head>")
print("<body>")
print(''' <header id="header">Air Ticket Booking <br>Travel and Explore your Holidays</header>
    <nav id="mynav">
        <ul class="ulnavi">
            <li class="navi" id="navi1">
                <li><a href="default.asp" class="link"><b>Login</b></a></li> 
                <li><a href="sum.html" class="link"><b>Contents</b></a></li>
                <li><a href="sum.html" class="link"><b>Places</b></a></li>
                <li><a href="Flight Booking.html" class="link"> <b>Blog</b></a></li></li>
                <li><a href="About Page.html" class="link"> <b>About</b></a></li>
                <li><a href="Flight Booking.html" class="link"><b>Home</b></a></li>
            </li>
        </ul>
    </nav><br>''')
print('<center>')
print('<div>')
print('<h1 id="header1">')
print('Booking Details')
print('</h1>')
print('<h6 id="subhead">')
print('Travel Details')
print('</h6>')
print('<hr class="hr1">')
print('<br>')
print('''<label for="from" id="from"class="all1">Boarding Airport: {}</label>'''.format(orgin.capitalize()))
print('''<label for="to" id="to" class="all1">Destination Airport: {}</label>'''.format(reach.capitalize()))
print('''<label for="class" id="class" class="all1">Preferred Class: {}</label>'''.format(cc))
print('<br>')
print('<br>')
print('<h6 id="subhead">')
print('Passenger Details')
print('</h6>')
print('<hr class="hr1">')
print('''<label for="pname1" id="pname1" class="all">Passenger Name: {}</label>'''.format(name3))
print('''<label for="age3" id="age3" class="all">Age: {}</label>'''.format(age1))
print('''<label for="gend" id="gend" class="all">Gender: {}</label>'''.format(g))
print('<br>')
print('<br>')
print('''<label for="depart" id="depart" class="all">Date of Departure: {}</label>'''.format(dd))
print('''<label for="return" id="return" class="all">Date of Return: {}</label>'''.format(rd))
print('<br>')
print('<br>')
print('''<label for="Mobile" id="mobile" class="all">Mobile No: {}</label>'''.format(ph))
print('''<label for="email" id="email" class="all">Email Id: {}</label>'''.format(em))
print('<br>')
print('<br>')
print('<h6 id="subhead">')
print('Flight Details')
print('</h6>')
print('<hr class="hr1">')
print('<br>')
print('''<label for="fno" id="fno" class="all">Flight No: {}</label>'''.format(flino))
print('''<label for="sno" id="sno" class="all">Seat No: {}</label>'''.format(seano))
print('''<label for="gno" id="gno" class="all">Gate No: {}</label>'''.format(gatno))
print('<br>')
print('<br>')
print('''<form action="thankyou.html" method="post"><center><input type="submit" id="submit" value="Confirm"></center></form>''')
print('</div>')
print('<br>')
print('''<footer id="footer" class="footer11">
        <ul class="foot1">
            <li class="foot" id="lifoot">
                <a href="sum.html" class="ft">About&nbsp;Airlines</a>
                <a href="sum.html" class="ft">Forms&nbsp;and&nbsp;Downloads</a>
                <a href="sum.html" class="ft" style="margin-left:35px;">Conditions&nbsp;of&nbsp;Carriage</a>
                <a href="sum.html" class="ft" style="margin-left:10px;">Terms&nbsp;and&nbsp;Conditions</a>
                <a href="sum.html" class="ft">Media&nbsp;Center</a>
                <a href="sum.html" class="ft">Contact&nbsp;Details</a>
                <a href="sum.html" class="ft">Citizen&nbsp;Charter</a>
                <a href="sum.html" class="ft">Copyrights</a>
                <a href="sum.html" class="ft">Refund&nbsp;Policy</a>
                <a href="sum.html" class="ft"style="margin-left:120px;">News&nbsp;of&nbsp;Upcoming&nbsp;Flights.</a>
            </li>
        </ul>
    </footer></center></body></html>''')
