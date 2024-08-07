# Flask - CMS

<p>This is the full custom demo for developer provide use Flask, You can run this Flask App with some configure with you system.<br>
Very Thanks For kind of the opensource module. To support any posiblae function with Javascript and Python.<br>
Note to all the dear developers, kind of the modules are not support of with you are run with 32bit or 64bit python version.<br>
In this template, We have update and alert user to know, we have use `async def` and normal `def` for function.<br>
With the new update with numpy>=2.0, you may have a bug error, recommand keep the numpy version before 2.0<br>
For AI Developers, if need `pandas` `pytorch` `tensorflow`, keep follow the requestion pip you need to update(s).<br>
This is the following module we ued in this DEMO project.</p>

* Flask
* Flask Longin
* Werkzeug Secuirty
* sqlite utils
* Tiny MCE v5 Editor
* flask_ckeditor
* QR Code
* Token Builder
* GPG Encrypt & Decrypt data(s)
* Supoort File(s) Upload

<p>
We have add the CK-Editor into the demo.<br>
That meant it support all the JavaScript plugin for make your work in text/coding.<br>
We have stop the CK-Editor Upload path but we tag the example code from flask-ckeditor modules.<br>
I stop the secuitry test on here.<br>
<br>
Update the bootstrap version and and one more open function dashboard<br>
We have same make the template empty page for the dashboard with file `plugins/dashboard/main.htm` in templates folder.<br>
Now you can create and setup your free code free API, easy convert and display with web html.<br>
Free for Open!!!</p>

![image](https://user-images.githubusercontent.com/1324252/217410498-87566f7c-4194-48b1-ae58-e1c332a90212.png)

### !!!NEW!!! Dashboard & Nav For FREE!

![image](https://github.com/constantinedev/Flask-CMS/assets/1324252/51ad0f56-07df-4959-903f-6cb096c95df6)

<p>For the basic This Demo will show you the basic secuirty login and, How to update the data with SQLite Database.<br>
What does it means? If you need the custom order, content this project developer for make a user require.<br>
We free out the SQLAlchemy to use the sqlite_utils to connect with the DB.<br>
That means in our develop can make most different DB connections.<br>
We are also many thank for Tiny MCE support the javascript plugin for this demo.<br>
Also you can make your favourite text editor or more plugin.</p>

## Update

<p>We have to move kind of the function from the corss with self build APIs list,<br>
In file `modules/apis.py` we have build kind of the default and open free functions include:<p>

1. Tor / Nor `gun_shell` requests, we have build it with `asyncio` and `aiohttp`, you can also install tor for requesting `.onion` address.
2. jwt Create, yes, we have try something open source persion trust for defances scam and ddos attack to your apps.`<br>`
   basic can make permission with your api requests.
3. GPG Message - We user GnuPG encrypt for singal function, with this demo jwt encodeing `<br>`
   sure you can use your coustom password generator to build with it, but if you need to use `pgpy<br>`
   make flash with pip or update with `python3 -m pip install -U -r request.txt`
4. QRCode - By QR code build with SVG/HTML support return.`<br>`
   Make your between devices can crose over read and run your sevices.
5. We finally break out the `page_loader` for the APIs, as we defind page load and redirect the function somehtings will me multily recall process,
   So now I make sure the `'page_loader` to your script's file and you can recall `apis` and `self-modules` you need.

More of the usage, in each default APIs function, welcome leave me an `issues`

## Configure The Demo

<p>To Run the Flask-CMS, you should install the python3 version.<br>
Support any browser with no plugin or cookies blocking.

1. Create your app [SECRET_KEY ](https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEYhttps://)
2. Config you SECRET_KEY in run.py
3. Update the python modules with pip install -U -r request.txt
4. Our Default post was 5001, and you can change this is the end line of run.py
5. Run the Program with
   [Windows]
   py -3 run.py
   [Linux/Unix/OSX]
   python3 run.py
6. We have use Tiny MCE Editor [Download](https://download.tiny.cloud/tinymce/community/tinymce_5.10.7_dev.zip?_ga=2.5061043.1812686262.1672891546-692894055.1672891546) and move the tinymce filder to Flask-CMS/status/js/tinymce/
7. Supprt Multi text editor for example you can see the load data and update are complely well!
8. Dark Mode 😄 Welcome Bootstrap v5.3 support the `data-bs-them` options for switching theme. We can custoum design all color theme and make it like a setting to save to user client account. :
   ================================================================================================================================================================================
9. We have use Tiny MCE Editor [Download](https://download.tiny.cloud/tinymce/community/tinymce_5.10.7_dev.zip?_ga=2.5061043.1812686262.1672891546-692894055.1672891546) and move the tinymce filder to Flask-CMS/js/
10. If you expect to use the editor in Modal you should make your modal tag after class `data-focus="false" / data-bs-foces="false"`
    *We have already enable the TincyMCE Editor Modal fix with javascript in `static/js/main.js`
11. Updat the basic blog database for ready the multi bolg system.

## New Feature of the build-in API

We are happy to say the build in API are use to help the junior developer to load with GET/POST mehtod to knowing who to make the Flask API with sqlite, The following are the instruction of the API File.

`system/setup.py `<
= The basic system DB create with SQLite DB and Login manager API.

* Create and setup basaic SQLite DB File(s) in 'data_db' and/or 'db' in the project foldoer.
* Host the user aguent sessions.

`system/panel.py` <

* Main 'register' 'account config' 'login/logout'
* Default Blogger Categorys and File(s)) Upload config.

`modules/plugins/blogger/blog.py` <

* Main of Blogger 'Create', 'Update', 'Delete' control.

`modules/plugins/dashboard/dashbpoard_api.py` <

* Page Loader API

`modules/apis.py` <

* API Main Control, `api_loader`
* Default API
  * *(NEW) QR-Code Maker `svgQRmaker` (pip install -U qrocde)
  * pgp Encrypt and Decrypt `pgpEnc` & `phpDec` (pip install -U pgpy)
  * Base64(64bit) Token Generator `tokMaker` & `tokRecovery`
  * Pyhton Country List plugin `CountryList` (pip install -U pycountry)

## First Time Setup

Go to your browser and lonig with http://locahost:8001/login (Port 8001 for default, you can change the debug also in run.py)
And you will see our demo regist link at the bottom.
Regist the account by yourself and start play our demo blogger CMS.

### What Are We Doing?

We are the programmer and developer need the job for life.
I have try to search and test the different CMS and ERP system help the entrepreneur build their business.
Flask is the very amazing Firmwork for your business to accomplish the full system with customization.
You can see more function like UPLOAD / ORDER / EMAIL function are not include with this demo.
Cuz This is the DEMO to tell you how free of our development. You maybe more exterm to Chnage the access password modules to upgrade the secuirty level.
We are make the service for you and grow your business to be more controllable.

### What are the feature can this CMS do?

Menu API with flask access and execute
Full custom CSS and JavaScript comparable.
Include Custom Build API to export data to direct social media
Menu build the custom system with online or localhosting web applications.
Support TSL/SSL (https) request by custom config.
g.e. Restaurant Cashier, CCTV-Viewer
More idea please try to make user require with Email: messiaht@pm.me

### Where can find us?

This is the Developer of [LinkedIn](https://www.linkedin.com/in/freeman-constantine-654341236/https://) Flask-CMS
