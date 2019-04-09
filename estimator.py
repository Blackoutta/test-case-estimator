import yaml
import sys

if len(sys.argv) == 1:
    print("使用方法1：$ python estimator.py <路径/文件名> <路径/文件名2>... (估算指定路径下指定yaml文件中的测试用例数量)")
    print("使用方法2(推荐)：$ python estimator.py */*.yaml (估算当前路径下，所有文件夹下中的yaml文件中的测试用例数量)")
    sys.exit(1)


total = 0
for i in sys.argv[1:]:
    with open(i, 'rb') as stream:
        try:
            tc_list = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    tc_num = 0

    def extract_value(dict):
        for value in dict.values():
            if isinstance(value, list):
                global tc_num
                tc_num += len(value)
            else:
                extract_value(value)

    extract_value(tc_list)
    print("{}: {:>5}".format(i[:-5], tc_num))
    total += tc_num

print("\n总测试用例数量估算：{}".format(total))