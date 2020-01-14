import pytest
import os
from copy import deepcopy

from futura.storage import storage
from futura.loader import FuturaLoader


IS_TRAVIS = 'TRAVIS' in os.environ
IS_APPVEYOR = 'APPVEYOR' in os.environ

if IS_TRAVIS:
    IS_PR = os.environ.get('TRAVIS_PULL_REQUEST', False) != False
elif IS_APPVEYOR:
    IS_PR = os.environ.get('APPVEYOR_PULL_REQUEST_NUMBER', False) != False
else:
    IS_PR = False

if not IS_PR:

    if IS_TRAVIS or IS_APPVEYOR:
        EI_USERNAME = os.environ['EI_USERNAME']
        EI_PASSWORD = os.environ['EI_PASSWORD']
        WRITE_CONFIG = False
    else:
        config = storage.config
        if config is not None:
            if "ecoinvent" in config:
                EI_USERNAME = config['ecoinvent'].get('username')
                EI_PASSWORD = config['ecoinvent'].get('password')
                WRITE_CONFIG = False
else:
    EI_USERNAME = None
    EI_PASSWORD = None
    WRITE_CONFIG = False

TEST_ASSET_PATH = os.path.join(os.path.dirname(__file__), 'tests', 'assets')

print(TEST_ASSET_PATH)


BASE_PROJECT = 'FuturaTest'
BASE_DATABASE = 'ecoinvent3_6'
BASE_DATABASE_VERSION = '3.6'
BASE_DATABASE_SYSTEM_MODEL = 'cut-off'

BASE_RECIPE = dict(metadata={'base_project': BASE_PROJECT,
                             'base_database': BASE_DATABASE,
                             'output_database': BASE_DATABASE,
                             'ecoinvent_version': BASE_DATABASE_VERSION,
                             'ecoinvent_system_model': BASE_DATABASE_SYSTEM_MODEL,
                             'description': 'This Futura recipe loads the ecoinvent {} {} database'.format(
                                 BASE_DATABASE_VERSION, BASE_DATABASE_SYSTEM_MODEL)},
                   actions=[{'action': 'load',
                             'tasks': [{'function': 'extract_bw2_database',
                                        'kwargs': {'project_name': BASE_PROJECT,
                                                   'database_name': BASE_DATABASE}}]}])

BASE_LOADER_FILE = 'test_base.fl'

ORIGINAL_CONFIG = deepcopy(storage.config)


@pytest.fixture(scope='session')
def loader():

    loader = FuturaLoader()

    loader.recipe = BASE_RECIPE

    loader.run()

    # Uncomment this if we need to write the base database in future
    # loader.write_database()

    # Uncomment this if we need to save and reload the base database in future
    # loader.save(os.path.join(TEST_ASSET_PATH, BASE_LOADER_FILE))

    return loader


@pytest.fixture(scope='session', autouse=True)
def setup_fixtures(request):
    print('running setup fixture')

    def teardown_fixtures():
        print('tearing down')

    request.addfinalizer(teardown_fixtures)
