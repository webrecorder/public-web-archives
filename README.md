# Public Web Archives
![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)

The purpose of this repository is an experiment in creating a distributed listing of web archives.

The list is intended to be easily readable by humans and also in a format that can be processed by new and existing software tools.
 
The goal is to highlight, and help promote the sizable (and growing list!) of publicly accessible web archives all over the world, in a distributed and democratic way. A lot of people may be familiar with "Wayback Machine", but there are actually many wayback machines all over the world. Let's make them more widely known and accessible!


### What format is the list?

The listing is presented in a single file: [webarchives.yaml](webarchives.yaml)

YAML was chosen as it strikes a good balance between readability and being easily processable by a wide variety of tools.

The file contains a top level `webarchives` keys, and each web archive is presented under a unique id.
The web archives are listed alphabetically by id in the file.

The web archive definition for each archive contains different fields based on the type of archive, although there is a lot of repetition in the fields. The focus initially is on clarity rather than conciseness to ensure the format is easy to understand.

The hope is that the format would be self-documenting or at documented directly in the yaml file. The intent is for the format to be a 'living standard' that may adapt as needed.

For more details about the format, please consult the latest version of the file.


### What archives are included in the list?

This is list is specifically for [web archives](https://en.wikipedia.org/wiki/Web_archiving) which preserve and provide web content and make it publicly accessible.

While there are many great archives out there, the list is specifically limited to web archives.


### What other properties must archives have to be included? What is relation to Memento?

The intent is to list archives that present web content archived in their original form as much as possible.

Archives which only present derived content, such as screenshots, can also be included on a case-by-case basis.

The information about the type of content the archive presents can be conveted in the YAML file.

Currently, the archives listed should support one of these methods of accessing web archives:

- The [Memento Protocol](https://tools.ietf.org/html/rfc7089) is one way of making web archive data accessible in a consistent way, and archives that support

- The [CDX Server API v2](https://github.com/ikreymer/pywb/wiki/CDX-Server-API), [CDX Server API v1](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md) provides an alternate API for providing access to web archive index.


### What if a web archive does not support either Memento or CDX API?

A key goal is to include all publicly accessible web archives!

If an archive makes archival web data available publicly, through any interface, it should be possible to include it and
define how it is accessed.

If there is another API spec that should be included, feel free to submit it as a request and/or suggest how it might be included!

For example, a standard "Wayback Machine"-style interface should be enough to include an archive in a defined way, and it need to be limited to this access pattern either.


### Why make such a list here?

The intent of this list is to be:

- open-source and distributed (git is the perfect place for it!)
- independent from any specific product, service or protocol.
- presented in a human and machine-readable format

The list is intended to encourage interoperability and interconnectedness between different web archives.


### Aren't there other archives lists out there already?

It is important to recognize that there are a few existing lists out there, mostly originating from the Memento project:

 - The [Memento Project](http://timetravel.mementoweb.org/) at LANL deserves much credit for starting and maintaining [achivelist.xml](http://labs.mementoweb.org/aggregator_config/archivelist.xml), a list of archives that support the [Memento Protocol](https://tools.ietf.org/html/rfc7089).
   This list is a key part of the [time travel search engine](http://timetravel.mementoweb.org/about/) and [memento aggregator api service](http://timetravel.mementoweb.org/guide/api/)

 - The [ODU Memento Aggregator](https://github.com/oduwsdl/memgator) project also contains such a list: [archives.json](https://github.com/oduwsdl/memgator/blob/master/archives.json)

- Wikipedia also maintains a [Listing of Web archiving initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)

If there are other such lists, feel free to let us know or submit a pull request to include them here.


### Who can contribute? What if I'd like to add/remove a web archive?

Anyone can contribute! We definitely encourage contributions to this repo to make it a truly distributed project:

- If you have a web archive not on the list, and you would like it to be included, feel free to make a PR adding the archive.

- If you have a web archive on the list, and you would like to remove it, feel free to make a PR and a brief note requesting the removal.

- If you have a question about how to include a new type of web archive, please open an issue to discuss.

- If you would like to make your fork, public or private, feel free to do that as the list is released into the public domain under CC0.


### How does this relate to the Webrecorder project?

The [Webrecorder project](https://webrecorder.io/) aims to promote distributed web archiving, encouraging others to create and run their own web archives. Having a growing web archive list aligns perfectly with these goals.

Webrecorder may use this list to help users augment existing public web archives and create new archives.


### Why isn't Webrecroder included in this list?

Good question! Mostly because there is not a single access point for public collections. Webrecorder allows users to create public and private collections, and there is not a way to access the content that users have made public through a single access point.

This question will help us motivate to solve this issue :)


### License

This document and the accompanying webarchives.yaml list are released into the public domain under CC0.
