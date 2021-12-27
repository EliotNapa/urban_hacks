# -*- coding: utf-8 -*-
"""
urban hack解法プログラム
"""
import copy

class CalcRecord():
    """
    逆ポーランド用の要素格納クラス
    """
    def __init__(self, a,b,c,d,op1,op2,op3):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.result = -1




def main():
    """
    urban hacks解法総当り計算
    """
    #問題文数字リスト
    src_nums = ["1", "3", "3", "7"]
    #src_nums = ["3", "4", "7", "8"]

    #別の問題サンプル
    #src_nums = ["1", "2", "3", "4"]

    #演算子リスト
    op_list = ["+", "-", "*", "/"]

    #順列ホルダー
    nums_holder = [0] * len(src_nums)

    #全順列格納用リスト
    result_list = []

    #順列を作成する
    process_ary(src_nums, 0, len(src_nums), nums_holder, result_list)

    #逆ポーランド式要素全順列格納用リスト
    calc_list = []

    #演算子の順列を作成し、数列と組み合わせて
    #逆ポーランド式要素全順列を作成する
    for i in result_list:
        for op1 in op_list:
            for op2 in op_list:
                for op3 in op_list:
                    calc_list.append(CalcRecord(
                        i[0],
                        i[1],
                        i[2],
                        i[3],
                        op1,
                        op2,
                        op3
                    ))

    calc_work = []


    #逆ポーランド式要素全順列より4パターンの
    #逆ポーランド演算式を計算し答えを求める
    for cur_calc in calc_list:
        calc_work.clear()
        #逆ポーランド演算式1
        # A B op1 C D op2 op3
        # (A op1 B) op3 (C op2 D)
        #1 7 / 3 3 + * = 10.0
        #(1 / 7)*(3 + 3)
        #
        # (1 + (7 / 3)) * 3
        # 1 7 3 / + 3 *
        
        calc_work.insert(0, cur_calc.a)
        calc_work.insert(0, cur_calc.b)
        exec_revpol(cur_calc.op1, calc_work)
        calc_work.insert(0, cur_calc.c)
        calc_work.insert(0, cur_calc.d)
        exec_revpol(cur_calc.op2, calc_work)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F1")
        if 10 == cur_calc.result:
            print_formula(cur_calc, "F1")
            return

        calc_work.clear()
        #逆ポーランド演算式2
        # A B op1 C op2 D op3
        # ((A op1 B) op2 C) op3 D
        calc_work.insert(0, cur_calc.a)
        calc_work.insert(0, cur_calc.b)
        exec_revpol(cur_calc.op1, calc_work)
        calc_work.insert(0, cur_calc.c)
        exec_revpol(cur_calc.op2, calc_work)
        calc_work.insert(0, cur_calc.d)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F2")
        if 10 == cur_calc.result:
            print_formula(cur_calc, "F2")
            return

        calc_work.clear()
        #逆ポーランド演算式3
        # A B C op1 op2 D op3
        # (A op2 (B op1 C)) op3 D
        calc_work.insert(0, cur_calc.a)
        calc_work.insert(0, cur_calc.b)
        calc_work.insert(0, cur_calc.c)
        exec_revpol(cur_calc.op1, calc_work)
        exec_revpol(cur_calc.op2, calc_work)
        calc_work.insert(0, cur_calc.d)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F3")
        if 10 == cur_calc.result:
            print_formula(cur_calc, "F3")
            return

        calc_work.clear()
        #逆ポーランド演算式4
        # A B C D op1 op2 op3
        # A op3 (B op2 (C op1 D))
        calc_work.insert(0, cur_calc.a)
        calc_work.insert(0, cur_calc.b)
        calc_work.insert(0, cur_calc.c)
        calc_work.insert(0, cur_calc.d)
        exec_revpol(cur_calc.op1, calc_work)
        exec_revpol(cur_calc.op2, calc_work)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F4")
        if 10 == cur_calc.result:
            print_formula(cur_calc, "F4")
            return


