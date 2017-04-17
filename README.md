# hackboy
Hack-Boy 9001 is a cryptanalytic toolkit for RobCo TERMLINK systems. Also known as Hacking in Fallout 3, New Vegas, and 4.

Developed by NeCo Corporation, provided to you under the C.I.T. License. (4thwall: MIT License)

## Requirements
* A terminal or PC (Hack-Boy 9001 is not yet available in holotape format.)
* Python 2.7
* Your Target: a RobCo TERMLINK memory hack session

## Basic Operation
Hack-Boy 9001 is meant to be used in 3 modes:
* Terminal Mode (also known as Interactive Mode) is a mode that runs interactively with the user. You can use a built-in command prompt to work with password candidacy.
* Command-Line Interface (CLI Mode) is a mode that does not run interactively, but accepts a list of words and guesses then produces a (hopefully) shorter list of candidates that might be used as entry point into the machine.
* Application-Programming Interface (API Mode) is a mode that can be called by other programs. Useful if you are going to link other programs to Hack-Boy 9001.

Currently, CLI and API mode are not implemented. We have no schedule for Graphical-User Interface (GUI) mode, either web-based, mobile, or on your native OS.

## Interactive Mode Commands

* new (or n): Start a new hacking session, clears all existing candidate word list from memory.
* add WORD WORD2 ... (or a): Add one or more words to the candidate word list. You usually copy a list of words from the RobCo machine.
* best WORD (or b): Automatically find the best word. Best word means the word that will, at worst, give as few candidates remaining as possible. In case of a tie, one will be chosen.
* try WORD SIMILARITY (or t): Record a hack attempt. Similarity is the number of matching characters provided by the RobCo machine.
* dud WORD WORD2 ... (or d): Delete one or more words from the candidate word list. You probably don't need this, but I'm providing this functionality just in case.
* sim WORD WORD2 (or s): Test similarity between two and only two words.
* list (or l or ls): Print the candidate word list. Note that the list is always printed after every successful command that concerns the word list.
* quit (or q): Exit program

Note that all words are automatically converted to UPPERCASE, as with RobCo TERMLINK standard. The commands must be lower-case.

## Example Usage
($ denotes your OS shell. > denotes Hack-Boy 9001 shell.)

You are provided with the following word list from RobCo Terminal:
```
COMPANY TRAPANS QUAMASH CULMING ETAMINE OUTMANS PLAYACT CLEWING COURANT ABEYANT CHAMOIX ALIMENT
```

You should start Hack-Boy 9001 using:
```
$ python hackboy.py
```
  
Then use the add (or a) command to add the words:
```
> add COMPANY TRAPANS QUAMASH CULMING ETAMINE OUTMANS PLAYACT CLEWING COURANT ABEYANT CHAMOIX ALIMENT
```

Then, pick a guess at RobCo terminal. For example CLEWING was picked and the terminal said I got 2/7 correct, you should type the following into Hack-Boy 9001:
```
> t clewing 2
```

You will get a shorter list of words:
```
COMPANY ETAMINE COURANT ABEYANT ALIMENT
5 words in list
```

These words are the only ones that could be the entry point into the RobCo machine. Let's try ETAMINE next. 1/7 correct.
```
> t etamine 1
COMPANY COURANT ABEYANT
3 words in list
```

COURANT gives 3 correct.
```
> t courant 3
ABEYANT
1 words in list
```

Now we have the only one possible word left. Choose it in RobCo terminal to gain access.

## Notes
Entry into the system is not guaranteed. RobCo terminals have additional weaknesses in the parentheses such as ( ), [ ], and { }.

If you can find a matching pair between the parentheses or braces on the same memory line, you can access the opening brace to
match them and either have one dud removed from the RobCo terminal (an action you can reflect in Hack-Boy using the d command) or
additional try quota can be given.

## Shout-outs

* If you do not have a RobCo terminal at hand, you can practice using an emulator at http://mitchellthompson.net/demos/terminal/
* I took KeyboardInterrupt handling from [SO::8813291](http://stackoverflow.com/questions/8813291/better-handling-of-keyboardinterrupt-in-cmd-cmd-command-line-interpreter)
* Bethesda Softworks, Bethesda Game Studios, Obsidian Entertainment for Fallout 3, NV, and 4 that featured RobCo terminals in their current form
* Interplay and Black Isle Studios for the inception, development, and publishing of early Fallout games
* I was personally inspired by [that lazy Russian guy](https://github.com/NARKOZ/hacker-scripts) who used a machine to send an excuse to his wife, lie to his boss, auto-rollback a client's database, and makes coffee remotely, done right when he makes it to the coffee machine.
