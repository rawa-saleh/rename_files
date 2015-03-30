import string
import os
import os.path
import sys

# Renames a single file
def rename_file(path_name, infile, outfile):
    abs_path = os.path.abspath(path_name)
    abs_infile = os.path.join(abs_path, infile)
    abs_outfile = os.path.join(abs_path, outfile)
    if os.path.exists(abs_infile):
        if os.path.exists(abs_outfile):
            return false
        else:
            os.rename(abs_infile, abs_outfile)
            print "Renaming the file ", abs_infile, " as ", abs_outfile
            return true

# Renames files based on a pattern
# i.e. MDSC123.jpg to Graduation123.jpg
def rename_files(path_name, inpattern, outpattern):
    allfiles = os.listdir(path_name)
    counter = 1
    for infile in allfiles:
        if (string.find(infile, inpattern) >= 0):
            pieces = string.split(infile, ".")
            extension = pieces[len(pieces)-1]
            outfile = "%s%d.%s" %(outpattern, counter, extension)
            success = rename_file(path_name, infile, outfile)
            while success == false:
                counter = counter + 1
                outfile = "%s%d.%s" %(outpattern, counter, extension)
                success = rename_file(path_name, infile, outfile)
            else:
                counter = counter + 1

if __name__ == '__main__':
   # rename_file("."," MDSC1.jpg", "testing.jpg")
    if len(sys.argv) < 3:
        print "The script should be called with input pattern, output pattern, and an optional path."
    # Files are in current directory
    if len(sys.argv) == 3:
        rename_files(".", sys.argv[1], sys.argv[2])
    # Directory passed
    else:
        rename_files(sys.argv[3], sys.argv[1], sys.argv[2])
