#!/usr/bin/python

import os
import sys
import json
from pprint import pprint

REGISTRY = 'crossbar.local:5000'

BUILD_DATE = os.environ.get('BUILD_DATE', None)
CROSSBAR_VERSION = os.environ.get('CROSSBAR_VERSION', None)
AUTOBAHN_JS_VERSION = os.environ.get('AUTOBAHN_JS_VERSION', None)
AUTOBAHN_PYTHON_VERSION = os.environ.get('AUTOBAHN_PYTHON_VERSION', None)
AUTOBAHN_CPP_VERSION = os.environ.get('AUTOBAHN_CPP_VERSION', None)

PACKAGE_TO_VERSION = {
    'crossbar': CROSSBAR_VERSION,
    'autobahn-js': AUTOBAHN_JS_VERSION,
    'autobahn-python': AUTOBAHN_PYTHON_VERSION,
    'autobahn-cpp': AUTOBAHN_CPP_VERSION,
}

IMAGES = [
    'debian:stretch',
]

with open('images.json') as f_in:
    data = f_in.read()
    obj = json.loads(data)
    for image in obj.get('images', []):
        package = image.get('package', None)
        architectures = image.get('architectures', None)
        tags = image.get('tags', [])
        for architecture in architectures:
            for _tag in tags:
                if package in PACKAGE_TO_VERSION:
                    _tag = _tag.format(version=PACKAGE_TO_VERSION[package])
                arch = '-{}'.format(architecture) if architecture != 'x86_64' else ''
                image_id = 'crossbario/{package}{arch}:{tag}'.format(package=package, tag=_tag, arch=arch)
                IMAGES.append(image_id)


IMAGES = [
    # Debian Stretch
    'debian:stretch',
    'aarch64/debian:stretch',
    'armhf/debian:stretch',

    # Debian Jessie
    'debian:jessie',
    'aarch64/debian:jessie',
    'armhf/debian:jessie',

    # Alpine
    'alpine',
    'armhf/alpine',
    'aarch64/alpine',

    # Ubuntu Xenial
    'ubuntu:xenial',
    'armhf/ubuntu:xenial',
    'aarch64/ubuntu:xenial',

    # Ubuntu Trusty
    'ubuntu:trusty',
    'armhf/ubuntu:trusty',
    'aarch64/ubuntu:trusty',

    # Python
    'python',
    'python:2',
    'armhf/python',
    'armhf/python:2',
    'aarch64/python',
    'aarch64/python:2',

    # Node
    'node',
    'armhf/node',
    'aarch64/node',

    # Node RED
    'nodered/node-red-docker',
]

for image in IMAGES:
    os.system('docker pull {image}'.format(image=image))
    os.system('docker tag {image} {registry}/{image}'.format(image=image, registry=REGISTRY))
    os.system('docker push {registry}/{image}'.format(image=image, registry=REGISTRY))
