#include <stdint.h>

uint32_t swap_endian(uint8_t* buffer)
{
    return buffer[3] | buffer[2] << 8 | buffer[1] << 16 | buffer[0] << 24;
}
