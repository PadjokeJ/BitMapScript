# BitMapScript  

Interpreted programming language that uses 256x bitmap images

## Positions 

Positions are defined by the values of the green and the blue channel of a given pixel  
´´x : green, y : blue´´

## Functions

Functions are defined by the value of a pixel's red channel.
The following headers indicate \[name\] : \[value\]

### Jump : 01

The most important command. Jumps to the given position.

### Write : 02

Reads the next pixel, writes it to the given position, then skips the next pixel.

### Read : 03

Currently useless. Sets the cursor's memory to the given position

