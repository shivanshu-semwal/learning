# TeX / LaTeX

[TeX](https://en.wikipedia.org/wiki/TeX) is a typesetting engine developed by Donald Knuth.
[LaTeX](https://en.wikipedia.org/wiki/LaTeX) is a set of macros for TeX created by Leslie Lamport. Its purpose is to simplify TeX typesetting, especially for documents containing mathematical formulae.

## Resources

* [WikiBook on LaTeX](https://en.wikibooks.org/wiki/LaTeX/Introduction)
* [Github repo of examples](https://github.com/MartinThoma/LaTeX-examples)

## Compiling

- compile `pdflatex file.tex`

## Functions in vim

- `\maketitle` - function without parameter
- `documentclass{article}` - function with parameters
- `{\LaTeX}` - good idea to keep functions within curly brackets to limit scope of the function 

## Start Document

- every document starts with a `\documentclass{}`
- `\documentclass{atricle}` - other choices, book, handout, beamer

```
\begin{document}
actual stuff
\end{document}
```

## Title For Document

- `\author{name}` - name of the author you want to use
- `\title{title}` - title you want to use
- `\date{date}` - date you want to use

- `\maketitle` - now use this function a the place where you want the title

## Sections

- `\section{Introduction}` - starting a new section

## Text Styles

- `\textbf{bold text}`
- `\textit{italics text}`
- `\emph{emhatic text}`
- `\underline{underline in the text}`

## Quotation marks in LaTeX

- `` - start quote
- '' - end quote

OR

- ` - start quote
- ' - end quote

## Lists

- `\begin{enumerate}` - for munbered list
- `\item` - make a new item
- `\end{enumerate}`

- `\begin{itemize}` - begin unordered list
- `\item` - add new items
- `\end{itemize}`

## Label and refrences

-  `\label{list1}` - label a section, list item, figure, table (basically everything which is numbered by default) `list1`
-  `\ref{list1}` - get the number of the label `list1`

## Bibliography

- First you need a index files for refrences, `file.bib`

```tex
<!-- test is the tag for the refrence -->
@book{test,
    author = "Shivanshu",
    title = "My book",
    year = "2021",
    publisher = "McGrawHill"
    }
```

- import package
  - To use this we use `biber` package(there aore other too), `\usepackage[backend=biber]{biblatex}`
- add the index file
  - `addbibresource{file.bib}`
- print bibliography
  - `\printbibliography`
- to add some refrences in the file
  - `\textcite{text}` - show the refrence
- add the refrences to text file
  - `biber file.tex`
- and now compile
  
## Center Environment

- `\begin{center}`
- `\end{center}`
  
## Images and figures

- `\usepackage{grphicx}`
- to insert image - `\includegraphics{imagename}`
- resize image - `\includegraphics[width=2in, height=4in]{imagename}` - maintains aspect ratio if any one dimention is missing
- `\includeimage[width=0.7\textwidth]{imagename}` 

- figures - `\begin{figure}` ... `end{figure}`
- extra parameters - `h` where it is in text, `t` - top of page, `b` - bottom of page, `p` - on new page
- figure can contain
  - `\caption{this is caption}`
  - `\centering`

- wrapping figure, `\usepackage{wrapfig}`
- `\begin{wrapfigure}{r}{3in}` ... `\end{wrapfigure}` - `{r}` - is right orientation, `{3in}` is the size of wrapping

## Beamer Presentation

- `\documentclass{beamer}`
- divided into frames, which have slides
- to add frames, `\begin{frame}` ... `\end{frame}`
- `\frametitle{give title}`
- `\usetheme{themename}` - Frankfurt ..
- `\pause` - adds new slide
- `\section{ection name}` - add section links

## Columns

- `\column{.5\textwidth}` - add a column half the width of text size


# Tips

## set page geometry

- `\usepackage[a4paper,margin=2cm]{geometry}`

## `listings`

- for code blocks
- use `\lstinline{}` for incline code blocks
- use `\begin{lstlisting}...\end{lstlisting}` for code blocks

```latex
\lstset{
  backgroundcolor=\color{white},   % choose the background color; you must add \usepackage{color} or \usepackage{xcolor}; should come as last argument
  basicstyle=\ttfamily,        % the size of the fonts that are used for the code
  breakatwhitespace=false,         % sets if automatic breaks should only happen at whitespace
  breaklines=true,                 % sets automatic line breaking
  % captionpos=b,                    % sets the caption-position to bottom
  commentstyle=\color{darkgray},    % comment style
  %firstnumber=1000,                % start line enumeration with line 1000
  %frame=single,	                   % adds a frame around the code
  keepspaces=true,                 % keeps spaces in text, useful for keeping indentation of code (possibly needs columns=flexible)
  keywordstyle=\bfseries\color{black},       % keyword style
  morekeywords={*,...},            % if you want to add more keywords to the set
  %numbers=left,                    % where to put the line-numbers; possible values are (none, left, right)
  %numbersep=5pt,                   % how far the line-numbers are from the code
  %numberstyle=\tiny\color{mygray}, % the style that is used for the line-numbers
  %rulecolor=\color{black},         % if not set, the frame-color may be changed on line-breaks within not-black text (e.g. comments (green here))
  showspaces=false,                % show spaces everywhere adding particular underscores; it overrides 'showstringspaces'
  showstringspaces=false,          % underline spaces within strings only
  showtabs=false,                  % show tabs within strings adding particular underscores
  %stepnumber=2,                    % the step between two line-numbers. If it's 1, each line will be numbered
  stringstyle=\color{blue},     % string literal style
  tabsize=4,	                   % sets default tabsize to 2 spaces
}
```

## `courier`

- for courier font

## `hyperref`

```latex
\usepackage[colorlinks = true,
            linkcolor = blue,
            urlcolor  = blue,
            citecolor = blue,
            anchorcolor = blue]{hyperref}
```

## `multicol`

```latex
\begin{multicols}{2}
Column 1
\columnbreak
Column 2
\end{multicols}
```

- If you omit the `\columnbreak`, the columns will balance automatically.

### Noob tips

#### Latex command structure

```
\commandname[option1,option2,...]{argument1}{argument2}...
```

#### Using packages

```
\usepackage[option1,option2,option3]{''package_name''}
```

#### Reserved Characters

* Don't use reserved characters in text. Usually when you copy-paste something form another file, it may contain some reserved text, remove those, or you will get errors.

```
# $ % ^ & _ { } ~ \
```

replace these with

```
\# \$ \% \^{} \& \_ \{ \} \~{} \textbackslash{}
```

#### How to code syntax-highliting?

* Use package - `\usepackage{listings}` and `\usepackage{color}`
* Define some colors -
```tex
\definecolor{mygreen}{rgb}{0,0.6,0}
\definecolor{mygray}{rgb}{0.5,0.5,0.5}
\definecolor{mymauve}{rgb}{0.58,0,0.82}
```
* And some configuration for the package - 
```tex
\lstset{ 
	backgroundcolor=\color{white},   % choose the background color; 
    %you must add \usepackage{color} or \usepackage{xcolor}; should come as last argument
	
    basicstyle=\footnotesize,        % the size of the fonts that are used for the code
	breakatwhitespace=false,         % sets if automatic breaks should only happen at whitespace
	breaklines=true,                 % sets automatic line breaking
	captionpos=b,                    % sets the caption-position to bottom
	commentstyle=\color{mygreen},    % comment style
	deletekeywords={...},            % if you want to delete keywords from the given language
	escapeinside={\%*}{*)},          % if you want to add LaTeX within your code
	extendedchars=false,             % lets you use non-ASCII characters; for 8-bits encodings only, does not work with UTF-8
	firstnumber=1,                % start line enumeration with line 1000
	frame=tb,	                  % adds a frame around the code
	keepspaces=true,              % keeps spaces in text, useful for keeping indentation of code (possibly needs columns=flexible)
	keywordstyle=\color{blue},       % keyword style
	%language=C++,                   % the language of the code
	morekeywords={*,...},            % if you want to add more keywords to the set
	numbers=left,                    % where to put the line-numbers; possible values are (none, left, right)
	numbersep=5pt,                   % how far the line-numbers are from the code
	numberstyle=\tiny\color{mygray}, % the style that is used for the line-numbers
	rulecolor=\color{black},         % if not set, the frame-color may be changed on line-breaks within not-black text (e.g. comments (green here))
	showspaces=false,                % show spaces everywhere adding particular underscores; it overrides 'showstringspaces'
	showstringspaces=false,          % underline spaces within strings only
	showtabs=false,                  % show tabs within strings adding particular underscores
	stepnumber=1,                    % the step between two line-numbers. If it's 1, each line will be numbered
	stringstyle=\color{mymauve},     % string literal style
	tabsize=2,	                     % sets default tabsize to 2 spaces
	%title=\lstname                  % show the filename of files included with \lstinputlisting; also try caption instead of title
}
```
* To highlight in doc - 
```
\begin{lstlisting} 
Put your code here. 
\end{lstlisting}
```

* To highlight a file 

```
\lstinputlisting[language=C++]{first.cpp}
```

#### I want some space at start of document

Use this `\vspace*{50mm}`
