# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src/main/main_window.py'],
             pathex=["src"],
             binaries=[],
             datas=[("src\\gui\\db_info_window_ui.py", "gui"),
             ("src\\gui\\tabbed_main_communication_window.py", "gui"),
             ("src\\gui\\save_window_ui.py", "gui")],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='main_window',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
