class Solution:
    def reverseBits(self, n: int) -> int:


        binary_array = []

        for i in range(32):
            if 1<< i & n:
                binary_array.append(1)
            else:
                binary_array.append(0)

        print(binary_array)
        number = int("".join(map(str, binary_array)), 2)

        return number
        