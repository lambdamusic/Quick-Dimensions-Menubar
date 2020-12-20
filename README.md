
# Quick Dimensions Menubar

An unofficial OSx [menu bar](https://support.apple.com/en-gb/guide/mac-help/mchlp1446/mac) app that makes it quicker to access the [Dimensions](https://app.dimensions.ai/discover/publication) database of scientific research objects. 

Resolve publications and other objects identifiers:

![screenshot](https://raw.githubusercontent.com/lambdamusic/quick-dimensions-menubar/master/img/screenshot1.png)

Quick links to research categories:

![screenshot](https://raw.githubusercontent.com/lambdamusic/quick-dimensions-menubar/master/img/screenshot2.png)


# Installation

Best is to get the [latest prebuilt binary](https://github.com/lambdamusic/quick-dimensions-menubar/releases). 

Download the file `quickdimensions.app.zip` , unzip and right-click open to run it. 

It was built with OSx 11.1, but it *should* work on not-too-older versions too.  


# Development 

QuickDimensions is a python3 app built with [rumps](https://rumps.readthedocs.io/en/latest/). After installing the dependencies, you can run it with: 

```
python quickdimensions
```

## Building the app

Requires `py2app`

```
python setup.py py2app
```


# Comments, bug reports

The Quick-Dimensions app lives on [Github](https://github.com/lambdamusic/quick-dimensions-menubar). You can file [issues]([issues](https://github.com/lambdamusic/quick-dimensions-menubar/issues/new)) or pull requests there. Suggestions, pull requests and improvements welcome!


## Disclaimer

Please note that this is an **unofficial** Dimensions application. I build it half for fun, half because I needed something to speed up my Dimensions searches. 

If others can make use of it, that definitely makes me happier. However I can't guarantee it will work on all OSx versions (especially older ones) nor I can provide support to all issues reported. 






