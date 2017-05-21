# Public Web Archives

The purpose of this repository is an experiment in creating a distributed listing of web archives.

The list is intended to be easily readable by humans and also in a format that can be processed by new and existing software tools.
 
The goal is to highlight, and help promote the sizable (and growing list!) of publicly accessible web archives all over the world, in a distributed and democratic way. A lot of people may be familiar with "Wayback Machine", but there are actually many wayback machines all over the world. Let's make them more widely known and accessible!


### What format is the list?

The listing is presented in a single file: [webarchives.yaml](webarchives.yaml)

YAML was chosen as it strikes a good balance between readability and being easily processable by a wide variety of tools.

The file contains entries for each known web archive and what common APIs the web archive supports.

The hope is that the format would be mostly self-documenting and/or documented directly in the yaml file. The intent is for the format to be a 'living standard' that may adapt as needed.

For more specifics about the current format, please consult the latest version of the file.


### What archives are included in the list?

This is list is specifically for [web archives](https://en.wikipedia.org/wiki/Web_archiving) which preserve and provide web content and make it publicly accessible.

While there are many great archives out there, the list is specifically limited to web archives.


### What other properties must archives have to be included?

The intent is to list archives that present web content archived in their original form as much as possible, and/or archives that support established web archiving APIs for interoperability.

However, archives which only present derived content, such as screenshots, can also be included on a case-by-case basis.

Currently, endpoints for the following common web archiving APIs, if supported by the web archive, are included in the list:

- `memento` -- Support for [Memento Protocol](https://tools.ietf.org/html/rfc7089), the appropriate endpoints should be included.

- `cdx` -- Support for [CDX Server API v2](https://github.com/ikreymer/pywb/wiki/CDX-Server-API), [CDX Server API v1](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md)

- `wayback` -- Support for 'Wayback Machine'-style replay, some variation of timestamp + url to access archived urls.

It should still be possible to include public web archives, even if they do not support any of these established APIs.

And of course, web archives are likely to support other, custom APIs, which are not listed in the file.

If there is another API spec that should be included, feel free to submit it as a request and/or suggest how it might be included!


### Why make such a list here?

The intent of this list is to be:

- open-source and distributed (git is the perfect place for it!)
- independent from any specific product, service or protocol.
- presented in a human and machine-readable format

The list is intended to encourage interoperability and interconnectedness between different web archives.


### Aren't there other archives lists out there already?

Yes! It is important to recognize that there are a few existing lists out there, mostly originating from the Memento project.

 - The [Memento Project](http://timetravel.mementoweb.org/) at LANL deserves much credit for starting and maintaining [achivelist.xml](http://labs.mementoweb.org/aggregator_config/archivelist.xml), a list of archives that support the [Memento Protocol](https://tools.ietf.org/html/rfc7089).
   This list is a key part of the [time travel search engine](http://timetravel.mementoweb.org/about/) and [memento aggregator api service](http://timetravel.mementoweb.org/guide/api/)

 - The [ODU Memento Aggregator](https://github.com/oduwsdl/memgator) project also contains such a list: [archives.json](https://github.com/oduwsdl/memgator/blob/master/archives.json)
 
 - The [oldweb.today](http://oldweb.today/) project uses an earlier version of such a list: [archives.yaml](https://github.com/oldweb-today/netcapsule/blob/master/archives.yaml) Thie list is used to provide archives accessible via the service.

 - Wikipedia also maintains a [Listing of Web archiving initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)

If there are other such lists, feel free to let us know or submit a pull request to include them here.


### Who can contribute? What if I'd like to add/remove a web archive?

Anyone can contribute! We definitely encourage contributions to this repo to make it a truly distributed project:

- If you have a web archive not on the list, and you would like it to be included, feel free to make a PR adding the archive.

- If you have a web archive on the list, and you would like to remove it, feel free to make a PR and a brief note requesting the removal.

- If you have a question about how to include a new type of web archive, please open an issue to discuss.

- If you would like to make your fork, public or private, feel free to do that as the list is released into the public domain under CC0.


### What tools use this list?

None yet!

But we hope that this will change, and would be happy to add any tools that make use of this list, directly or directly.

A future release of [pywb](https://github.com/ikreymer/pywb) will likely add support for reading this list directly.

[Webrecorder](https://webrecorder.io/) may use this list to provide users the ability to work with existing web archives.


### Who created this list?

This list originates with the [Webrecorder project](https://github.com/webrecorder/), which aims to promote distributed web archiving, encouraging anyone to create and run their own web archives. Having a public, distributed web archive list aligns perfectly with this mission.

You may note that Webrecorder is not yet included in this list! This is mostly due to to current technical limitations. Webrecorder allows users to create public and private collections, and there is not yet a way to access the content that users have made public through a single access point. This answer is here to remind us to solve this issue :)


### License
![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)

This document and the accompanying [webarchives.yaml](webarchives.yaml) list are released into the public domain under CC0.
