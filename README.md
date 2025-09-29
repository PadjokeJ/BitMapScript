# BitMapScript  

Interpreted programming language that uses 256x bitmap images. You can either draw an image, and then interpret it, or write a ``main.bms`` file.

## .bms

Very basic compiled language to "write" images. Run ``python translate.py``.  
Compiled on a line by line basis. One pixel per line, anything more than 6 characters is discarded.  
You have to write colors in their hex format : ``ffffff`` for white.  
You can skip to the next line using ``endl``

## Positions 

Positions are defined by the values of the green and the blue channel of a given pixel  
``x : green, y : blue``

## Functions

Functions are defined by the value of a pixel's red channel.
The following headers indicate \[name\] : \[hex value\]

### Jump : 01

The most important command. Jumps to the given position.

### Write : 02

Reads the next pixel, writes it to the given position, then skips the next pixel.

### Read : 03

Currently useless. Sets the cursor's memory to the given position. (Could be used as a copy?)

### Endif : 10

Delimits the end of an if. Its position value is ignored

### If : 11

Checks if the memory slot at position holds the same value as the next pixel. If yes, execute what is enclosed between the if and the endif.

### Addition : 20

Adds the next to pixels (maxed out result at ffffff) and returns the value into the position argument.