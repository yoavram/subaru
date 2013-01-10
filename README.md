# Subaru
## Auto-Sub: Automatic Subtitle Downloader

## Overview
Subaru is designed to overcome subtitle websites such as [subscenter] and [torec] which give free subtitles but require multiple mouse clicks, in the browser and in the desktop to choose the series, season, episode and version and then open the downloaded file and unzip it. Moreover, they require registration, or otherwise the user must "wait" for several seconds before each download.

Subaru automates this process.

## Support 

Currently Subaru works with the hebrew subtitle site [subscenter] but can be easily extended by developers familiar with Python, HTML and some jQuery.
It would probably be easiest to extend it to work with [Bsubs] because [subscenter] is the Hebrew version of [Bsubs].

## Requirements

1. Python 2.7 (other versions might work as well)
2. [Requests] to request URL from subtitle websites
3. [Spynner] to browse subtitle websites in headless mode
4. [PyQuery] to parse and query HTML 
5. [FeedParser] to parse subtitle feeds

I wrote Subaru on Windows 7 but it should work on any platform with Python.

## Install

After installing all the requirements, you need to clone this repo:

```
git clone https://github.com/yoavram/subaru.git
```

## Configuration

You should open `subscenter.py` and change the constants:
1. `OUTPUT_PATH` - subtitle files (`.srt`) will be downloaded to this folder
2. `FAVORITES` - a list of hebrew names of favorite series to download from the *latest* feed

## Usage

There are two usage modes:

### Latest Favorites

This mode is run by simply calling 
```
$ python subscenter.py
```
Subaru will get the latest episodes feed from [subcenter] and search it for the series in the `FAVORITES` constant. It will then download subtitles for every episode it finds.

### On demand

In this mode you can specificaly download an episode and even specify the version:
```
$ python subscenter.py <series-name> <season-number> <episode-number> [version-keyword]
```
  * <series-name> is the name as it appears in the URL of the series page. It is all lowercase and dashes (`-`) are used instead of spaces, without any other punctuation (examples: `modern-family`, `greys-anatomy`, `the-big-bang-theory`)
  * <seasnon-number>/<episode-number>: no need for preciding zero (`1` not `01`).
  * [version-keyword] is an *optional* argument. Subaru will only download subtitles that have this keyword in the filename. Use this to specifiy the version you want. Exampes: `LOL`, `DivX`.

If the episode was not found a proper message will appear, so feel free to use this to check if a subtitle has been uploaded.

## Contributing

If you want to add support for another site please create a new file `<site-name>.py` Try to respect the function names in `subscenter.py` if you can. 
I'm not sure that this project needs to be abstracted or anything like this - the code is very simple, mainly due to the amazing strength and usability of the modules used (see *requirements*).

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.

Subaru, of course, is a fine car company and is not affiliated with this project. The name is just a reference to the automation of the subtitle downloading process - auto-sub in Hebrew sounds like "Subaru car".


[subscenter]: http://www.subscenter.org/
[torec]: http://torec.net/
[Requests]: http://python-requests.org/
[Spynner]: https://github.com/makinacorpus/spynner
[FeedParser]: http://code.google.com/p/feedparser/
[PyQuery]: https://github.com/gawel/pyquery/
[Bsubs]: http://www.bsubs.com/en/
