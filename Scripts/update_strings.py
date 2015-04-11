# -*- coding: utf-8 -*-
import os, sys
import argparse
import re
from collections import OrderedDict

parser = argparse.ArgumentParser(description='Update strings File for iOS & Mac OS X Projects based on genstrings. Supports Swift and Objective-C files.')
parser.add_argument('localizable_file', metavar='Localizable.strings', help='Path to the project Localizable.strings file')
parser.add_argument('-e', '--encoding', help='Encoding of the Localizable.strings file (Optional, default: \'utf16\')', required=False, default='utf16')
parser.add_argument('-s', '--source', help='Path to Source files (Optional, default: \'.\')', required=False, default='.')
parser.add_argument('-p', '--project', help='Project Name (Optional)', required=False, default='DefaultProject')
args = parser.parse_args()

LOCALIZABLE_FILE_ENCODING = args.encoding
LOCALIZABLE_FILE = args.localizable_file
SOURCE_PATH = args.source
PROJECT_NAME = args.project

PATTERN_LOCALIZED_ENTRY = re.compile('(/\*[^\*][^/]*\*/)[^"]*"([^"]*)"[ ]*=[ ]*"([^"]*)"[ ]*;')

temp_dir = '/tmp/%s' % PROJECT_NAME
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

genstrings_command = 'find %s -name "*.swift" -o -name "*.m" -o -name "*.mm" | xargs genstrings -o %s' \
                     % (SOURCE_PATH, temp_dir)
os.system(genstrings_command)
temp_localized_strings = os.path.join(temp_dir, "Localizable.strings")



class LocalizableEntry(object):
    def __init__(self,value, comment=None):
        self.value = value
        self.comment = comment

    def str_with_key(self, key):
        comment = "%s\n" % self.comment if self.comment is not None else ""
        return '%s"%s"="%s";\n\n' % (comment, key, self.value)


localized_entries = OrderedDict()
def parse_localized_strings_file(path, initial=False):
    file_content = open(path, "r").read().decode(LOCALIZABLE_FILE_ENCODING)
    results = PATTERN_LOCALIZED_ENTRY.findall(file_content)
    for r in results:
        #only update, ignore unused
        if r[1] in localized_entries:
            localized_entries[r[1]].value = r[2]
        elif initial == True:
            localized_entries[r[1]] = LocalizableEntry(r[2], r[0])

parse_localized_strings_file(temp_localized_strings, True)
parse_localized_strings_file(LOCALIZABLE_FILE)

#write to file
output_file = open(LOCALIZABLE_FILE, "w")
for key, localized_entry in localized_entries.items():
    output_file.write(localized_entry.str_with_key(key).encode(LOCALIZABLE_FILE_ENCODING))
