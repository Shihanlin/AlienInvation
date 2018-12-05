#!python
# -*- coding: utf-8 -*-

# 这个脚本专为pygame优化，使用py2exe打包代码和资源至dist目录
#
# 使用中若有问题，可以留言至：
#  //eyehere.net/2011/python-pygame-novice-professional-py2exe/
#
# 安装需求:
#         python, pygame, py2exe 都应该装上

# 使用方法:
#         1: 修改此文件，指定需要打包的.py和对应数据
#         2: python pygame2exe.py
#         3: 在dist文件夹中，enjoy it~

try:
    from distutils.core import setup
    import py2exe, pygame
    from modulefinder import Module
    import glob, fnmatch
    import sys, os, shutil,time
except ImportError, message:
    raise SystemExit,  "Sorry, you must install py2exe, pygame. %s" % message

# 这个函数是用来判断DLL是否是系统提供的（是的话就不用打包）
origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    # 需要hack一下，freetype和ogg的dll并不是系统DLL
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
        return 0
    return origIsSystemDLL(pathname)
# 把Hack过的函数重新写回去
py2exe.build_exe.isSystemDLL = isSystemDLL

# 这个新的类也是一个Hack，使得pygame的默认字体会被拷贝
'''
class pygame2exe(py2exe.build_exe.py2exe):
    def copy_extensions(self, extensions):
        # 获得pygame默认字体
        #pygamedir = os.path.split(pygame.base.__file__)[0]
        #pygame_default_font = os.path.join(pygamedir, pygame.font.get_default_font())
        # 加入拷贝文件列表
        extensions.append(Module("pygame.font", r"D:\Program Files\Sublime Text 3\practice\Alien_Invasion_new\arial.ttf"))
        py2exe.build_exe.py2exe.copy_extensions(self, extensions)
'''

# 这个类是我们真正做事情的部分
class BuildExe:
    def __init__(self):
        #------------------------------------------------------#
        ##### 对于一个新的游戏程序，需要修改这里的各个参数 #####
        #------------------------------------------------------#

        # 起始py文件
        self.script = "alien_invasion.py"
        # 游戏名
        self.project_name = "Alien_Invasion"
        # 游戏site
        self.project_url = "about:none"
        # 游戏版本
        self.project_version = "1.0"
        # 游戏许可
        self.license = "MyGames License"
        # 游戏作者
        self.author_name = "Robert"
        # 联系电邮
        self.author_email = "nj_shihanlin@126.com"
        # 游戏版权
        self.copyright = "Copyright (c) 3000 xishui."
        # 游戏描述
        self.project_description = "Alien_Invasion Description"
        # 游戏图标(None的话使用pygame的默认图标)
        self.icon_file = None
        # 额外需要拷贝的文件、文件夹(图片，音频等)
        self.extra_files = [ ("images",["images/alien.png","images/ship.png","images/stars3.jpg","images/ship_icon.bmp"]),
                ("Muisc",["Muisc/Aliens_Boom.wav","Muisc/Escala-Escala-Palladio-128.mp3","Muisc/Ship_Boom.wav"])
              ]
        # 额外需要的python库名
        self.extra_modules = []
        # 需要排除的python库
        self.exclude_modules = [
                                'email',
                                'AppKit',
                                'Foundation',
                                'bdb',
                                'difflib',
                                'tcl',
                                'Tkinter',
                                'Tkconstants',
                                'curses',
                                'distutils',
                                'setuptools',
                                'urllib',
                                'urllib2',
                                'urlparse',
                                'BaseHTTPServer',
                                '_LWPCookieJar',
                                '_MozillaCookieJar',
                                'ftplib',
                                'gopherlib',
                                '_ssl',
                                'htmllib',
                                'httplib',
                                'mimetools',
                                'mimetypes',
                                'rfc822',
                                'tty',
                                'webbrowser',
                                'socket',
                                'base64',
                                'compiler',
                                'pydoc']
        # 额外需要排除的dll
        self.exclude_dll = []
        # 需要加入的py文件
        self.extra_scripts = ['encodings',"encodings.utf_8"]
        # 打包Zip文件名(None的话，打包到exe文件中)
        self.zipfile_name = None
        # 生成文件夹
        self.dist_dir ='dist'

    def opj(self, *args):
        path = os.path.join(*args)
        return os.path.normpath(path)

    def find_data_files(self, srcdir, *wildcards, **kw):
        # 从源文件夹内获取文件
        def walk_helper(arg, dirname, files):
            # 当然你使用其他的版本控制工具什么的，也可以加进来
            if '.svn' in dirname:
                return
            names = []
            lst, wildcards = arg
            for wc in wildcards:
                wc_name = self.opj(dirname, wc)
                for f in files:
                    filename = self.opj(dirname, f)

                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
            if names:
                lst.append( (dirname, names ) )

        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
            os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
            walk_helper((file_list, wildcards),
                        srcdir,
                        [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])
        return file_list

    def run(self):
        if os.path.isdir(self.dist_dir): # 删除上次的生成结果
            shutil.rmtree(self.dist_dir)

        # 获得默认图标
        if self.icon_file == None:
            path = os.path.split(pygame.__file__)[0]
            self.icon_file = os.path.join(path, 'pygame.ico')


        # 开始打包exe
        setup(
 #           cmdclass = {'py2exe': pygame2exe},
            version = self.project_version,
            description = self.project_description,
            name = self.project_name,
            url = self.project_url,
            author = self.author_name,
            author_email = self.author_email,
            license = self.license,

            # 默认生成窗口程序，如果需要生成终端程序(debug阶段)，使用：
            # console = [{
            windows = [{
                'script': self.script,
                'icon_resources': [(0, self.icon_file)],
                'copyright': self.copyright
            }],
            options = {'py2exe': {'optimize': 2, 'bundle_files': 3,
                                  'compressed': True,
                                  'excludes': self.exclude_modules,
                                  'packages': self.extra_modules,
                                  'dist_dir': self.dist_dir,
                                  'dll_excludes': self.exclude_dll,
                                  'includes': self.extra_scripts} },
            #zipfile = self.zipfile_name,
            data_files = self.extra_files,
            zipfile = None
            )

        if os.path.isdir('build'): # 清除build文件夹
            shutil.rmtree('build')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.argv.append('py2exe')
    BuildExe().run() #Run generation
    raw_input("Press any key to continue") #Pause to let user see that things ends