def print_formula(cur_calc, msg):
    """
    逆ポーランド演算子表示
    """
    if msg == "F1":
        print("{8}# {0} {1} {2} {3} {4} {5} {6} = {7}".format(
            cur_calc.a,
            cur_calc.b,
            cur_calc.op1,
            cur_calc.c,
            cur_calc.d,
            cur_calc.op2,
            cur_calc.op3,
            cur_calc.result,
            msg
        ))
    elif msg == "F2":
        print("{8}# {0} {1} {2} {3} {4} {5} {6} = {7}".format(
            cur_calc.a,
            cur_calc.b,
            cur_calc.op1,
            cur_calc.c,
            cur_calc.op2,
            cur_calc.d,
            cur_calc.op3,
            cur_calc.result,
            msg
        ))
    elif msg == "F3":
        print("{8}# {0} {1} {2} {3} {4} {5} {6} = {7}".format(
            cur_calc.a,
            cur_calc.b,
            cur_calc.c,
            cur_calc.op1,
            cur_calc.op2,
            cur_calc.d,
            cur_calc.op3,
            cur_calc.result,
            msg
        ))
    else:
        print("{8}# {0} {1} {2} {3} {4} {5} {6} = {7}".format(
            cur_calc.a,
            cur_calc.b,
            cur_calc.c,
            cur_calc.d,
            cur_calc.op1,
            cur_calc.op2,
            cur_calc.op3,
            cur_calc.result,
            msg
        ))

    

def exec_revpol(op, work_list):
    """
    逆ポーランド演算を実施する
    op        - 演算子
    work_list - 演算の要素と結果を格納するスタック
    """
    s2 = work_list.pop(0)
    s1 = work_list.pop(0)
    if (s1 == "∞" or s2 == "∞"):
        work_list.insert(0, "∞")
        return

    r2 = float(s2)
    r1 = float(s1)
    if op == "+":
        # print("{0} {1} {2} = {3}".format(
        #     r1,
        #     op,
        #     r2,
        #     r1 + r2
        # ))
        work_list.insert(0, r1 + r2)
    elif  op == "-":
        # print("{0} {1} {2} = {3}".format(
        #     r1,
        #     op,
        #     r2,
        #     r1 - r2
        # ))
        work_list.insert(0, r1 - r2)
    elif  op == "*":
        # print("{0} {1} {2} = {3}".format(
        #     r1,
        #     op,
        #     r2,
        #     r1 * r2
        # ))
        work_list.insert(0, r1 * r2)
    elif  op == "/":
        if (0 == r2):
            # print("{0} {1} {2} = {3}".format(
            #     r1,
            #     op,
            #     r2,
            #     "∞"
            # ))
            work_list.insert(0, "∞")
        else:
            # print("{0} {1} {2} = {3}".format(
            #     r1,
            #     op,
            #     r2,
            #     r1 / r2
            # ))
            work_list.insert(0, r1 / r2)

def process_ary(src_list, depth, org_depth, nums_holder, result_list):
    """
    数字の順列作成(再帰)
    src_list     - 問題数字列(呼び元で選択されたものは削除されていく)
    depth        - 再帰深さ
    org_depth    - 元文字列の長さ
    nums_holder  - 順列格納用
    result_list  - すべての順列を格納するリスト
    """
    for idx in range(len(src_list)):
        local_list = copy.copy(src_list)
        nums_holder[depth] = local_list.pop(idx)
        if depth < org_depth - 1:
            process_ary(local_list, depth + 1, org_depth, nums_holder, result_list)
        else:
            # print("A:{0},B:{1},C:{2},D:{3}".format(nums_holder[0],nums_holder[1],nums_holder[2],nums_holder[3]))
            result_list.append([nums_holder[0],nums_holder[1],nums_holder[2],nums_holder[3]])


if __name__ == '__main__':
    main()

