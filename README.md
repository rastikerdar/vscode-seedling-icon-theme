# VSCode Seedling Icon Theme

Small and simple icon theme for VSCode IDE.

![VSCode Seedling Icon Theme](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/preview.png)

Put `"workbench.tree.indent": 14` in your settings for better look.
![VSCode settings tree indent](https://raw.githubusercontent.com/rastikerdar/vscode-seedling-icon-theme/master/images/settings-tree-indent.png)

## Development

This extension uses `Icon Font` method. If you want to add or change icons you need to install `python-fontforge` and simply run `python makefont.py` to convert and integrate all SVGs into a single font file. Each svg name must begin with a `code point` to be identified later.

But to change/add colors or types/names you only need to update `icons.json`.

## Resources

- [Font Awesome](http://fontawesome.com/)
- `icons.json` from [vscode-icons](https://github.com/vscode-icons/vscode-icons)

## License

MIT
