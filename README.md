
# Quick Dimensions Menubar

An unofficial OSx [menu bar](https://support.apple.com/en-gb/guide/mac-help/mchlp1446/mac) app that makes it quicker to access the [Dimensions](https://app.dimensions.ai/discover/publication) database of scientific research objects. 

Resolve publications and other objects identifiers:

![screenshot](https://raw.githubusercontent.com/lambdamusic/quick-dimensions-menubar/master/img/screenshot1.png)

Quick links to research categories:

![screenshot](https://raw.githubusercontent.com/lambdamusic/quick-dimensions-menubar/master/img/screenshot2.png)


# Installation

Best is to get the [latest prebuilt binary](https://github.com/lambdamusic/quick-dimensions-menubar/releases). 

Download the file `QuickDimensions.app.zip` , unzip and right-click open to run it. 

It was built with OSx 11.1, but it *should* work on not-too-older versions too.  

## Opening the app

The first time you'll probably have to **right-click** on it and select 'Open', instead of just double-clicking on it. This is because the app doesn't come from the App Store and hence the OS flags it as [potentially malicious](https://www.cultofmac.com/672576/cant-launch-your-apps-on-macos-catalina-heres-the-fix/). 


# Development 

QuickDimensions is a python3 app built with [rumps](https://rumps.readthedocs.io/en/latest/). After installing the dependencies, you can run it with: 

```
python QuickDimensions
```

## Building the app

Requires `py2app`

```
python setup.py py2app
```

# FAQs

* Do I need a subscription to use Dimensions? 

No, although Dimensions has paid-for plans for professional use, you will be able to search it and access individual record pages (eg publications metadata) free-of-charge. 

* Is this app free? 

Yes this app is free as in beer. I build it half for fun, half because I needed something to speed up my Dimensions searches.
If others can make use of it, that definitely makes me happier. And if you like it please give it a star!

* Why doesn't it work on OSx version X/Y/Z ? 

I tested and built the app on a mac running macOS Big Sur, version 11.1. The app should work on recent OS versions but I can't guarantee that, nor test it. 

If you know your way around Python it's pretty easy to download the source code and build the app executable on your mac (see the section above).


# Comments, bug reports

The Quick-Dimensions app lives on [Github](https://github.com/lambdamusic/quick-dimensions-menubar). You can file [issues]([issues](https://github.com/lambdamusic/quick-dimensions-menubar/issues/new)) or pull requests there. Suggestions, pull requests and improvements welcome!


## Disclaimer

Please note that this is an **unofficial** Dimensions application. 







