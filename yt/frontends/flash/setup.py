#!/usr/bin/env python
import setuptools
import os
import sys
import os.path


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('flash', parent_package, top_path)
    config.add_extension("_flash_particle_reader",
                         ["yt/frontends/flash/_flash_particle_reader.pyx"],
                         language="c"
                         )
    config.make_config_py()  # installs __config__.py
    #config.make_svn_version_py()
    return config
