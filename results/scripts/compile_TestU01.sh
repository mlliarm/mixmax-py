#!/bin/bash

echo "Compiling test_mixmax_smallcrush..."

gcc -o test_mixmax_smallcrush test_mixmax_smallcrush.c \
    $(python3-config --includes) \
    -I$HOME/TestU01/include \
    -L$HOME/TestU01/lib \
    -ltestu01 -lprobdist -lmylib -lm \
    $(python3-config --ldflags --embed)

if [ $? -eq 0 ]; then
    echo "Compilation successful!"
    echo "Run with: ./test_mixmax_smallcrush"
else
    echo "Compilation failed!"
    exit 1
fi
