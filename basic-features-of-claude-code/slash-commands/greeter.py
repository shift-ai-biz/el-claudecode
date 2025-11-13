def say_hello(name):
    """挨拶する"""
    return f"こんにちは、{name}さん！"


def say_goodbye(name):
    """さよならを言う"""
    return f"さようなら、{name}さん！"


def get_greeting(time_of_day):
    """時間帯に応じた挨拶を返す"""
    if time_of_day == "morning":
        return "おはようございます！"
    elif time_of_day == "afternoon":
        return "こんにちは！"
    elif time_of_day == "evening":
        return "こんばんは！"
    else:
        return "やあ！"
