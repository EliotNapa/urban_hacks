# -*- coding: utf-8 -*-
"""
"""
import copy
import time
import itertools

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

    def print(self):
        print("{0} {1} {2} {3} {4} {5} {6} {7}".format(
            self.a,
            self.b,
            self.c,
            self.d,
            self.op1,
            self.op2,
            self.op3,
            self.result
        ))



def main():
    t1 = time.time() 
    exist_count = 0
    # src_list, count = calc_puzle(1, 3, 3, 7, detail_print = True)
    # src_list, count = calc_puzle(4, 6, 7, 9, detail_print = True)
    # if count > 0:
    #     exist_count += 1
    # print("{0} count = {1}".format(src_list, count))
    #
    #数字の重複を省く
    #(1,2,3,1) === (1,1,2,3)
    for a in range(0, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    src_list, count = calc_puzle(a, b, c, d, detail_print = False)
                    print("{0} count = {1}".format(src_list, count))
                    if count > 0:
                        exist_count += 1

    print("成立個数：{0}".format(exist_count))
    t2 = time.time()
    print("実行時間：{0}".format(t2-t1))

def calc_puzle(a,b,c,d, detail_print = False):
    ans_count = 0
    #問題文数字リスト
    src_nums = [str(a), str(b), str(c), str(d)]

    #演算子リスト
    oprs = ["+", "-", "*", "/"]


    #順列を作成する
    permu_list = list(itertools.permutations(src_nums))

    #演算子の組み合わせを作成する
    op_list= list(itertools.product(oprs, repeat=3))

    #逆ポーランド式要素全順列格納用リスト
    calc_list = []

    for op_set in op_list:
        for one_line in permu_list:
            calc_list.append(CalcRecord(
                one_line[0],
                one_line[1],
                one_line[2],
                one_line[3],
                op_set[0],
                op_set[1],
                op_set[2]
            ))

    calc_work = []


    #逆ポーランド式要素全順列より4パターンの
    #逆ポーランド演算式を計算し答えを求める
    for cur_calc in calc_list:
        calc_work.clear()
        #逆ポーランド演算式1
        # A B op1 C D op2 op3
        # (A op1 B) op3 (C op2 D)
        
        calc_work.append(cur_calc.a)
        calc_work.append(cur_calc.b)
        exec_revpol(cur_calc.op1, calc_work)
        calc_work.append(cur_calc.c)
        calc_work.append(cur_calc.d)
        exec_revpol(cur_calc.op2, calc_work)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F1")
        if 10 == cur_calc.result:
            ans_count += 1
            if detail_print:
                print_formula(cur_calc, "F1")
            # return [src_nums, ans_count]

        calc_work.clear()
        #逆ポーランド演算式2
        # A B op1 C op2 D op3
        # ((A op1 B) op2 C) op3 D
        calc_work.append(cur_calc.a)
        calc_work.append(cur_calc.b)
        exec_revpol(cur_calc.op1, calc_work)
        calc_work.append(cur_calc.c)
        exec_revpol(cur_calc.op2, calc_work)
        calc_work.append(cur_calc.d)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F2")
        if 10 == cur_calc.result:
            ans_count += 1
            if detail_print:
                print_formula(cur_calc, "F2")
            # return [src_nums, ans_count]

        calc_work.clear()
        #逆ポーランド演算式3
        # A B C op1 op2 D op3
        # (A op2 (B op1 C)) op3 D
        calc_work.append(cur_calc.a)
        calc_work.append(cur_calc.b)
        calc_work.append(cur_calc.c)
        exec_revpol(cur_calc.op1, calc_work)
        exec_revpol(cur_calc.op2, calc_work)
        calc_work.append(cur_calc.d)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F3")
        if 10 == cur_calc.result:
            ans_count += 1
            if detail_print:
                print_formula(cur_calc, "F3")
            # return [src_nums, ans_count]

        calc_work.clear()
        #逆ポーランド演算式4
        # A B C D op1 op2 op3
        # A op3 (B op2 (C op1 D))
        calc_work.append(cur_calc.a)
        calc_work.append(cur_calc.b)
        calc_work.append(cur_calc.c)
        calc_work.append(cur_calc.d)
        exec_revpol(cur_calc.op1, calc_work)
        exec_revpol(cur_calc.op2, calc_work)
        exec_revpol(cur_calc.op3, calc_work)
        cur_calc.result = calc_work.pop()

        # print_formula(cur_calc, "F4")
        if 10 == cur_calc.result:
            ans_count += 1
            if detail_print:
                print_formula(cur_calc, "F4")
            # return [src_nums, ans_count]
    return [src_nums, ans_count]


def print_formula(cur_calc, msg):
    """
    逆ポーランド演算子表示
    """
    if msg == "F1":
        # A B op1 C D op2 op3
        # (A op1 B) op3 (C op2 D)
        print("{8}# {0} {1} {2} {3} {4} {5} {6}\n(({0} {2} {1}) {5} {3}) {6} {4} = {7}".format(
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
        # A B op1 C op2 D op3
        # ((A op1 B) op2 C) op3 D
        print("{8}# {0} {1} {2} {3} {4} {5} {6}\n(({0} {2} {1}) {4} {3}) {6} {5}= {7}".format(
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
        # A B C op1 op2 D op3
        # (A op2 (B op1 C)) op3 D
        print("{8}# {0} {1} {2} {3} {4} {5} {6}\n({0} {4} ({1} {3} {2})) {6} {5} = {7}".format(
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
        # A B C D op1 op2 op3
        # A op3 (B op2 (C op1 D))
        print("{8}# {0} {1} {2} {3} {4} {5} {6}\n{0} {6} ({1} {5}({2} {4} {3})) = {7}".format(
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
    s2 = work_list.pop()
    s1 = work_list.pop()
    if (s1 == "∞" or s2 == "∞"):
        work_list.append("∞")
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
        work_list.append(r1 + r2)
    elif  op == "-":
        # print("{0} {1} {2} = {3}".format(
        #     r1,
        #     op,
        #     r2,
        #     r1 - r2
        # ))
        work_list.append(r1 - r2)
    elif  op == "*":
        # print("{0} {1} {2} = {3}".format(
        #     r1,
        #     op,
        #     r2,
        #     r1 * r2
        # ))
        work_list.append(r1 * r2)
    elif  op == "/":
        if (0 == r2):
            # print("{0} {1} {2} = {3}".format(
            #     r1,
            #     op,
            #     r2,
            #     "∞"
            # ))
            work_list.append("∞")
        else:
            # print("{0} {1} {2} = {3}".format(
            #     r1,
            #     op,
            #     r2,
            #     r1 / r2
            # ))
            work_list.append(r1 / r2)


if __name__ == '__main__':
    main()
