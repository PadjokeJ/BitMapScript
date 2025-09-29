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
The following headers indicate \[name\] : \[value\]

### Jump : 01

The most important command. Jumps to the given position.

### Write : 02

Reads the next pixel, writes it to the given position, then skips the next pixel.

### Read : 03

Currently useless. Sets the cursor's memory to the given position

