import pandas as pd
import numpy as np
import os

def generate_battery_data(n_cycles=1000, noise_level=0.05):
    """
    生成模拟的蓄电池循环测试数据集
    
    参数:
        n_cycles: 循环次数
        noise_level: 噪声水平
    
    返回:
        DataFrame: 包含电池测试数据的数据框
    """
    np.random.seed(42)
    
    data = {
        'Cycle': np.arange(1, n_cycles + 1),
        'Voltage': np.random.uniform(3.0, 4.2, n_cycles) + np.random.normal(0, 0.1, n_cycles),
        'Current': np.random.uniform(-5, 5, n_cycles) + np.random.normal(0, 0.5, n_cycles),
        'Temperature': np.random.uniform(15, 45, n_cycles) + np.random.normal(0, 2, n_cycles),
        'Capacity': np.linspace(10, 8, n_cycles) + np.random.normal(0, 0.1, n_cycles),
    }
    
    # 生成SOH（0-100%），随循环次数逐渐衰减
    soh = 100 - (np.arange(n_cycles) / n_cycles) * 50 + np.random.normal(0, noise_level * 10, n_cycles)
    soh = np.clip(soh, 20, 100)
    data['SOH'] = soh
    
    df = pd.DataFrame(data)
    
    # 创建data目录
    os.makedirs('data', exist_ok=True)
    
    # 保存CSV文件
    df.to_csv('data/battery_data.csv', index=False)
    print(f"✓ 数据集生成成功！共 {len(df)} 条记录")
    print(f"✓ 数据文件保存至: data/battery_data.csv")
    print(f"\n数据统计:\n{df.describe()}")
    
    return df

if __name__ == "__main__":
    df = generate_battery_data(n_cycles=1000)