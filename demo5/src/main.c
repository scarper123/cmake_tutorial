#include "hello.h"

int main(int argc, char const *argv[])
{
    const char* name = "World!!!";
    if (argc > 1)
    {
        name = argv[1];
    }
    hello(name);
    return 0;
}