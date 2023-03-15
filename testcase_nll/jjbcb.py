import os
import csv

# 这里是设置参数的
# 文件夹路径
class fill():
    dir_path = r'D:\zhaoyu\Test_pythonProject\test_APP\reports/'

    # 接下来开始运行程序
    # 检查文件夹路径是否正常
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        print("文件夹路径异常，请检查文件夹路径是否正确！！！")
        exit()


    # 获取文件列表方法
    def get_list_file(temp_path, temp_report):
        temp_dir_list = os.listdir(temp_path)
        for temp_one in temp_dir_list:
            temp_path_now = os.path.join(temp_path, temp_one)
            if os.path.isfile(temp_path_now):
                temp_report.append(temp_path_now)
            if os.path.isdir(temp_path_now):
                temp_report.append(temp_path_now)
                temp_path.get_list_file(temp_path_now, temp_report)


    # 获取文件列表
    report_file_list = []
    get_list_file(dir_path, report_file_list)
    print(str(report_file_list)[1:-1])
    # 结果保存为txt文件
    # text_file = open(dir_path + '测试报告.text', mode='w+')
    # for temp_one in report_file_list:
    #     text_file.write(temp_one + '\n')
    # text_file.close()
    # 结果保存为csv文件
    csv_file = open(dir_path + '测试报告.text', 'w')
    with csv_file:
        temp_writer = csv.writer(csv_file)
        for temp_one in report_file_list:
            temp_writer.writerow(temp_one.replace(dir_path, "").split("\\"))
    # 结束
    print("提取文件名列表结束，结果保存在" + dir_path + '测试报告' + "【共" + str(len(report_file_list)) + "项】")


