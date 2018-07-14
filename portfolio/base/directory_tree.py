from __future__ import print_function
import os

class Root(object):
# The a root object holds the rest of the
# virtual filesystem.

# The root object contains the top level
# of files and directories. Each directory
# object holds it's level of files and
# directories.

# Root constructor must be passed a directory name!

    dir_name = ""
    directories = []
    files = []

    def __init__(self):
        self.clear()

    def populate(self, folder):
        # Get all top level files and directories
        if(len(self.directories) > 0 or len(self.files) > 0):
            self.clear()

        self.dir_name = folder
            
        for item in os.listdir(self.dir_name):
            if os.path.isdir(os.path.join(self.dir_name, item)):
                # Create a new directory object
                found_dir = Directory(item, self.dir_name)
                self.directories.append(found_dir)
            if os.path.isfile(os.path.join(self.dir_name, item)):
                self.files.append(item)

        # Populate all top level directories
        for directory in self.directories:
            directory.populate(self.dir_name + '/' + str(directory))

    def print_contents(self):
        # Print full virtual filesystem 
        print(self.dir_name, end="")
        if(self.dir_name[-1] == '/'):
            print('')
        else:
            print('/')
        if(len(self.files) > 0):
            for file in self.files:
                print('  - ' + file)
        if(len(self.directories) > 0):      
            for directory in self.directories:
                print('  ' + str(directory) + '/')
                directory.print_contents(2)

    def print_paths(self):
        # Print full virtual filesystem 
        print(self.dir_name, end="")
        if(self.dir_name[-1] == '/'):
            print('')
        else:
            print('/')
        if(len(self.files) > 0):
            for file in self.files:
                print('  ' + str(self.dir_name) + '/' + file)
        if(len(self.directories) > 0):      
            for directory in self.directories:
                print('  ' + str(directory.dir_path) + '/')
                directory.print_paths(2)        

    def clear(self):
        # Clear virtual filesystem
        if(len(self.files) > 0):
            del self.files[:]
        if(len(self.directories) > 0):      
            del self.directories[:]
        self.dir_name = ""

class Directory(Root):
# The directory object is derived from the root
# Each directory contains it's level of files
# and directories.

# Directory levels are created recursively

    dir_path = ""

    def __init__(self, name, path):
        self.dir_name = name
        self.dir_path = path + '/' + self.dir_name
        self.directories = []
        self.files = []

    def populate(self, folder):
        # Get all current level files and directories
        for item in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, item)):
                found_Dir = Directory(item, str(folder))
                self.directories.append(found_Dir)
            if os.path.isfile(os.path.join(folder, item)):
                self.files.append(item)

        # Populate all current level directories recursively
        for directory in self.directories:
            directory.populate(folder + '/' + str(directory))   

    def print_contents(self, level):
        # Print current level contents and recurse deeper
        if(len(self.files) > 0):
            for file in self.files:
                print(level * 2 * ' ' + '- ' + file)
        if(len(self.directories) > 0):
            for directory in self.directories:
                print((level * 2 * ' '), end="")
                print(str(directory) + '/')
                directory.print_contents(level + 1)
                
    def print_paths(self, level):
        # Print current level contents and recurse deeper
        if(len(self.files) > 0):
            for file in self.files:
                print(level * 2 * ' ' + self.dir_path + '/' + file)
        if(len(self.directories) > 0):
            for directory in self.directories:
                print((level * 2 * ' '), end="")
                print(str(directory.dir_path) + '/')
                directory.print_paths(level + 1)
        
    def __repr__(self):
        return str(self.dir_name)
    
    def __str__(self):
        return str(self.dir_name)
