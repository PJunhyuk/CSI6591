#!/usr/bin/env python
# coding: utf-8

# import

from music21 import *

# testing environment settings -> fail

# environment.set('musicxmlPath', 'C:\Program Files (x86)\MuseScore 2\\bin/MuseScore.exe')
# environment.set('musescoreDirectPNGPath', 'C:\Program Files (x86)\MuseScore 2\\bin/MuseScore.exe')

## 1. About Bach's chorale 'bach/bwv101.7'
## A. Count the number of F3, F4, A3, A4, and C4 notes in the entire song

sBach = corpus.parse('bach/bwv101.7')

for i in range(len(sBach)):
    print(sBach[i])

count_F3 = 0
count_F4 = 0
count_A3 = 0
count_A4 = 0
count_C4 = 0
for k in range(3, 7): ## Soprano: 3 / Alto: 4 / Tenor: 5 / Bass: 6
    for i in range(1, len(sBach[k])): ## sBach[3][0] is meta data
        for j in range(0, len(sBach[k][i])):
            if sBach[k][i][j] == note.Note("F3"):
                count_F3 = count_F3 + 1
            elif sBach[k][i][j] == note.Note("F4"):
                count_F4 = count_F4 + 1
            elif sBach[k][i][j] == note.Note("A3"):
                count_A3 = count_A3 + 1
            elif sBach[k][i][j] == note.Note("A4"):
                count_A4 = count_A4 + 1
            elif sBach[k][i][j] == note.Note("C4"):
                count_C4 = count_C4 + 1

print("F3:", count_F3)
print("F4:", count_F4)
print("A3:", count_A3)
print("A4:", count_A4)
print("C4:", count_C4)

## B. Find the total sum of the local offset (for its measure) and the global offset (for the entire song) of all the notes in the tenor part

global_offset = -1
sum_local_offset = 0
sum_global_offset = 0
for i in range(1, len(sBach[5])): ## Tenor: 5
    for thisNote in sBach[5][i].getElementsByClass(note.Note):
        global_offset = global_offset + 1
#         print(thisNote, int(thisNote.offset), global_offset)
        sum_local_offset = sum_local_offset + int(thisNote.offset)
        sum_global_offset = sum_global_offset + global_offset

print("The total sum of the local offset:", sum_local_offset)
print("The total sum of the global offset:", sum_global_offset)

## C. If the pitches of the notes in the melody of the Soprano part are repeated, combine them all together to a single note (for example, (C5 quater) (C5 quater) (C5 half) can be combined to (C5 whole)). Show the revised score.

note_num = 0
for i in range(1, len(sBach[3])): ## Soprano: 3
    for thisNote in sBach[3][i].getElementsByClass(note.Note):
        note_num = note_num + 1
        if note_num == 1: ## first node
            prev_note = thisNote
        else:
            if thisNote.pitch == prev_note.pitch:
                ## Use tie instead of combining notes, because soprano has melody
                prev_note.tie = tie.Tie('start')
                prev_note.tie.style = 'normal'
                thisNote.tie = tie.Tie('stop')
            prev_note = thisNote

sBach.show() ## error in jupyter notebook
