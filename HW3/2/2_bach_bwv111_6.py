#!/usr/bin/env python
# coding: utf-8

# import

from music21 import *

## 2. About Bach's chorale 'bach/bwv111.6'
## A. Add the new chord part to the original song

sBach = corpus.parse('bach/bwv111.6')

sBachNew = sBach.chordify()
sBach.insert(0, sBachNew)

for c in sBachNew.recurse().getElementsByClass('Chord'):
    c.closedPosition(forceOctave=4, inPlace=True)
    while len(c) != 1:
        for a in c:
            c.remove(a) ## Remove notes until

sBach.show() ## error in jupyter notebook
sBach.write("midi", "2_bach_bwv111_6.mid") ## error in jupyter notebook

## B. Find all two-five progression in the song

sBach = corpus.parse('bach/bwv111.6')

sBachChords = sBach.chordify()

for c in sBachChords.recurse().getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, key.Key('C'))
    c.addLyric(str(rn.figure))

# sBachChords.show() ## error in jupyter notebook

count_2_5 = 0
for c in sBachChords.flat:
    if 'Chord' not in c.classes:
        continue
    if c.lyric == 'V':
        if prev_c.lyric == 'II':
            count_2_5 = count_2_5 + 1
    prev_c = c

print("two-fives in this song:", count_2_5)
