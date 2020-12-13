# Stock Price Announcer

Stock Price Announcer is a Python script that will announce live stock prices for you.

### Installation

SPA requires the following packages installed in order for it work.

 - Text-to-Speech -> [pyttsx3](https://pypi.org/project/pyttsx3/)
 - HTTP Requests -> [requests](https://requests.readthedocs.io/en/master/user/install/#install)
```sh
$ pip install pyttsx3
$ pip install requests
```

### Usage

Add `stock_name: stock_ticker` to `stocks` dictionary in `main.py` to announce more stocks.

### Schedule stock announcements using `crontab`

You will need to add a cronjob in your terminal. Do this by using the `crontab -e` command.

```sh
$ crontab -e #opens a vim file to which you can add a cronjob
```
Use [crontab.guru](https://crontab.guru/) to create a schedule. For example: `0,30 9-16 * * 1-5` would announce every 30 minutes of every trading day of the week.

##### What do add to crontab vim file

`0,30 9-16 * * 1-5 cd ~/path_to_scripts_folder && path_to_python main.py`

You can find your path to python by running
```sh
$ which python
```
or
```sh
$ which python3
```