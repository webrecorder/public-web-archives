import yaml
import os
import pprint

def test_format(filename):
    """ Ensure the yaml file is valid
    and all required fields are present in each api block
    """

    fullpath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '..',
                            filename)

    with open(fullpath, 'rb') as fh:
        config = yaml.load(fh.read())

    for name, webarchive in config['webarchives'].items():
        assert(name)
        assert(webarchive['name'])
        assert(webarchive['about'])

        apis = webarchive.get('apis')
        if not apis:
            continue

        if 'cdx' in apis:
            assert(apis['cdx']['query'])

        if 'memento' in apis:
            assert(apis['memento']['timegate'])
            assert(apis['memento']['timemap'])

        if 'wayback' in apis:
            assert(apis['wayback']['prefix'])
            assert(apis['wayback']['calendar_suffix'])
            assert(apis['wayback']['replay_suffix'])

            assert('raw' in apis['wayback']['replay_suffix'])
            assert('rewritten' in apis['wayback']['replay_suffix'])

    #pprint.pprint(config['webarchives'])

    print('{0} is valid'.format(filename))

if __name__ == "__main__":
    filename = 'webarchives.yaml'

    try:
        test_format(filename)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print('{0} is not valid, see error above!'.format(filename))

