# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import operator
from typing import Any
from assertpy import assert_that

operations = {
        0: lambda a: sum(a),
        1: lambda a: math.prod(a),
        2: lambda a: min(a),
        3: lambda a: max(a),
        5: lambda a: operator.gt(*a),
        6: lambda a: operator.lt(*a),
        7: lambda a: operator.eq(*a)
    }


def extract_data_from_file(file_name: str) -> str:
    with open(file_name, 'r') as data_file:
        return bin(int('1'+data_file.read().strip(), 16))[3:]


class Bits:
    def __init__(self, string: str):
        self.data = iter(string)
        self.bits = len(string)

    def pop(self, n: int) -> str:
        s_: str = ""
        for i in range(n):
            s_ += next(self.data)
            self.bits -= 1
        return s_

    def read(self):
        version = int(self.pop(3), 2)
        op_id = int(self.pop(3), 2)
        if op_id == 4:
            n_ = ""
            while self.pop(1) == '1':
                n_ += self.pop(4)
            return version, op_id, int(n_ + self.pop(4), 2)
        if self.pop(1) == '1':
            s_packages =[]
            for i in range(int(self.pop(11), 2)):
                s_packages.append(self.read())
            return version, op_id, s_packages
        else:
            s_p_len = self.pop(15)
            s_p = Bits(self.pop(int(s_p_len, 2)))
            s_packages = []
            while s_p.bits > 0:
                s_packages.append(s_p.read())
            return version, op_id, s_packages
            

def do_operations(data: tuple):
    _, op_id, s_packages = data
    if isinstance(s_packages, int):
        return s_packages
    return operations[op_id](do_operations(s_package) for s_package in s_packages)


def get_version_sum(data: tuple[int, int, Any]) -> int:
    v, _, s_packages = data
    if isinstance(s_packages, int):
        return v
    return sum([get_version_sum(s_package) for s_package in s_packages]) + v


if __name__ == '__main__':
    # PART1 TEST
    bits_s = extract_data_from_file("data_test_packet_v_sum1.txt")
    bits = Bits(bits_s).read()
    answer = get_version_sum(bits)
    assert_that(answer).is_equal_to(16)
    bits_s = extract_data_from_file("data_test_packet_v_sum2.txt")
    bits = Bits(bits_s).read()
    answer = get_version_sum(bits)
    assert_that(answer).is_equal_to(12)
    bits_s = extract_data_from_file("data_test_packet_v_sum3.txt")
    bits = Bits(bits_s).read()
    answer = get_version_sum(bits)
    assert_that(answer).is_equal_to(23)
    bits_s = extract_data_from_file("data_test_packet_v_sum4.txt")
    bits = Bits(bits_s).read()
    answer = get_version_sum(bits)
    assert_that(answer).is_equal_to(31)

    answer = do_operations(Bits(bin(int('1' + 'C200B40A82', 16))[3:]).read())
    assert_that(answer).is_equal_to(3)
    answer = do_operations(Bits(bin(int('1' + '04005AC33890', 16))[3:]).read())
    assert_that(answer).is_equal_to(54)
    answer = do_operations(Bits(bin(int('1' + '880086C3E88112', 16))[3:]).read())
    assert_that(answer).is_equal_to(7)
    answer = do_operations(Bits(bin(int('1' + 'CE00C43D881120', 16))[3:]).read())
    assert_that(answer).is_equal_to(9)
    answer = do_operations(Bits(bin(int('1' + 'D8005AC2A8F0', 16))[3:]).read())
    assert_that(answer).is_equal_to(1)
    answer = do_operations(Bits(bin(int('1' + 'F600BC2D8F', 16))[3:]).read())
    assert_that(answer).is_equal_to(0)
    answer = do_operations(Bits(bin(int('1' + '9C005AC2F8F0', 16))[3:]).read())
    assert_that(answer).is_equal_to(0)
    answer = do_operations(Bits(bin(int('1' + '9C0141080250320F1802104A08', 16))[3:]).read())
    assert_that(answer).is_equal_to(1)
    #
    bits_s = extract_data_from_file("data_test_operational1.txt")
    bits = Bits(bits_s).read()
    answer = do_operations(bits)
    assert_that(answer).is_equal_to(0)

    bits_s = extract_data_from_file("data_test_operational2.txt")
    bits = Bits(bits_s).read()
    answer = do_operations(bits)
    assert_that(answer).is_equal_to(1)

    # PART 1 & 2 REAL
    bits_s = extract_data_from_file("data_real.txt")
    bits = Bits(bits_s).read()
    answer = do_operations(bits)
    print(answer)
