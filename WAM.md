# Web Archive Manifest (WAM) Format

WAM is simple schema for a YAML file (and therefore also for JSON) to specify key aspects of a web archive.

## Sample definition

A WAM file contains the following structure:

```  yaml
version: '1.0'

webarchives:

  <unique_id>:

    name: 'My Example Web Archive'
    about: 'http://webarchive.example.com/'

    # optional: supported collection
    # if the web archive is multi-collection archive,
    # the 'collections' can be used to indicate the collections
    # and  the {collection} variable can be used in any of the api urls

    # if the collection list is known:
    collections:
      - id: coll_1
        name: 'Collection 1 Description'

      - id: coll_2
        name: 'Collection 2 Description'
               ...

    # or, if collection list is unknown/too large to list/dynamic, use a regex:
    # collections: '\d+'

    # optional: if the web archive is primarily focused on certain domains or sites,
    # (but not necessarily limited to those), these can be included under the 'domain_hint' key
    # This can include top-level domains or any subdomain that the web archive specializes in
    domain_hint:
      - .tld
      - .example.com

    # optional: known apis supported by the web archive, if any, are added here
    apis:
      # add if archive supports Memento Protocol API
      memento:
        timegate: 'http://webarchive.example.com/timegate/'
        timemap:  'http://webarchive.example.com/timemap/'

      # add if archive supports CDX Server APIs
      cdx:
        query: <a url to CDX Server endpoint>

      # add if the archive supports 'Wayback Machine' style calendar + replay
      wayback:
        calendar: http://webarchive.example.com/path/*/
        replay:
          rewritten: http://webarchive.example.com/path/{timestamp}/{url}

          # if an archive doesn't support 'raw' replay, adding: 'raw: NULL' is preferred
          raw: http://webarchive.example.com/path/{timestamp}id_/{url}
```


## Required Keys

A WAM format file should have at least the following keys:

- `version`: The version of the WAM format (currently 1.0)

- `webarchives`: The top-level key containing one or more web archives by unique id.

- `name`: Human readable name of the web archive.

- `about`: A URL to a page about the web archive.

## Optional Keys

- `collections`: If the web archive is a multi-collection archive, possibly specify the collections. See [Collections](#collections) for more info.

- `domain_hint`: if the web archive is primarily focused on a specific domain(s), such as certain top-level domains, or certain other domains, these can be added here as a list. This list is only a 'hint' and does not mean the web archive only has those domains, or doesn't have content from any other domains.

- `apis`: Includes sections for apis that the web archive supports. More below.

- `webarchive_index`: A list of where to find other WAM files, see [WAM Index](#wam-index)

## APIs

Currently supported apis are as follows. Each api has subkeys pointing to urls that are part of the api.

### Memento

The `memento` key should be included if the web archive implements support for the [Memento Protocol](https://tools.ietf.org/html/rfc7089).

The definition object should have a key for the `timegate` and `timemap`, pointing to the Memento TimeGate and TimeMap urls for the web archive.

### CDX Server

The `cdx` key should be included if the web archive supports either [IA CDX Server](https://github.com/ikreymer/pywb/wiki/CDX-Server-API) or the [pywb CDX Server API](https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md) in some form. Both apis are very similar and are identical for majority of use cases.

The definition object should have a single key `query`, pointing to the CDX server endpoint.

### Wayback

The `wayback` key should be included if the web archive supports the "Wayback Machine"-style web archive access, using a combination of timestamp and url. This key should be included if the web archive is running some version of wayback machine, or wayback machine-like service.

Generally, such as service will have an HTML calendar page, listing captures of a singe url over time. This page should be listed under the `calendar` key, if available.

The replay endpoints for the wayback machine service should be included under the `replay` key.

- If the web archive provides content in any way modified/rewritten, it should be listed under `rewritten` key.
- If the web archive provides access to raw web content (even better!) it should be included in the `raw` key

### Url Templates

Special url template variables, `{url}` and `{timestamp}` may be included in any api url. These represent the url and timestamp and indicate how these are to be inserted into the apis. These variables are optional and if they are omitted, established conventions for passing url and timestamp should be used.

## Collections

If a web archive supports collections, a list of collections may be included in the `collections` key.

If it is not possible to list all the collections, the `collections` key should be a regular expression that indicates possible values
that are valid collection ids.

If including a full list of collections, it should be a list of objects that contain a `id` and `name` field.

Any api url may contain an additional `{collection}` template variable if and only if a `collections` key is defined.

The `id` values from the collection list should then be substitutable to get valid collection urls, eg:

``` yaml
    collections:
      - id: coll_1
        name: 'Collection 1 Description'

      - id: coll_2
        name: 'Collection 2 Description'

    api:
      wayback:
        calendar: http://myarchive.example.com/{collection}/*/{url}
        replay:
          rewritten: http://myarchive.example.com/{collection}/{timestamp}/{url}
          raw: http://myarchive.example.com/{collection}/{timestamp}id_/{url}
```

Based on this definition,

`http://myarchive.example.com/coll_1/*/http://example.com/` and `http://myarchive.example.com/coll_2/*/http://example.com/` should both be valid calendar paths.


## WAM Index

It is also possible to define an index that indicates how to find other WAM files.

The `webarchive_index` key provides a list of files, directories or urls to load:


``` yaml

    version: '1.0'

    # all known web archives
    webarchive_index:
      - 'webarchives/*.yaml'
      - 'some_other/myarchive.yaml'
      - 'http://webarchive1.example.com/wam.yaml'
      - 'http://webarchive2.example.com/wam.yaml'
```

Web archives manifests loaded from multiple files should be considered the same as if they were all loaded under a single `webarchives` key in a single file.

In this example, the urls might specify that the WAM file should be loaded directly from the web archive server.

This pattern should allow web archives to serve their own WAM definition and contribute to a more distributed index.

