
import shlex, subprocess

class ADSL_dial (object):

    def __init__(self, uname, pass_, conn_name=u"宽带连接"):
        self._uname = uname
        self._pass = pass_
        self._conn_name = conn_name

    def connect (self, u=None, pass_=None):
        ''' 宽带连接, 如果不提供用户名与密码, 那么将使用初始化时的用户名和密码
        '''
        
        if u and pass_:
            self._uname = u
            self._pass = pass_

        cp = subprocess.Popen(
            shlex.split('rasdial "%s" "%s" "%s"' % (self._conn_name, self._uname, self._pass)),
            stdout = subprocess.PIPE,
            shell = False
            )

        # 等待命令返回
        cp.wait()
        
        if cp.returncode == 0:
            return True

        return cp.returncode

    def disconnect (self):
        ''' 断开宽带连接
        '''
        
        cp = subprocess.Popen(
            shlex.split('rasdial /DISCONNECT'),
            stdout = subprocess.PIPE,
            shell = False
            )

        cp.wait()

        return cp.returncode