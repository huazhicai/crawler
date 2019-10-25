# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
SETUP_DIR = 'E:\\PycharmProjects\\crawler\\crawler\\editor\\'

a = Analysis(['main.py', 'widgets.py', 'mutil.py'],
             pathex=['E:\\PycharmProjects\\crawler\\crawler\\editor'],
             binaries=[],
             datas=[(SETUP_DIR+'meta', 'meta'), (SETUP_DIR+'images', 'images'), (SETUP_DIR+'graph', 'graph'),
             (SETUP_DIR+'font', 'font')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
