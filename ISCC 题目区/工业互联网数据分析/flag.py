import hashlib

def generate_flag(*answers):
    # 将所有答案使用英文逗号连接
    combined_answers = ','.join(answers)
    # 生成flag格式
    initial_flag = f"ISCC{{{combined_answers}}}"
    # 对flag进行MD5加密
    md5_hash = hashlib.md5(initial_flag.encode()).hexdigest()
    return md5_hash

# 示例用法
if __name__ == "__main__":
    # 每道题目的所有填空写在一个字符串中
    answers = [
        "IP1,IP2,...,NUM",  # 第一小题答案：IP顺序从小到大排列，涉及的IP个数由选手自己判断，数值为整数
        "XX",  # 第二小题答案：数值为整数
        "IP1,IP2,...,NUM",  # 第三小题答案：IP顺序从小到大排列，涉及的IP个数由选手自己判断，数值保留小数点后2位
        "IP1,IP2,...",  # 第四小题答案：IP顺序从小到大排列，涉及的IP个数由选手自己判断
        "NAME,X,X"   # 第五小题答案：数据校验算法名称长度为5个字符，其中英文字母大写
    ]
    # 生成MD5加密后的flag
    final_flag = generate_flag(*answers)
    # 输出最终的MD5加密字符串
    print(final_flag)
