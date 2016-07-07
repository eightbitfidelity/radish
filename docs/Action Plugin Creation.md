Action Plug-In Creation
=======================

radish's general purpose is to provide code assembly and disassembly functions, but is designed to be extensible to provide a variety of related capabilities. All of these capabilities (or actions) are provided as plug-ins. If you wish for radish to provide some function it does not, then by all means, follow this guide and create your own action plug-in!

Process
-------

1. There is a _plugins_ directory off the project root, and in that directory is the _actions_ folder. This is where your plug-in should live.

2. Create a python file in that folder named appropriately for the action you are documenting, for example "dump-nes-tiles.py". 

3. Please do not create any additional files in the _actions_ folder. While doing so won't create a problem per se, it is the convention that the each plug-in gets on file and only those plug-in files are the only thing in each plug-in directory.

4. You may, however, create a package folder in the _actions_ folder to go with your plug-in file, and in there do whatever you want. The convention is to name it the same as the file name for the action plug-in (less the extension).

5. In your primary plug-in file, implement the API as documented below.

Your plug-in will be automatically read on invocations of radish.py. If you have implemented the API as required, your new action will be ready to use. 

API
---

### Metadata

First and foremost, you must provide some metadata for your action:

<table>
	<thead>
		<tr>
			<th>Variable</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>NAME</td>
			<td>str</td>
			<td>The short name for the action. Spaces discouraged. Used on the
			command line for matching the action and used by other plug-ins to
			identify the action.</td>
		</tr>
		<tr>
			<td>VERSION</td>
			<td>int</td>
			<td>A serial version number for the release of this action. At a
			minimum, increment if some significant or incompatible change
			is made.</td>
		</tr>
		<tr>
			<td>DESCRIPTION</td>
			<td>str</td>
			<td>Use this field to create a meaningful description of the action.
			This can be arbitrarily long</td>
		</tr>
		<tr>
			<td>AUTHOR</td>
			<td>str</td>
			<td>The name, ID, handle, or whatever preferred signature of the
			author of the plug-in. </td>
		</tr>
		<tr>
			<td>CONTACT</td>
			<td>str</td>
			<td>An email address for the author.</td>
		</tr> 
	</tbody>
</table>


An example of this metadata follows:

		NAME = 'assemble'
		VERSION = 5
		DESCRIPTION = """Action to assemble mnemonics into binary
						for the givien architecture"""
		AUTHOR = 'Rob Snyder'
		CONTACT = '<robsnyder14850@gmail.com>'

### Applicability / Context

Not all actions are applicable to all types of data, nor are they necessarily supported on all platforms (using the above example, it would not be expected that the "dump-nes-tiles" plug-in does much for an Atari 2600). You need to indicate what environments you support by providing the following lists:

1. A list of the CPUs that your action supports

2. A list of the data formats that your action supports

3. A list of the platforms that your action supports

You may wild-card any of the above. 

Each of the above is a list, and each list entry is a regex that will be tested to match agains the name

		
