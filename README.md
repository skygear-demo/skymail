# Skymail

### Adaptor to send email via static HTML forms - via Gmail or other mailing services.

Making use of [Skygear](https://skygear.io) Cloud Function to send form data to emails from static website (with simple HTML page templates)

## Demo

[DEMO](https://mailtest.skygeario.com/static) - hosted at Skygear hosting

In the demo example, we are using a default email account from Gmail: `margin.top.20px@gmail.com` to send testing mails. Which means: **Quota may exeed.**

Desipte using the default settings works, You are advised to **fork and deploy your own version** on [Skygear](https://skygear.io), with custom email server settings (in [settings.py](settings.py)). See how to set up [here](#setup).

## Features

### Need a email sender for sending email on a static web page?

- Easily set up Cloud Function handler to send email via SMTP
- Google Recaptcha enabled by default
- Simple API call
- Custom SMTP server supported
- Embed into your static site easily
- Standalone and customizable static HTML page templates

## Setting up a form
<a name="setup"></a>

### Prepare your SMTP server / service

These are available choices:

- [Sendgrid](https://sendgrid.com/docs/Integrate/index.html#-SMTP-Relay)
- [Gmail](https://support.google.com/a/answer/176600?hl=en)
 	- Limit: 2000 messages per day
	- If you have G Suite, you can sent to 10000 recipients per day
- Your own SMTP server

Gmail is recommended for low volume usage; and Sendgrid is recommended if you send massive emails.

### Setting up the Cloud Function on Skygear

- Sign up with [Skygear](https://portal.skygear.io) to deploy the sender on your site
- Clone this repo
- Update settings accordingly in `settings.py`
- Set up [Google Recatpcha](https://www.google.com/recaptcha), requires API Key and secret to enable, update them in `settings.py` and html page `data-sitekey`
- Update the template UI as you wish
- Update Skygear API Endpoint and API Key (in HTML files)
- Deploy updated code to Skygear - using [Skycli](https://github.com/SkygearIO/skycli).
- Try it out! Hosted at `/static/` of your app path.

## Custom Settings

You can set up custom settings in [settings.py](settings.py).

### Turning off recaptcha (not recommended)

If you find recaptcha unneccessary, you may turn if off by setting `enable_grecaptcha` to `False`.

```python
config = {
    "default_sender": "David Ng<me@davidng.hk>",
    "default_reply_to": "me+skymail@davidng.hk",
    "enable_grecaptcha": False,
    "grecaptcha_secret": 'IGNORE THIS FIELD'
}
```
### Set default user names
Update `default_sender` as the address and name you wish to send as.

Update `default_reply_to` as the reply-to address.

```python
config = {
    "default_sender": "Peter Smart<peter.smart@gmail.com>",
    "default_reply_to": "reply.peter@gmail.com",
    "enable_grecaptcha": True,
    "grecaptcha_secret": 'ADD YOUR GOOGLE RECAPTCHA HERE'
}
```

## Usage Examples

- Subscription forms
- Sign up for more information
- Web app sign up confirmation
- Auto welcome email (using cloud functions part without the form)
- Receive support requests

## Develop (Cloud Functions)
- Cloud function using Python 3.6. [Installation Guide](http://docs.python-guide.org/en/latest/starting/install3/osx/).
- Initialize an virtual env for the first time. [Follow this guide.](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```python3 -m venv env```

```source env/bin/activate```

Note: If there is error when running `pip install -r requirements.txt` on `Python3.6`, you may need to use `easy_install pyzmail` to install pyzmail instead.

## Credits

- Using [pyzmail](http://www.magiksys.net/pyzmail/) for the SMTP mailing function - a neat and lightweight Python library.

## Contribution
Feel free to open any issue and PR. Contact at [hello+skymail@skygear.io](hello+skymail@skygear.io) or fill in the form [here]().

### About Skygear
[Skygear](https://skygear.io) is an open-source backend for apps. You can write plugins to enrich your application. Skymail is a perfect example to demostrate the use of cloud functions.

Besides sending emails, Skygear is suitable for writing simple or even database-connected cloud functions.