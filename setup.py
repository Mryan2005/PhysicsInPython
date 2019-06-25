from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.

setup(name = "Physics in Python",
    version = "0.0.0.1",
    description = "Physics in Python",
    author = "Mr.yan",
    author_email = "a2564011261@163.com",
    url = "https://github.com/Mryan2005/PhysicsInPython",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['Physics_in_Python'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'Physics_in_Python' : '' },
    #'runner' is in the root.
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
)