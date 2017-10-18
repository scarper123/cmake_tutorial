cmake_minimum_required(VERSION 2.8)
project(HELLO)
set(LIB_SRC hello.c)
set(APP_SRC main.c)
add_library(libhello ${LIB_SRC})
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello") # set the library name
