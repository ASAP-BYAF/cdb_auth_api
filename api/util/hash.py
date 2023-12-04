import hashlib

def hash256(word: str) -> str:
    """_summary_

    Args:
        word (str): ハッシュ化したい文字列

    Returns:
        str: 受けっとった他文字列をハッシュ化した文字列
    """
    return hashlib.sha256(word.encode()).hexdigest()
