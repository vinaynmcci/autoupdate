# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['./src'],
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

a.datas += [('/icons/mcci_logo.ico','./icons/mcci_logo.ico', "DATA")]
a.datas += [('/icons/mcci_logo.png','./icons/mcci_logo.png', "DATA")]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BrixUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='./icons/mcci_logo.icns')
app = BUNDLE(exe,
             name='BrixUI.app',
             icon='./icons/mcci_logo.icns',
             bundle_identifier=None)
