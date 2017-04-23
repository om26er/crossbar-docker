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


import json
from pprint import pprint

HEADER = """# Crossbar.io Project Docker Images
## Package Versions

Docker images last built on **{BUILD_DATE}** from package versions:

* Crossbar.io {CROSSBAR_VERSION}
* AutobahnJS {AUTOBAHN_JS_VERSION}
* AutobahnPython {AUTOBAHN_PYTHON_VERSION}
* AutobahnC++ {AUTOBAHN_CPP_VERSION}

## Docker Images

No | Package | Architecture | Image | docker pull
---|---|---|---|---
""".format(BUILD_DATE=BUILD_DATE,
           CROSSBAR_VERSION=CROSSBAR_VERSION,
           AUTOBAHN_JS_VERSION=AUTOBAHN_JS_VERSION,
           AUTOBAHN_PYTHON_VERSION=AUTOBAHN_PYTHON_VERSION,
           AUTOBAHN_CPP_VERSION=AUTOBAHN_CPP_VERSION)

# [![](https://images.microbadger.com/badges/image/crossbario/autobahn-python-aarch64:cpy3-minimal-tx-0.18.2.svg)](https://microbadger.com/images/crossbario/autobahn-python-aarch64:cpy3-minimal-tx-0.18.2 "Get your own image badge on microbadger.com")

i = 1
with open('IMAGES.md', 'w') as f_out:
    with open('images.json') as f_in:
        data = f_in.read()
        obj = json.loads(data)
        f_out.write(HEADER)
        for image in obj.get('images', []):
            package = image.get('package', None)
            architectures = image.get('architectures', None)
            github = image.get('github', None)
            name = image.get('name', None)
            tags = image.get('tags', [])
            for architecture in architectures:
                _tags = ', '.join([tag if tag.strip() != '' else '-' for tag in tags])
                for _tag in tags:
                    arch = '-{}'.format(architecture) if architecture != 'x86_64' else ''
                    image_id = 'crossbario/{package}{arch}:{tag}'.format(package=package, tag=_tag, arch=arch)
                    # autobahn-python-aarch64:cpy3-minimal-tx-0.18.2
                    fqn = 'autobahn-python-aarch64:cpy3-minimal-tx-0.18.2'
                    badge ='[![](https://images.microbadger.com/badges/image/crossbario/{fqn}.svg)](https://microbadger.com/images/crossbario/{fqn} "Metadata")'.format(fqn=fqn)
                    f_out.write('{i} | [{package}]({github}) | {architecture} | {badge} | [`{image_id}`](https://github.com/crossbario/crossbar-docker/blob/master/{package}/{architecture}/Dockerfile.{tag})\n'.format(badge=badge, package=package, architecture=architecture, github=github, name=name, tag=_tag, tags=_tags, image_id=image_id, arch=arch, i=i))
                    i += 1

