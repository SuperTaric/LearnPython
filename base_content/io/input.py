import argparse

parser = argparse.ArgumentParser(description="参数处理")

parser.add_argument("-number", help="输入一个数字")
args = parser.parse_args()
print(f"你输入的number参数是 {args.number}")