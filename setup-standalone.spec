# -*- mode: python -*-

block_cipher = None


a = Analysis(['PyFrontierLiveDPS\\peld.py'],
             pathex=['.\\PyFrontierLiveDPS'],
             binaries=[],
             datas=[('app.ico', '.'), ('.\\PyFrontierLiveDPS\\images\\*.png', 'images'), ('.\\PyFrontierLiveDPS\\images\\*.gif', 'images')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PELD-standalone',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='app.ico')
