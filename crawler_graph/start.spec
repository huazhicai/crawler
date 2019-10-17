# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
setup_dir = 'E:\\PycharmProjects\\crawler\\crawler\\crawler_graph\\'
runtime = setup_dir + 'runtime\\'
actions = setup_dir + 'actions\\'

a = Analysis(['start.py',
                runtime+'Action.py',
                runtime+'ActionIO.py',
                runtime+'Runtime.py',
                actions+'DataOutput.py',
                actions+'DataProcess.py',
                actions+'Exclusive.py',
                actions+'FlowControl.py',
                actions+'Others.py',
                actions+'Pageoperate.py',
                actions+'ParsePage.py',
                actions+'Request.py',],
             pathex=['E:\\PycharmProjects\\crawler\\crawler\\crawler_graph'],
             binaries=[],
             datas=[(setup_dir+'actions', 'actions'), (setup_dir+'runtime', 'runtime'),
                (setup_dir+'his.txt', '.')],
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
          name='start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='start')
