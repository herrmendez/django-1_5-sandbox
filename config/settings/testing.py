from .defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = os.path.join(BASE_PATH, 'tests')
TEST_DISCOVER_ROOT = TEST_DISCOVER_TOP_LEVEL
TEST_DISCOVER_PATTERN = 'test_*'

