import os

def _detect_project_root():
    project_root = os.getcwd()
    base_file_names = ['Gemfile', 'package.json', '.supso', 'environment.yml', 'requirements.txt', 'setup.py']
    #while True:
    #    if project_root == "":
    #        break
    #    
    # TODO finish this
    
    return path

PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = _detect_project_root()
PROJECT_SUPSO_CONFIG_ROOT = PROJECT_ROOT + '/.supso' if PROJECT_ROOT else None
USER_SUPSO_CONFIG_ROOT = os.path.expanduser('~')

print PACKAGE_ROOT
print PROJECT_ROOT
print PROJECT_SUPSO_CONFIG_ROOT
print USER_SUPSO_CONFIG_ROOT
