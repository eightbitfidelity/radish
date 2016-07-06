import argparse
from pathlib import Path
import sys
import logging

"""
Copyright 2016 Robert L Snyder <robsnyder14850@gmail.com>, 258 Duboise Road, Ithaca, NY 14850

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS"
BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language
governing permissions and limitations under the License.
"""

"""
radish.py

radish is a assembler / disassembler for retro computers and retro consoles, with additional tools to facilitate understanding
and creating new software for retro platforms. For more complete information, please see the README.md file.

Invoke:

    python radish.py --help

for some basic help to get started.
"""

def initialize_logging(log_level):
    logging.basicConfig(level={'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR,
        'critical': logging.CRITICAL}[log_level])



def check_and_open_file(file_name, action):

    in_file = Path(file_name)
    if not in_file.exists():
        logging.fatal('The specified infile does not exist.')
        sys.exit(1)

def main():

    print('radish - a retro assembler / disassembler / code exploration tool')
    print('Copyright (C) 2016 Robert L Snyder <robsnyder14850@gmail.com>, licensed under the Apache 2.0 license.')
    print(' ')

    parser = argparse.ArgumentParser(prog='radish')

    parser.add_argument('infile', help='the input file to process')
    parser.add_argument('-a', '--action', help='the action to take (assemble | disassemble)',
        choices=['assemble', 'disassemble'], required=True, dest='action')
    parser.add_argument('-ll', '--log_level', help='desired logging level', default='error',
        choices=['debug', 'info', 'warning', 'error', 'critical'], dest='loglevel')

    args = parser.parse_args()
    initialize_logging(args.loglevel)
    check_and_open_file(args.infile, args.action)


if __name__ == '__main__':
    main()
