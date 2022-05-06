# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['newfront.py'],
             pathex=['C:\\Users\\Mahmoud\\Desktop'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
a.datas += [('coil3.jpg','C:\\Users\\Mahmoud\\Desktop\\coil3.jpg', 'Data')]
a.datas += [('l.ico','C:\\Users\\Mahmoud\\Desktop\\l.ico', 'Data')]
a.datas += [('large.jpeg','C:\\Users\\Mahmoud\\Desktop\\large.jpeg', 'Data')]
a.datas += [('light.jpg','C:\\Users\\Mahmoud\\Desktop\\light.jpg', 'Data')]
a.datas += [('one.jpg','C:\\Users\\Mahmoud\\Desktop\\one.jpg', 'Data')]
a.datas += [('red2.jpg','C:\\Users\\Mahmoud\\Desktop\\red2.jpg', 'Data')]
a.datas += [('tesla.jpg','C:\\Users\\Mahmoud\\Desktop\\tesla.jpg', 'Data')]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='RLC forcé',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='l.ico')
