import constants
import exceptions
from base64 import b64decode
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import os.path
import json
from collections import OrderedDict

PROJECT_ROOT = '/Users/jrp/projects/super_source/python/super_source/' # TODO update this

class Project:
    projects = []

    def __init__(self, name, api_token, options={}):
        self.name = name
        self.api_token = api_token
        self.options = options
        if 'level' not in self.options:
            self.options['level'] = 'error'
        self.client_data = self.load_client_data()
        self.client_token = self.load_client_token()

    def filename(self, filetype):
        return PROJECT_ROOT + '/projects/' + self.name + '.' + filetype

    def data_filename(self):
        return self.filename('json')

    def token_filename(self):
        return self.filename('token')

    def load_client_data(self):
        if os.path.isfile(self.data_filename()):
            return json.loads(open(self.data_filename(), 'r').read(), object_pairs_hook=OrderedDict)
        else:
            return {}

    def load_client_token(self):
        if os.path.isfile(self.token_filename()):
            return open(self.token_filename(), 'r').read()
        else:
            return None

    def is_valid(self):
        if not self.client_token or not self.client_data:
            return False

        if (('project_api_token' not in self.client_data) or
          self.client_data['project_api_token'] != self.api_token):
            return False

        return self.is_valid_crypto()

    def is_valid_crypto(self):
        public_key_path = constants.PACKAGE_ROOT + '/other/supso2.pub'
        public_key = open(public_key_path, 'r').read()
        digest = SHA256.new()
        digest.update(json.dumps(self.client_data, separators=(',', ':')))
        rsa_key = RSA.importKey(public_key)
        signer = PKCS1_v1_5.new(rsa_key)
        decoded_token = b64decode(self.client_token)
        return bool(signer.verify(digest, decoded_token))

    def ensure_required(self):
        if not self.is_valid():
            raise exceptions.InvalidProjectToken("Invalid Super Source token for project: " + self.name + "\n" + exceptions.HELP_MESSAGE)

    @staticmethod
    def add(*args):
        project = Project(*args)
        Project.projects.append(project)
        project.ensure_required()
