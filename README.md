# Public Web Archives

The purpose of this repository is an experiment in creating a distributed listing of web archives.

To accomplish, a new format, the [Web Archive Manifest](WAM.md) is introduced to describe web archives and what properties and APIs they support. The format is designed to be readable by humans and processed by new and existing software tools.

The goal is to highlight, and help promote the sizable (and growing list!) of publicly accessible web archives all over the world, in a distributed and democratic way.

A lot of people may be familiar with "Wayback Machine", but there are actually many wayback machines all over the world. Let's make them more widely known and accessible!

### How are the web archives listed? How can new archives be included?

There is a YAML file following the [WAM spec](WAM.md) for each web archive in the [webarchives](webarchives/) directory.

YAML was chosen as it strikes a good balance between readability and is easily processable by a wide variety of tools in a variety of languages.

The intent is for the format to be a 'living standard' that may adapt as needed as web archives evolve.

There is also an [index](webarchives.yaml) which specifies to include all files in the directory.

To add a new web archive, simply add a new .yaml file in this directory.


### What archives are included in the list?

This listing is specifically for [web archives](https://en.wikipedia.org/wiki/Web_archiving) which preserve and provide web content and make it publicly accessible.

While there are many great archives out there, this format and directory is specifically limited to web archives.


### What other properties must archives have to be included?

Any web archive can be included in the listing, even if they do not support any of the established apis.

For a list of currently supported apis, see the [WAM Spec](WAM.md)

This directory should also not be seen as an exhaustive list of all web archive apis, as many may support, custom or specific apis.

If there is another api spec that should be included in this shared listing, feel free to submit it as a request and/or suggest how it might be included!


### Why make a new web archive directory?

The intent of this directory is to be:

- open-source and distributed (git is the perfect place for it!)
- independent from any specific product, service or protocol.
- presented in a human and machine-readable format

This directory and WAM format are intended to encourage interoperability and interconnectedness between different web archives.


### Aren't there other archives lists out there already?

Yes! It is important to recognize that there are a few existing lists out there, mostly originating from the Memento project.

 - The [Memento Project](http://timetravel.mementoweb.org/) at LANL deserves much credit for starting and maintaining [achivelist.xml](http://labs.mementoweb.org/aggregator_config/archivelist.xml), a list of archives that support the [Memento Protocol](https://tools.ietf.org/html/rfc7089).
   This list is a key part of the [time travel search engine](http://timetravel.mementoweb.org/about/) and [memento aggregator api service](http://timetravel.mementoweb.org/guide/api/)

 - The [ODU Memento Aggregator](https://github.com/oduwsdl/MemGator) project also contains such a list: [archives.json](https://oduwsdl.github.io/MemGator/archives.json)

 - The [oldweb.today](http://oldweb.today/) project uses an earlier version of such a list: [archives.yaml](https://github.com/oldweb-today/netcapsule/blob/master/archives.yaml) This list is used to provide archives accessible via the service.

 - Wikipedia also maintains a [Listing of Web archiving initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)

If there are other such lists, feel free to let us know or submit a pull request to include them here.


### Who can contribute? What if I'd like to add/remove a web archive?

Anyone can contribute! We definitely encourage contributions to this repo to make it a truly distributed project:

- If you have a web archive not in the directory, and you would like it to be included, feel free to make a PR adding the archive to a new yaml file.

- If you have a web archive that is included, and you would like to remove it, feel free to make a PR and a brief note requesting the removal.

- If you have a question about how to include a new type of web archive, please open an issue to discuss.

- If you would like to make your fork, public or private, feel free to do that as the list is released into the public domain under CC0.


### Any plans for extending this format? How could it be made more distributed?

Yes! Currently, all the web archives are specified explicitly in this repository.

However, it would be really great if web archives start to 'advertise' what APIs they support and other information included in the WAM file.

For example, an archive could provide: ``http://myarchive.example.com/wam.yaml`` and then the file need not be stored in this repository, and we would only need to add this url to the [index](webarchives.yaml)

If adding support for WAM to a web archive, please let us know or submit a PR to include this information.


### What tools use this listing?

None yet!

But we hope that this will change, and would be happy to add any tools that make use of this format or listing, directly or directly.

A future release of [pywb](https://github.com/ikreymer/pywb) will likely add support for reading WAM format files.

[Webrecorder](https://webrecorder.io/) may also use this directory to provide users the ability to work with existing web archives.


### Who created this listing?

This web archive listing and the [WAM](WAM.md) format originates with the [Webrecorder project](https://github.com/webrecorder/), which aims to promote distributed web archiving, encouraging anyone to create and run their own web archives. Having a formal Web Archive Manifest, as well as a public, distributed web archive directory aligns perfectly with this mission.


### License
![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)

This document, the [WAM](WAM.md) format and the accompanying [web archive directory](webarchives) are released into the public domain under CC0.
