import fontforge
import json
import sys


def main(name):
    f = fontforge.open('%s.ttf' % name)
    result = {}
    for i in f.selection.all():
        try:
            if f[i].glyphname != '.notdef':
                result[f[i].glyphname] = f[i].unicode
        except:
            pass
    
    with open("%s.map" % name, "w") as fp:
        fp.write(json.dumps(result, indent=2))

if __name__ == '__main__':
    main(sys.argv[1].split('.', -1)[0])
    
