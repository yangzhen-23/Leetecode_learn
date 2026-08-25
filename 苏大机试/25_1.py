# 给定范围1000年到2025年（闭区间），题目输入为year,month,day三个整数，请判断这个日期是否合法，是返回true, 否返回false。
def is_valid_date(year, month, day) -> bool:
    # 判断年份是否在范围内：
    if year < 1000 or year > 2025:
        return False
    # 判断月份是否在范围内：
    if month < 1 or month > 12:
        return False
    # 判断日期是否合法：
    if day < 1 or day > 31:
        return False
    # 判断月份和日期的对应关系：
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 ==0 and year %100 ==0 and year %400 != 0:
        days[1] = 29
    if day > days[month - 1]:
        return False
    return True
