from testcase_nll.file_e import send_email
from testcase_nll.file_t import get_type_file


def main():
    filelist = get_type_file()
    send_email(filelist)


main()