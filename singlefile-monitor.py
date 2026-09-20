# just importing the hashes library and the path library
# hashlib has the functions inside already
# pathlib deals w different os path systems
import hashlib
import pathlib

# starting to define function for creating the hash
# hashit is the name of the function
# pathtype should be pathlib.Path
# output should be a string
def hashit(filepath: pathlib.Path) -> str:
    # varname is create hash
    # use sha256 function from hashlib
    createhash = hashlib.sha256()
    # (r)eading from filepath in (b)inary
    # file213 is temp file name while func is running
    # with closes file auto when func ends or js autocloses when error
    with open(filepath, "rb") as file213:
        # for every part in xyz
        # repeat action x until hit y
        # lambdas just a nameless function (which will be repeated here) like aws' lambda is serverless
        # file213.read is the nameless function thats being repeated by the iter
        # 65636 is js the number of bytes being taken from filepath, basically 64kb
        # stop doing this function when you hit b"" which js means an empty 
        for part in iter(lambda: file213.read(65536), b""):
            # put the thing from line above into createhash and generate a sha256 for it
            # update thing just replaces the thing being run every time
            createhash.update(part)

    # at the end of the function it should return a hash
    # the hex part of hexdigest puts output into hexadecimal form
    # the digest part of hexdigest is just outputting
    # js digest() would give something random in binary bytes
    return createhash.hexdigest()
