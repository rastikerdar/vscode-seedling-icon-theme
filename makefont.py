import fontforge
import os

FONTNAME = 'vscode-adjusted-icons'
DIR = './icons'

if __name__ == '__main__':

    font = fontforge.font()
    font.fontname = FONTNAME
    font.familyname = FONTNAME
    font.copyright = 'Symbols are imported from FontAwesome SVGs'
    font.fullname = FONTNAME

    for svg_file in os.listdir(DIR):
        if svg_file.find('.svg') == -1:  # is nor a svg file
            continue
        g = font.createChar(int(svg_file.split('-')[0], base=16))
        g.importOutlines(
            os.path.join(DIR, svg_file), ('removeoverlap', 'correctdir'))
        g.removeOverlap()

    font.generate('%s.ttf' % FONTNAME)
