import yaml
import os
import pprint
import sys
import re
import pytest
import glob


def load_targets(webarchives='webarchives.yaml'):
    dir_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '..')

    with open(os.path.join(dir_name, webarchives)) as fh:
        config = yaml.load(fh.read())
        for pattern in config['webarchive_index']:
            return glob.glob(os.path.join(dir_name, pattern))


@pytest.fixture(params=load_targets())
def filename(request):
    return request.param


def test_wam_format(filename):
    """ Ensure the yaml file is valid
    and all required fields are present in each api block
    """

    print('Checking ' + filename)

    with open(filename, 'rb') as fh:
        config = yaml.load(fh.read())

    assert(config['version'] == '1.0')

    for name, webarchive in config['webarchives'].items():
        assert(name)
        assert(webarchive['name'])
        assert(webarchive['about'])

        assert(key in ('name', 'about', 'apis', 'domain_hint', 'collections') for key in webarchive.keys())

        has_collections = ('collections' in webarchive)
        if has_collections:
            # must be a list or a regex
            assert(isinstance(webarchive['collections'], list) or re.compile(webarchive['collections']))

        domain_hint = webarchive.get('domain_hint')
        if domain_hint:
            assert(isinstance(domain_hint, list))

        apis = webarchive.get('apis')
        if not apis:
            continue

        assert(api_key in ('memento', 'cdx', 'wayback') for api_key in apis.keys())

        if 'cdx' in apis:
            assert(apis['cdx']['query'])

        if 'memento' in apis:
            assert(apis['memento']['timegate'])
            assert(apis['memento']['timemap'])

        if 'wayback' in apis:
            assert(apis['wayback']['replay'])

            for mode in ['raw', 'rewritten']:
                assert(mode in apis['wayback']['replay'])

                if apis['wayback']['replay'][mode] is None:
                    continue

                assert('{url}' in apis['wayback']['replay'][mode])
                assert('{timestamp}' in apis['wayback']['replay'][mode])

                assert(('{collection}' in apis['wayback']['replay'][mode]) == has_collections)

