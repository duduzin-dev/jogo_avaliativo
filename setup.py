import cx_Freeze

executables = [cx_Freeze. Executable(script="JogoEducativo.py", icon="imagens/icon.ico")]
cx_Freeze.setup(
    name='Anti_covid_Game',
    options={
        "build_exe": {
        "packages": ["pygame"],
        "include_files":["imagens"]
    }},
    executables = executables
)