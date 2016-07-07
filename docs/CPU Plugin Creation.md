CPU Plug-In Creation
====================

In order to assemble and disassemble code for any particular CPU, radish needs a plug-in to be written. The API that you'll need to implement is quite simple, and you have a range of options at your disposable for how you meet those requirements (for example, you could hardcode the opcode table, or you could programmatically generate it, your choice). Once you've provided the plug-in implementation, you'll generally need to provide at least one format handler unless one of the default handlers has what you need. Provide this much, and you'll have a basic assembler / disassembler at your disposal.

Process
-------

1. There is a _plugins_ directory off the project root, and in that directory is the _cpu_ folder. This is where your plug-in should live.

2. Create a python file in that folder named after the CPU you are documenting, for example "6502.py". 

3. Please do not create any additional files in the _cpu_ folder. While doing so won't create a problem per se, it is the convention that the each plug-in gets on file and only those plug-in files are the only thing in each plug-in directory.

4. You may, however, create a package folder in the _cpu_ folder to go with your plug-in file, and in there do whatever you want. The convention is to name it the same as the file name for the CPU plug-in (less the extension).

5. In your primary plug-in file, implement the API as documented below.

Your plug-in will be automatically read on invocations of radish.py. If you have implemented the API as required, your new CPU support will be ready to use. 

API
---

