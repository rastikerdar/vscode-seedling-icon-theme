# VSCode Seedling Icon Theme

Simple icon theme for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=rastikerdar.vscode-seedling-icon-theme).

![VSCode Seedling Icon Theme](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/preview-folder.gif)

![VSCode Seedling Icon Theme](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/preview.png)

Put `"workbench.tree.indent": 14` in your settings for better look.

![VSCode settings tree indent](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/settings-tree-indent.png)

## Development

This extension uses `Icon Font` method. If you want to add or change icons you need to install `python-fontforge` and simply run `python makefont.py` to convert and integrate all SVGs into a single font file. Each svg name must begin with a `code point` to be identified later.

But to change/add colors or types/names you only need to update `icons.json` or `icons-plus.json`.

## Resources

- [Font Awesome](http://fontawesome.com/)
- `icons.json` from [vscode-icons](https://github.com/vscode-icons/vscode-icons)

## Todo

- Write a python script for generating `images/preview.png`

## License

MIT
