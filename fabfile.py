from fabric.api import local

def test_project():
    '''Run tests with correct configuration file.'''
    local('python manage.py test --settings=config.settings.testing')

def upgrade_app(app_name):
    '''Upgrade given app. Eg: fab upgrade_app:Django '''
    local('pip install {0} --upgrade'.format(app_name))
