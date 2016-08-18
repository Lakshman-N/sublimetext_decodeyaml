import sublime
import sublime_plugin
from os.path import basename, splitext


class BaseCommand(sublime_plugin.TextCommand):

    def __init__(self, view):
        self.view = view
        self.language = self.get_language()

    def get_language(self):
        syntax = self.view.settings().get('syntax')
        language = splitext(basename(syntax))[0].lower() if syntax is not None else "plain text"
        return language

    def check_enabled(self, lang):
        return True

    def is_enabled(self):
        """
        Enables or disables the 'decode_yaml' command. Command will be disabled if
        there are currently no text selections and current file is not 'Plain Text'. This helps clarify to the user about when the command can
        be executed, especially useful for UI controls.
        """
        if self.view is None:
            return False

        return self.check_enabled(self.get_language())

    def run(self, edit):
        """
        Main plugin logic for the 'decode_yaml' command.
        """
        view = self.view
        regions = view.sel()
        # if there are more than 1 region or region one and it's not empty
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    s = view.substr(region).strip()
                    s = self.decode(s)
                    view.replace(edit, region, s)
        else:  # format all text
            alltextreg = sublime.Region(0, view.size())
            s = view.substr(alltextreg).strip()
            s = self.decode(s)
            view.replace(edit, alltextreg, s)
        view.set_syntax_file('Packages/YAML/YAML.tmLanguage')

    def decode(s):
    	return s # Dummy parent class method

class DecodeYamlCommand(BaseCommand):
    def check_enabled(self, language):
        return (language == "plain text") or (language == "yaml")

    def indentLine(self):
        self.output += '  ' * self.treedepth

    def parseArray(self, cardinal):
        if self.STATE == 'VALUE':	# This will be true for all arrays except the root array
            if (cardinal == 0):
                self.output += ' {  }\n'
            else:
                self.output += '\n'

        self.treedepth += 1;		# Increase the depth by 1 for new array
        i = 0;
        self.p += 1					# Moving by '{'
        while (i < cardinal):
            self.indentLine()		# Every new array item is indented appropriately
            self.STATE='KEY'
            self.parse()			# parse key

            self.STATE='VALUE'
            self.parse()			# parse value
            i += 1					# Move onto next array item
        self.p += 1					# Moving by '}'
        self.treedepth -= 1
        return

    def parseString(self, cardinal):
        self.p += 1             # Moving by '"'
        string = self.input[self.p:self.p+cardinal]
        self.p += cardinal		# Moving by actual string

        if (self.STATE == 'KEY'):
            self.output += string + ':'
        else:
            self.output += ' ' + string + '\n'

        self.p += 2             # Moving by '";'
        return

    def parseInt(self, cardinal):
        if (self.STATE == 'KEY'):
            self.output += '-'
        else:
            self.output += ' ' + str(cardinal) + '\n'

    def parseBool(self, cardinal):
        if (cardinal == 0):
            self.output += ' false\n'
        else:
            self.output += ' true\n'

    def parse(self):
        objType = self.input[self.p]
        self.p += 2						# Moving by 'a:|b:|s:|i:'
        cardinal = ''
        while self.input[self.p] != ':' and self.input[self.p] != ';':
            cardinal += self.input[self.p]
            self.p += 1
        self.p += 1 					# Moving by ':|;'
        if objType == 'a':
            self.parseArray(int(cardinal))
        elif objType == 'i':
            self.parseInt(int(cardinal))
        elif objType == 's':
            self.parseString(int(cardinal))
        elif objType == 'b':
            self.parseBool(int(cardinal))
        return

    def decode(self, s):
        self.input = s.replace(' ', '').replace('\n', '') # Remove white_spaces
        self.output = ''		# YML output
        self.treedepth = -1		# To properly indent nested arrays
        self.STATE = ''			# KEY | VALUE - says what part of array is being parsed
        self.p = 0  			# Pointer to current character
        self.parse()
        return self.output
