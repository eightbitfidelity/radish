radish
======

**Assembler / Disassembler Designed for Retro-Computing and Retro-Gaming**
**In Development**

Introduction
------------

There exist many tools, across many platforms, for creating and exploring code from older computers and game systems, but there is a significant lack of consistency and general availability. I noticed this first when trying to teach my son how to modify Atari 2600 ROMs the other day; there's a perfectly workable compiler we found (_dasm_ if you're interested) but the most recently compiled version we  could locate online was over a decade old and the executable just would not run on a "modern" version of Windows. A half-hour later we had patched the old source and recompiled. But...

This seems to be more and more prevalent. I know what I'd like to personally have is a unified set of tools for disassembling, exploring, and re-assembling code across multiple retro architectures, with additional tools to dissect and build the proper ROM or load-file formats, virtual disk formats, etc., as well as interrogate and create common data structures (e.g. tile maps for older consoles). A set of tools that works not only today but is somewhat future-proof (as much as any technology could be). 

My goals for this project, therefore:

* Be easily extensible, through plug-ins, so that new architectures and machines can be added to a consistent framework
* Be portable without re-compiling or relying on esoteric dependencies; use of a widely available interpreted language is suggested.
* I don't much care to be compatible with existing assembler syntaxes (e.g. AT&T vs. Intel), because I want consistency across the architectures supported more than I desire compatibility with existing source. However, whatever radish disassembles, it must be able to assemble again, and the syntax must materially be the same as an accepted existing format.


Installation
------------

### Requirements

radish is written in Python. Python 3.5, or a newer Python 3.x branch, is recommended; earlier versions of Python 3 will probably be fine as well. Python 2 is not supported. You will need to install some additional libraries; _pip_ is strongly recommended. Although not required, _virtualenv_ is recommended as well.

### Installation

The official version of this source is available on GitHub:

    https://github.com/eightbitfidelity/radish

The _main_ branch will always contain the latest 'stable' release and is what you should check out. All prior stable releases are tagged (see "Release History" below). There is a _development_ branch which is where new development is occurring, and _fix_XXX_ branches for specific fixes being applied to release live.

1. Clone from GitHub into the directory of your choice.

		git clone https://github.com/eightbitfidelity/radish.git

2. Change into the newly created __radish__ directory.

3. You will need to install all of dependencies in the _requirements.txt_ file. It is recommended you create a virtualenv for this, activate that virtualenv, then invoke 

		pip install -r requirements.txt 
		
	but if you manage your environment differently, do whatever it is you do to get those requirements installed.

### Usage

You can invoke radish simply by typing:

    python radish.py --help

at which point radish will give you high level help on how to use it. Details for specific activities follow.


Additional Documentation
------------------------

There is a /docs directory in the distribution that contains additional documentation for specific items, such as information around supported architectures and guidance as to how to create plug-ins.

You may find my personal retro-technology blog, **Add, With Carry** interesting. 

		https://adc.eightbitfidelity.com
		

This is the site where I chronicle my explorations and adventures with retro computers and old consoles, etc., and have links there to other resources of general interest to the retro-technician or enthusiast.


Supported Platforms and Architectures
-------------------------------------

None, yet.

Release History
---------------

There have been no releases of this code yet. Development on the initial alpha release is still underway.



License
-------

Copyright 2016 Robert L Snyder <robsnyder14850@gmail.com>, Ithaca, NY

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
