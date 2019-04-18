# -*- coding: UTF-8 -*-
# 这是一个用来计算工时的简单程序, 程序的输入包括:
# 1. 公司规定的工作时间, 例如[[9, 18]]表示工作时间是9点到18点, [[9, 12], [14, 18]]表示工作时间是9点到12点和14点到18点
# 2. 员工的开始签到时间和结束签到时间
# 3. 为了简化运算, 我们把时间的最小单位设置为小时

def calculate_working_time(work_periods, start, end):
    work_time = 0
    # 对每个工作区间(p_start, p_end), 计算它和(start, end)的交集, 并把结果累加到work_time上
    for p_start, p_end in work_periods:
        # 当前区间的开始时间大于签到的结束时间, 则跳出循环
        if p_start >= end:
            break

        # 当前时间的结束时间小于签到的开始时间, 则检查下一个区间
        if p_end <= start:
            continue

        # 当前区间和签到区间有交集
        work_period = min(p_end, end) - max(p_start, start)
        work_time += work_period

    return work_time


class TestCase:
    def __init__(self, work_periods, start, end, result):
        self.work_periods = work_periods
        self.start = start
        self.end = end
        self.result = result

    def __str__(self):
        return "work_periods: %s, start: %s, end: %s, result: %s" % (self.work_periods, self.start, self.end, self.result)

if __name__ == "__main__":
    test_cases = [TestCase([[9, 17]], 10, 20, 7),
                  TestCase([[9, 12], [14, 19]], 7, 8, 0),
                  TestCase([[9, 12], [14, 19]], 13, 14, 0),
                  TestCase([[9, 12], [14, 19]], 20, 22, 0),
                  TestCase([[9, 12], [14, 19]], 7, 10, 1),
                  TestCase([[9, 12], [14, 19]], 7, 13, 3),
                  TestCase([[9, 12], [14, 19]], 7, 15, 4),
                  TestCase([[9, 12], [14, 19]], 7, 20, 8),
                  TestCase([[9, 12], [14, 19]], 10, 13, 2),
                  TestCase([[9, 12], [14, 19]], 10, 15, 3),
                  TestCase([[9, 12], [14, 19]], 10, 20, 7),
                  TestCase([[9, 12], [14, 19]], 13, 15, 1),
                  TestCase([[9, 12], [14, 19]], 13, 20, 5),
                  TestCase([[9, 12], [14, 19]], 15, 20, 4)]
    for case in test_cases:
        assert case.result == calculate_working_time(case.work_periods, case.start, case.end)
        print("case: %s test succeed" % case)
