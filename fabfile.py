from fabric.api import local

def test_project():
    '''Run tests with correct configuration file.'''
    local('python manage.py test --settings=config.settings.testing')
