import paramiko


class Client:
    def __init__(self, name):
        self.name = name
        self.Host = '3.13.31.198'
        self.UserName = 'ubuntu'
        self.KeyPath = 'BOB-MUZE.pem'

        self.SSH = paramiko.SSHClient()
        self.SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.Conn = self.SSH.connect(hostname=self.Host,
                                     username=self.UserName,
                                     key_filename=self.KeyPath,
                                     allow_agent=False,
                                     look_for_keys=False)

        self.sftp = self.SSH.open_sftp()

    def shell(self, cmd):
        stdin, stdout, stderr = self.SSH.exec_command(cmd)
        return stdin, stdout, stderr

    def file_upload(self, filename, path):
        self.sftp.put(filename, path)

    def close(self):
        self.sftp.close()
        self.SSH.close()


if __name__ == '__main__':
    client = Client('naver_pre')
