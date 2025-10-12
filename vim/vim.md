# Vim Cheatsheet

## Movement/ Range

### Character

- `i` left
- `j` down
- `k` top
- `l` right

### word, WORD

- `printf("hello world");`
    - `words` are [`printf`, `"(`, `hello`, `world`, `")`]
    - `WORDS` are [`printf("hello`, `world");`]

- `w` `b` next/prev word
- `W` `B` next/prev WORD
- `e` `E` end of word/WORD

### line

- `$` end of line
- `0` beginning of line
- `^` beggining of a first non blank character of line

### paragraph, block

- a pragraph begins with a new line `\n`
- a block begins with a new `{` and ends with `}`

- `{` `}` prev/next praragraph
- `[{` `}]` prev/next block
- `%` matching parenthesis

### window, file

- `H` top of windows
- `M` middle of windows
- `L` bottom of window

- `zt` scroll to top
- `zz` scroll to middle
- `zb` scroll to bottom

- `Ctrl B` `Ctrl F` pre/next page
- `gg` `G` begin/end of file

- `mx` `'x` - mark `x`, jump to `x`

### search

- `*` `#` find current word forward/backword
- `fx` find character `x` to right
- `gd` go to definition of word
- `/xxx` search `xxx`
- `n` `N` next/prev result

## Mode Commands

- `Esc` `Ctrl [` enter normal mode
- `v` enter visual mode
- `V` enter visual line mode
- `Ctrl v` enter visual block mode
- `i` insert mode
- `R` replace mode
- `a` append
- `A` append at the end of line

## General Commands

- `y` yank/copy range
- `d` delete/cut range
- `c` change range
- `x` delete/cut character
- `D` delete to end of line
- `C` modify to the end of line
- `p` paste after the cursor
- `J` join lines
- `r` replace character
- `>` indent
- `<` indent leftward
- `.` redo
- `u` undo

## ex commands

- `:w` write
- `:q` quit
- `:e x` edit file x
- `:n` new window
- `:h` vim help
- `:xx` jump to line `xx`

## Auto Complete (insert mode)

- `Ctrl N` `Ctrl P` auto complete next/prev keyword
- `Ctrl X Ctrl F` auto complete file name

## Split window

- `:vsp` vertical split
- `:sp` horizontal split
- `:diffs` split and diff
- `Ctrl W p` to last accessed windows
- `Ctrl W w` to next window
