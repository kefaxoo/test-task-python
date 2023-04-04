import requests
from collections import Counter

def main():
    response = requests.get("https://python.org")
    text = response.text
    counter = Counter(text)
    output = "|Symbol|Count|\n|--|--|\n"
    for symbol, count in counter.most_common():
        if symbol == "|":
            symbol = "\|"

        output += f"| {symbol} | {count} |\n"


    print(output)
    file_md = open("README.md", "w", encoding="utf-8")
    file_md.write(output)

if __name__ == "__main__":
    main()