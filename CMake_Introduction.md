# CAMKE 入门实战

## 什么是CMAKE
1. Camke是一种平台无关的CMakeList.txt文件来定制化编译过程。
2. 然后根据目标平台生成对应的Makefile和工程文件。

### Linux平台下使用CMake生成Makefile编译过程如下：
1. 编写CMake配置文件CMakeLists.txt。
2. 执行命令 cmake PATH 或者 ccmake PATH 生成 Makefile。
3. 使用 make 命令进行编译。

### CMakeList.txt语法是有命令和注释组成。
1. 命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。
2. 符号 # 后面的内容被认为是注释。

## 例子
### 单个源文件
main.c: 
```C
#include <stdio.h>
int main(int argc, char const *argv[])
{
    printf("Hello World!\n");
    return 0;
}
```

CMakeLists.txt:
```CMake
cmake_minimum_required(VERSION 2.8 )
project(HELLO)
set(SRC_LIST main.c)
add_executable(hello ${SRC_LIST})
```

编译执行：
```Shell
eselnts1291(master) ~/workspace/cmake_tutorial/demo1> ll
total 8
-rw-rw---- 1 eghklmi gbgusers 115 Oct 18 13:43 main.c
-rw-rw---- 1 eghklmi gbgusers 106 Oct 18 13:48 CMakeLists.txt
eselnts1291(master) ~/workspace/cmake_tutorial/demo1> cmake .
-- The C compiler identification is GNU 4.4.7
-- The CXX compiler identification is GNU 4.4.7
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/eghklmi/workspace/cmake_tutorial/demo1
eselnts1291(master) ~/workspace/cmake_tutorial/demo1> make
Scanning dependencies of target hello
[100%] Building C object CMakeFiles/hello.dir/main.c.o
Linking C executable hello
[100%] Built target hello
eselnts1291(master) ~/workspace/cmake_tutorial/demo1> ./hello 
Hello World!
```

### 多个源文件, 同一目录
main.c:
```C
#include "hello.h"

int main(int argc, char const *argv[])
{
    hello("World!!!");
    return 0;
}
```

hello.c:
```C
#include <stdio.h>
#include "hello.h"

void hello(const char* name){
    printf("Hello %s\n", name);
}
```

hello.h:
```C
#ifndef HELLO_
#define HELLO_
void hello(const char* name);
#endif
```

CMakeLists.txt:
```CMake
cmake_minimum_required(VERSION 2.8)
project(HELLO)
set(LIB_SRC hello.c)
set(APP_SRC main.c)
add_library(libhello ${LIB_SRC})
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello") # set the library name
```

编译执行：
```Shell
eselnts1291(master) ~/workspace/cmake_tutorial/demo3> ll
total 16
-rw-rw---- 1 eghklmi gbgusers  67 Oct 18 13:56 hello.h
-rw-rw---- 1 eghklmi gbgusers 102 Oct 18 13:57 hello.c
-rw-rw---- 1 eghklmi gbgusers 282 Oct 18 15:20 CMakeLists.txt
-rw-rw---- 1 eghklmi gbgusers  99 Oct 18 15:57 main.c
eselnts1291(master) ~/workspace/cmake_tutorial/demo3> cmake .
-- The C compiler identification is GNU 4.4.7
-- The CXX compiler identification is GNU 4.4.7
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/eghklmi/workspace/cmake_tutorial/demo3
eselnts1291(master) ~/workspace/cmake_tutorial/demo3> make
Scanning dependencies of target libhello
[ 50%] Building C object CMakeFiles/libhello.dir/hello.c.o
Linking C static library libhello.a
[ 50%] Built target libhello
Scanning dependencies of target hello
[100%] Building C object CMakeFiles/hello.dir/main.c.o
Linking C executable hello
[100%] Built target hello
eselnts1291(master) ~/workspace/cmake_tutorial/demo3> ./hello 
Hello World!!!
```

### 多个源文件， 多个目录
1. 文件内容跟上一个一样， 只是目录结构改了
2. CMakeList.txt文件修改

目录结构:
```
eselnts1291(master) ~/workspace/cmake_tutorial/demo4> tree
.
|-- CMakeLists.txt
|-- libhello
|   |-- CMakeLists.txt
|   |-- hello.c
|   `-- hello.h
`-- src
    |-- CMakeLists.txt
    |-- hello
    `-- main.c

2 directories, 7 files
```

Project CMakeLists.txt:
```
cmake_minimum_required(VERSION 2.8)
project(HELLO)
add_subdirectory(src)
add_subdirectory(libhello)
```

src CMakeLists.txt:
```
include_directories(${PROJECT_SOURCE_DIR}/libhello)
set(APP_SRC main.c)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)  # 指定可执行文件路径
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)
```

libhello CMakeLists.txt:
```
set(LIB_SRC hello.c)
add_library(libhello ${LIB_SRC})
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)  # 指定库文件路径
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello")
```

编译执行：
```Shell
eselnts1291(master) ~/workspace/cmake_tutorial/demo4> cmake .
-- The C compiler identification is GNU 4.4.7
-- The CXX compiler identification is GNU 4.4.7
...
eselnts1291(master) ~/workspace/cmake_tutorial/demo4> make
Scanning dependencies of target libhello
[ 50%] Building C object libhello/CMakeFiles/libhello.dir/hello.c.o
Linking C static library ../lib/libhello.a
[ 50%] Built target libhello
Scanning dependencies of target hello
[100%] Building C object src/CMakeFiles/hello.dir/main.c.o
/home/eghklmi/workspace/cmake_tutorial/demo4/src/main.c: In function 'main':
/home/eghklmi/workspace/cmake_tutorial/demo4/src/main.c:8: warning: assignment discards qualifiers from pointer target type
Linking C executable ../bin/hello
[100%] Built target hello
eselnts1291(master) ~/workspace/cmake_tutorial/demo4> tree
...
|-- bin
|   `-- hello
|-- lib
|   `-- libhello.a
...
13 directories, 57 files
eselnts1291(master) ~/workspace/cmake_tutorial/demo4> cd bin/
eselnts1291(master) ~/workspace/cmake_tutorial/demo4/bin> ./hello
Hello World!!!
```

### Installing and Testing

### Adding System Introspection

### Adding a Generated File and Generator

### Building an Installer

### Adding Support for a Dashboard

## 参考资料
1. [官网资料](https://cmake.org/cmake/help/v3.10/)
2. [cmake-tutorial](https://cmake.org/cmake-tutorial/)
2. [CMake CSDN](http://blog.csdn.net/wzjking0929/article/details/52701831)
