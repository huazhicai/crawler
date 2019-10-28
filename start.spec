# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
base_dir = 'E:\\PycharmProjects\\crawler\\crawler\\'

a = Analysis(['start.py',
                base_dir+'editor\\main.py',
                base_dir+'editor\\widgets.py',
                base_dir+'editor\\util.py',
                base_dir+'editor\\mutil.py',
                base_dir+'editor\\logger.py',
                base_dir+'editor\\ActivityScriptExporter.py',
                base_dir+'editor\\graphics.py',

                base_dir+'crawler_graph\\run.py',
                base_dir+'crawler_graph\\actions\\DataOutput.py',
                base_dir+'crawler_graph\\actions\\Others.py',
                base_dir+'crawler_graph\\actions\\Request.py',
                base_dir+'crawler_graph\\actions\\ParsePage.py'],
             pathex=['E:\\PycharmProjects\\crawler\\crawler'],
             binaries=[],
             datas=[(base_dir+ 'editor\\meta', 'meta'), (base_dir+ 'editor\\graph', 'graph'),
             (base_dir+ 'editor\\font', 'font'), (base_dir+ 'editor\\images', 'images'),
              (base_dir+ 'editor', 'editor'),(base_dir+'crawler_graph', 'crawler_graph'),
             (base_dir+'his.json', '.')],
             hiddenimports=['widgets'],
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
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='start')