#!/bin/bash
#

clear(){
    pushd $1
    rm -rf CMakeCache.txt Makefile cmake_install.cmake lib bin CMakeFiles
    cd libhello && rm -rf CMakeCache.txt Makefile cmake_install.cmake lib bin CMakeFiles && cd ..
    cd src && rm -rf CMakeCache.txt Makefile cmake_install.cmake lib bin CMakeFiles && cd ..
    popd
}

for i in $@; do
    clear ${i}
done