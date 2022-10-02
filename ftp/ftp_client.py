from ftplib import FTP
import os

host = "192.168.1.235"
username = "mzy"
password = "123"
port = 21

remote_file_path = "/"   # FTP server
local_file_path = "ftp"  # local


class FTP_OP(object):
    def __init__(self, host, username, password, port):
        self.buffer_size = 102400  # default 8192
        # connect to ftp
        _ftp = FTP()
        _ftp.set_debuglevel(1)              # turn off debug mode
        _ftp.connect(host=host, port=port)  # connect to ftp
        _ftp.login(username, password)      # login ftp
        _ftp.set_pasv(False)
        self.ftp = _ftp

    def download_file(self, remote_file_path, local_file_path, selected_files=[]):
        """
        download all files in directory
        :param remote_file_path:
        :param local_file_path:
        :param selected_files:  if no files selected, download all files
        :return:
        """
        file_list = self.ftp.nlst(remote_file_path)  # read ftp directory
        print("-" * 20)
        for file_name in file_list:
            if file_name not in selected_files or len(selected_files) == 0:
                continue
            else:
                ftp_file = os.path.join(remote_file_path, file_name)
                write_file = local_file_path + file_name
                with open(write_file, "wb") as f:
                    self.ftp.retrbinary('RETR {}'.format(ftp_file), f.write, self.buffer_size)

        self.ftp.quit()

    def upload_file()
        pass


if __name__ == '__main__':
    if not os.path.exists(remote_file_path):
        os.mkdir(local_file_path)
    ftp = FTP_OP(host=host, username=username, password=password, port=port)
    ftp.download_file(remote_file_path=remote_file_path, local_file_path=local_file_path)
