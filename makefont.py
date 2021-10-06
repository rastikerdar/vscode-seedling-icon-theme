import os
import fontforge
import psMat;

FONTNAME = 'vscode-adjusted-icons'
DIR = './icons'

if __name__ == '__main__':

    font = fontforge.font()
    font.fontname = FONTNAME
    font.familyname = FONTNAME
    font.copyright = 'Symbols are imported from FontAwesome SVGs'
    font.fullname = FONTNAME

    try:
        for svg_file in os.listdir(DIR):
            if svg_file.find('.svg') == -1:  # is not a svg file
                continue
            g = font.createChar(int(svg_file.split('-')[0], base=16))
            print(svg_file)
            g.importOutlines(
                os.path.join(DIR, svg_file), ('removeoverlap', 'correctdir'))
            g.removeOverlap()
            move_mat = psMat.translate( -100,0 )
            g.transform(move_mat)
            scale_mat = psMat.scale(1.1)
            g.transform(scale_mat)
    except ValueError:
        print('"%s" is not a valid file name.' % svg_file)
        print('File name should be in format "hexnumber-name.svg". e.g. "ff5a-search.svg"')

    except Exception as e:
        raise e

    font.generate('%s.ttf' % FONTNAME)
