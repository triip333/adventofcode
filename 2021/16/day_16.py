from os import sys, path
import math
sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
from common import get_input

def hex_to_bin(input):
    return (bin(int(input, 16))[2:]).zfill(len(input * 4))

class Bits():
    def __init__(self, input):
        self.s = input
    
    def read_bits(self, ln):
        res = self.s[:ln]
        self.s = self.s[ln:]
        return res
    
    def read_int(self, ln):
        return int(self.read_bits(ln), 2)

    def get_packets(self, count=1e6):
        global version_sum
        res_list = []
        while '1' in self.s and len(res_list) < count:
            version = self.read_int(3)
            version_sum += version
            type_id = self.read_int(3)
            if type_id == 4:
                res, read_done = '', False
                while not read_done:
                    temp = self.read_bits(5)
                    read_done = temp[0] == '0'
                    res += temp[1:5]
                res_list.append(int(res, 2))
            else:
                length_type = self.read_int(1)
                if length_type == 0:
                    ln = self.read_int(15)
                    b = Bits(self.read_bits(ln))
                    op_params = b.get_packets()
                else:
                    ln = self.read_int(11)
                    b = Bits(self.s)
                    op_params = b.get_packets(ln)
                    self.s = b.s

                # Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
                if type_id == 0:
                    value = sum(op_params)
                # Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
                elif type_id == 1:
                    value = math.prod(op_params)
                # Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
                elif type_id == 2:
                    value = min(op_params)
                # Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
                elif type_id == 3:
                    value = max(op_params)
                # Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
                elif type_id == 5:
                    assert len(op_params) == 2
                    value = 1 if op_params[0] > op_params[1] else 0
                # Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
                elif type_id == 6:
                    assert len(op_params) == 2
                    value = 1 if op_params[0] < op_params[1] else 0
                # Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
                elif type_id == 7:
                    assert len(op_params) == 2
                    value = 1 if op_params[0] == op_params[1] else 0
                    
                res_list.append(value)
        return res_list

def part_1(input):
    global version_sum
    version_sum = 0
    bits = Bits(hex_to_bin(input))
    bits.get_packets()
    return version_sum

def part_2(input):
    bits = Bits(hex_to_bin(input))
    return bits.get_packets().pop()

if __name__ == '__main__':
    input = get_input()
    assert part_1('8A004A801A8002F478') == 16
    assert part_1('620080001611562C8802118E34') == 12
    assert part_1('C0015000016115A2E0802F182340') == 23
    assert part_1('A0016C880162017C3686B18A3D4780') == 31
    print(part_1(input))
    assert part_2('C200B40A82') == 3, 'finds the sum of 1 and 2, resulting in the value 3'
    assert part_2('04005AC33890') == 54, 'finds the product of 6 and 9, resulting in the value 54'
    assert part_2('880086C3E88112') == 7, 'finds the minimum of 7, 8, and 9, resulting in the value 7'
    assert part_2('CE00C43D881120') == 9, 'finds the maximum of 7, 8, and 9, resulting in the value 9'
    assert part_2('D8005AC2A8F0') == 1, 'produces 1, because 5 is less than 15'
    assert part_2('F600BC2D8F') == 0, 'produces 0, because 5 is not greater than 15'
    assert part_2('9C005AC2F8F0') == 0, 'produces 0, because 5 is not equal to 15'
    assert part_2('9C0141080250320F1802104A08') == 1, 'produces 1, because 1 + 3 = 2 * 2'
    print(part_2(input))
