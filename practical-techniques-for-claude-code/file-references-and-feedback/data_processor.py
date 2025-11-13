"""
データ処理プログラム
※わざとリファクタリングが必要なコードを含んでいます
"""

def process_data(data):
    # データを処理する関数
    result = []
    for i in range(len(data)):
        if data[i]['type'] == 'A':
            if data[i]['value'] > 100:
                if data[i]['status'] == 'active':
                    result.append({
                        'id': data[i]['id'],
                        'processed_value': data[i]['value'] * 1.5 + 20,
                        'category': 'high',
                        'tax': data[i]['value'] * 0.1
                    })
                else:
                    result.append({
                        'id': data[i]['id'],
                        'processed_value': data[i]['value'] * 1.2 + 10,
                        'category': 'medium',
                        'tax': data[i]['value'] * 0.08
                    })
            else:
                result.append({
                    'id': data[i]['id'],
                    'processed_value': data[i]['value'] * 1.1 + 5,
                    'category': 'low',
                    'tax': data[i]['value'] * 0.05
                })
        elif data[i]['type'] == 'B':
            if data[i]['value'] > 100:
                if data[i]['status'] == 'active':
                    result.append({
                        'id': data[i]['id'],
                        'processed_value': data[i]['value'] * 2.0 + 30,
                        'category': 'premium',
                        'tax': data[i]['value'] * 0.12
                    })
                else:
                    result.append({
                        'id': data[i]['id'],
                        'processed_value': data[i]['value'] * 1.8 + 25,
                        'category': 'standard',
                        'tax': data[i]['value'] * 0.1
                    })
            else:
                result.append({
                    'id': data[i]['id'],
                    'processed_value': data[i]['value'] * 1.5 + 15,
                    'category': 'basic',
                    'tax': data[i]['value'] * 0.07
                })
    return result

def calculate_stats(data):
    # 統計を計算
    total = 0
    count = 0
    max_val = 0
    min_val = 999999

    for i in range(len(data)):
        total = total + data[i]['processed_value']
        count = count + 1
        if data[i]['processed_value'] > max_val:
            max_val = data[i]['processed_value']
        if data[i]['processed_value'] < min_val:
            min_val = data[i]['processed_value']

    avg = total / count

    # 中央値を計算
    sorted_data = []
    for i in range(len(data)):
        sorted_data.append(data[i]['processed_value'])
    for i in range(len(sorted_data)):
        for j in range(len(sorted_data) - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                temp = sorted_data[j]
                sorted_data[j] = sorted_data[j + 1]
                sorted_data[j + 1] = temp

    if len(sorted_data) % 2 == 0:
        median = (sorted_data[len(sorted_data) // 2] + sorted_data[len(sorted_data) // 2 - 1]) / 2
    else:
        median = sorted_data[len(sorted_data) // 2]

    return {
        'total': total,
        'count': count,
        'average': avg,
        'max': max_val,
        'min': min_val,
        'median': median
    }

def print_report(stats, data):
    # レポートを出力
    print('=' * 50)
    print('データ処理レポート')
    print('=' * 50)
    print(f'合計値: {stats["total"]}')
    print(f'データ数: {stats["count"]}')
    print(f'平均値: {stats["average"]}')
    print(f'最大値: {stats["max"]}')
    print(f'最小値: {stats["min"]}')
    print(f'中央値: {stats["median"]}')
    print('=' * 50)
    print('カテゴリ別集計:')

    # カテゴリ別に集計
    categories = {}
    for i in range(len(data)):
        if data[i]['category'] not in categories:
            categories[data[i]['category']] = 0
        categories[data[i]['category']] = categories[data[i]['category']] + 1

    for cat in categories:
        print(f'{cat}: {categories[cat]}件')
    print('=' * 50)

# メイン処理
if __name__ == '__main__':
    # テストデータ
    test_data = [
        {'id': 1, 'type': 'A', 'value': 150, 'status': 'active'},
        {'id': 2, 'type': 'A', 'value': 80, 'status': 'inactive'},
        {'id': 3, 'type': 'B', 'value': 200, 'status': 'active'},
        {'id': 4, 'type': 'B', 'value': 50, 'status': 'inactive'},
        {'id': 5, 'type': 'A', 'value': 120, 'status': 'inactive'},
        {'id': 6, 'type': 'B', 'value': 180, 'status': 'active'},
    ]

    processed = process_data(test_data)
    stats = calculate_stats(processed)
    print_report(stats, processed)
