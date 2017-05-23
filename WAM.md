# Web Archive Manifest (WAM) Format

WAM is simple schema for a YAML file (and therefore also for JSON) to specify key aspects of a web archive.

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
      - id: <coll_id_1>
        name: 'Collection 1 Description'

      - id: <coll_id_2>
        name: 'Collection 2 Description'
               ...

    # or, if collection list is unknown/too large to list/dynamic, use a regex:
    # collections: '\d+'

    # optional: if the web archive is primarily focused on certain domains or sites,
    # (but not necessarily limtied to those), these can be included under the 'domain_hint' key
    # This can include top-level domains or any subomdain that the web archive specializes in
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

The main keys in the WAM format are as follows:

- `version` (required): The version of the WAM format, currently 1.0 

- `webarchives`: The top-level key containing all web archives by unique id. At least one web archive should be included.
