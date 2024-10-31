#!/usr/bin/python3
""" determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    # Masks to check leading bits
    mask1 = 1 << 7       # 10000000
    mask2 = 1 << 6       # 01000000

    for byte in data:
        # Mask to get only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
