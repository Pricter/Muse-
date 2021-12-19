# Muse
A python based interpreter for making music

## based on:
This amazing [article](https://towardsdatascience.com/mathematics-of-music-in-python-b7d838c84f72) by Nishu Jain

## Syntax:
The songs are generated from .muse files<br>
each .muse file should contain a:
- `start <name>` where `name` will be the generated filename
- `song <music notes>` where `music notes` is the piano "notes" seperated by a -
- `end` for ending the program

## Music notes:
- C is the base note
- the black bar on a piano are written as 'a' if the white bar to it's left is 'A'

## Supported notes:
- C, D, E, F, G, A, B -> white bars
- c, d, e, f, g, a, b ->black bars

## How to run?
- `python muse.py <filename>.muse` will generate a .wav file which can then be played in any supported audio player
