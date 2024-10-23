def calculate_change(n, x):
    # 定义可用的硬币面值
    coins = [500, 100, 50, 10]
    
    # 计算需要找零的金额
    change = n - x
    if change < 0:
        return "输入的金额不足以购买商品。"
    
    # 存储找零时使用的硬币数量
    result = {}
    
    # 逐步计算每种硬币的数量
    for coin in coins:
        count = change // coin
        if count > 0:
            result[coin] = count
            change -= coin * count
    
    return result

# 示例输入与输出
n = int(input("请输入支付的金额（单位：円）："))
x = int(input("请输入商品价格（单位：円）："))
result = calculate_change(n, x)

if isinstance(result, dict):
    print("找零时使用的硬币数量如下：")
    for coin, count in result.items():
        print(f"{coin}円硬币: {count}枚")
else:
    print(result)
