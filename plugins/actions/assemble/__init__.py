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
assemble.py

The 'assemble' plug-in, one of the core plug-ins for radish. Given an assembly source file, a format plug-in that can
read that file, and a CPU plug-in for the architecutre, assembles the file into object code.
"""

# metadata

NAME = 'assemble'
VERSION = 1
DESCRIPTION = 'Assembler action'
AUTHOR = 'Rob Snyder'
CONTACT = '<robsnyder14850@gmail.com>'
