import os
import sfst
import os

CURR_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

print("SFST version " + sfst.__version__)
sfst.init(os.path.join(CURR_DIR, 'easy.a'))
assert sfst.analyse("easy") == 'easy<ADJ><pos>\n'
assert sfst.generate("easy<ADJ><pos>") == 'easy\n'