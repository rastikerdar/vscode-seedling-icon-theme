# VSCode Seedling Icon Theme

Small and simple icon theme for VSCode IDE.

![VSCode Seedling Icon Theme](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/preview.png)

## Development

All `SVGs` are adjusted (resized and moved) to be used in [Visual Studio Code](http://code.visualstudio.com/). This extension uses the `Icon Font` method. If you want to add or change icons you need to install `python-fontforge` and simply run `python makefont.py` to convert and integrate all SVGs into a single font file. Each svg name must begin with a `code point` to be specified in the font. Please see the `FontAwesome` cheatsheet.

But to change/add colors or types/names you only need to update `icons.json`.

## Resources

- SVGs from [Font Awesome](http://fontawesome.com/)
- `icons.json` from [vscode-icons](https://github.com/vscode-icons/vscode-icons)

## License

MIT