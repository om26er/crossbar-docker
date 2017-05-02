# [autobahn-js](https://github.com/crossbario/autobahn-js) | amd64 |

#  | [![](https://images.microbadger.com/badges/image/crossbario/

# [![](https://images.microbadger.com/badges/version/crossbario/autobahn-js:full.svg)](https://github.com/crossbario/crossbar-docker/blob/master/autobahn-js/x86_64/Dockerfile.full)

import os

def badger_url(package, flavor):
    return '[![](https://images.microbadger.com/badges/version/crossbario/autobahn-js:full.svg)](https://github.com/crossbario/crossbar-docker/blob/master/autobahn-js/x86_64/Dockerfile.full)'


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

import json
from pprint import pprint

HEADER = """# Crossbar.io Project Docker Images

This repository contains the Docker tooling to build the official
Docker images published by the Crossbar.io Project on Dockerhub
[here](https://hub.docker.com/r/crossbario/).

For building the images yourself, please see [here](BUILDING.md).

## Package Versions

Latest Docker images built on **{BUILD_DATE}** from package versions:

* Crossbar.io {CROSSBAR_VERSION}
* AutobahnJS {AUTOBAHN_JS_VERSION}
* AutobahnPython {AUTOBAHN_PYTHON_VERSION}
* AutobahnC++ {AUTOBAHN_CPP_VERSION}


## Open Issues

AutobahnC++:

* [segfault on armhf](https://github.com/crossbario/autobahn-cpp/issues/166)


## Docker Images

""".format(BUILD_DATE=BUILD_DATE,
           CROSSBAR_VERSION=CROSSBAR_VERSION,
           AUTOBAHN_JS_VERSION=AUTOBAHN_JS_VERSION,
           AUTOBAHN_PYTHON_VERSION=AUTOBAHN_PYTHON_VERSION,
           AUTOBAHN_CPP_VERSION=AUTOBAHN_CPP_VERSION)

PACKAGE_HEADER = """
### {package}

"""

ARCH_HEADER = """
#### {package} on {architecture}

No | Package | Architecture | Image | docker pull
---|---|---|---|---
"""

# [![](https://images.microbadger.com/badges/image/crossbario/autobahn-python-aarch64:cpy3-minimal-tx-0.18.2.svg)](https://microbadger.com/images/crossbario/autobahn-python-aarch64:cpy3-minimal-tx-0.18.2 "Get your own image badge on microbadger.com")

with open('README.md', 'w') as f_out:
    with open('images.json') as f_in:
        data = f_in.read()
        obj = json.loads(data)
        f_out.write(HEADER)
        for image in obj.get('images', []):
            i = 1
            package = image.get('package', None)
            version = image.get('version', None)
            architectures = image.get('architectures', None)
            github = image.get('github', None)
            name = image.get('name', None)
            tags = image.get('tags', [])
            f_out.write(PACKAGE_HEADER.format(package=package))
            for architecture in architectures:
                f_out.write(ARCH_HEADER.format(package=package, architecture=architecture))
                _tags = ', '.join([tag if tag.strip() != '' else '-' for tag in tags])
                for _tag in tags:
                    if package in PACKAGE_TO_VERSION:
                        _tag = _tag.format(version=PACKAGE_TO_VERSION[package])
                    arch = '-{}'.format(architecture) if architecture != 'x86_64' else ''
                    image_id = 'crossbario/{package}{arch}:{tag}'.format(package=package, tag=_tag, arch=arch)
                    # 'autobahn-python-aarch64:cpy3-minimal-tx-0.18.2'
                    fqn = '{package}{arch}:{tag}'.format(package=package, arch=arch, tag=_tag, version=version)
                    badge ='[![](https://images.microbadger.com/badges/image/crossbario/{fqn}.svg)](https://microbadger.com/images/crossbario/{fqn} "Metadata")'.format(fqn=fqn)
                    f_out.write('{i} | [{package}]({github}) | {architecture} | {badge} | [`{image_id}`](https://github.com/crossbario/crossbar-docker/blob/master/{package}/{architecture}/Dockerfile.{tag})\n'.format(badge=badge, package=package, architecture=architecture, github=github, name=name, tag=_tag, tags=_tags, image_id=image_id, arch=arch, i=i))
                    i += 1

