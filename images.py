# [autobahn-js](https://github.com/crossbario/autobahn-js) | amd64 |

#  | [![](https://images.microbadger.com/badges/image/crossbario/

# [![](https://images.microbadger.com/badges/version/crossbario/autobahn-js:full.svg)](https://github.com/crossbario/crossbar-docker/blob/master/autobahn-js/x86_64/Dockerfile.full)

def badger_url(package, flavor):
    return '[![](https://images.microbadger.com/badges/version/crossbario/autobahn-js:full.svg)](https://github.com/crossbario/crossbar-docker/blob/master/autobahn-js/x86_64/Dockerfile.full)'

import json
from pprint import pprint

HEADER = """
# Images

Package | Architecture | Flavor                             | Image                               | `docker pull   `
---|---|---|---|---
"""

with open('IMAGES.md', 'w') as f_out:
    with open('images.json') as f_in:
        data = f_in.read()
        obj = json.loads(data)
        f_out.write(HEADER)
        for image in obj.get('images', []):
            package = image.get('package', None)
            architecture = image.get('architecture', None)
            github = image.get('github', None)
            name = image.get('name', None)
            tags = image.get('tags', [])
            _tags = ', '.join([tag if tag.strip() != '' else '-' for tag in tags])
            _tag = tags[0]
            for _tag in tags:
                image_id = 'crossbario/{package}{arch}:{tag}'.format(package=package, tag=_tag, arch='-{}'.format(architecture) if architecture else '')
                f_out.write('[{package}]({github}) | {architecture} | [![](https://images.microbadger.com/badges/version/crossbario/{package}:{tag}.svg)](https://github.com/crossbario/crossbar-docker/blob/master/{package}/{architecture}/Dockerfile.{tag}) | [![](https://images.microbadger.com/badges/image/crossbario/{package}:{tag}.svg)](https://hub.docker.com/r/crossbario/{package}/) | `{image_id}`\n'.format(package=package, architecture=architecture, github=github, name=name, tag=_tag, tags=_tags, image_id=image_id))
