import sys

def convert(s):
    try:
        return int(s)        
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1
