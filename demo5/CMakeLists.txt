cmake_minimum_required(VERSION 2.8)

option(USE_CLANG "build application with clang" ON) # OFF is the default
if(USE_CLANG)
    message("Use CLANG as default compiler...")
    SET (CMAKE_C_COMPILER             "/home/eghklmi/installed/clang_llvm/v5000/bin/clang")
    SET (CMAKE_C_FLAGS                "-Wall -std=c99")
    SET (CMAKE_C_FLAGS_DEBUG          "-g")
    SET (CMAKE_C_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
    SET (CMAKE_C_FLAGS_RELEASE        "-O4 -DNDEBUG")
    SET (CMAKE_C_FLAGS_RELWITHDEBINFO "-O2 -g")

    SET (CMAKE_CXX_COMPILER             "/home/eghklmi/installed/clang_llvm/v5000/bin/clang++")
    SET (CMAKE_CXX_FLAGS                "-Wall")
    SET (CMAKE_CXX_FLAGS_DEBUG          "-g")
    SET (CMAKE_CXX_FLAGS_MINSIZEREL     "-Os -DNDEBUG")
    SET (CMAKE_CXX_FLAGS_RELEASE        "-O4 -DNDEBUG")
    SET (CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O2 -g")
endif(USE_CLANG)

project(HELLO)

add_subdirectory(src)
add_subdirectory(libhello)