from typing import Generator, Iterable

class BitHandler:
    def __init__(self):
        pass

    @staticmethod
    def bit_stream(file_path: str) -> Generator[int, None, None]:
        """Yield bits from a file one at a time."""
        with open(file_path, "rb") as f:
            while (byte := f.read(1)):
                b = byte[0]
                for i in range(7, -1, -1):
                    yield (b >> i) & 1

    @staticmethod             
    def bits_to_bytes(bits:Iterable[int]) -> Generator[int, None, None]:
        """Convert an iterable of bits to bytes."""
        byte = 0
        n = 0
        for bit in bits:
            byte = (byte << 1) | bit
            n += 1
            if n == 8:
                yield byte
                byte = 0
                n = 0
        if n > 0:
            # pad last byte
            byte <<= (8 - n)
            yield byte