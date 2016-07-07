import pathlib
import logging
import sys
import importlib

"""
Copyright 2016 Robert L Snyder <robsnyder14850@gmail.com>, 258 Duboise Road, Ithaca, NY 14850

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS"
BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions and limitations under the License.
"""

def _check_metadata(plugin):

    metadata = [getattr(plugin, name, None) for name in  ['NAME', 'VERSION', 'DESCRIPTION', 'AUTHOR', 'CONTACT']]
    if None in metadata:
        logging.error('Metadata incomplete')
        sys.exit(1)


def load_plugins(plugin_directory):

    plugins = {}
    path = pathlib.Path(plugin_directory)
    if not path.exists():
        logging.fatal('The specified plug-in path does not exist: %s', plugin_directory)
        sys.exit(1)

    for plugin_package in [sub_directory for sub_directory in path.iterdir() if sub_directory.is_dir()]:
        logging.debug('Checking potential plugin file: %s', plugin_package)
        try:
            new_module = importlib.import_module(str(plugin_package.as_posix()).replace('/', '.'))
        except Exception as ex:
            logging.fatal('The module had errors and could not be imported: %s', plugin_package)
            logging.fatal(ex)
            sys.exit(1)
        _check_metadata(new_module)
        logging.info('Sucessfully imported %s', plugin_package)
        plugins[plugin_package.name] = new_module

    return plugins
