# EN: Tests: key sources, decoded file up to date, known words present, calibration figure.
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

from decode import load_key, load_lines, decode  # noqa: E402


class TestDecode(unittest.TestCase):
    def setUp(self):
        self.key, self.src = load_key(os.path.join(ROOT, 'data', 'key.tsv'))
        self.lines = dict(load_lines(os.path.join(ROOT, 'data', 'transcription_f50.txt')))

    def test_key_sources(self):
        # source は T・S・X・C の組み合わせ
        for s in self.src.values():
            self.assertTrue(set(s.split(',')) <= {'T', 'S', 'X', 'C'}, s)

    def test_decoded_file_is_current(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'decode.py'),
                              os.path.join(ROOT, 'data', 'key.tsv'),
                              os.path.join(ROOT, 'data', 'transcription_f50.txt')],
                             capture_output=True, text=True, check=True).stdout
        with open(os.path.join(ROOT, 'data', 'decoded_f50.txt'), encoding='utf-8') as f:
            self.assertEqual(out, f.read())

    def test_known_words(self):
        d = {k: decode(v, self.key) for k, v in self.lines.items()}
        self.assertIn('detoutce', d['r08'])            # de tout ce
        self.assertIn('paquets', d['v01'])
        self.assertIn('la Reyne', d['v06'])
        self.assertIn('Monsieur le Mareschal de La Motte', d['r06'])

    def test_calibration(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'calib.py'),
                              os.path.join(ROOT, 'calib', 'f171r_reading.txt'),
                              os.path.join(ROOT, 'calib', 'f172r_ref.txt')],
                             capture_output=True, text=True, check=True).stdout
        self.assertIn('# matched 337/360', out)


    def test_sign_accuracy(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'score_signs.py'),
                              os.path.join(ROOT, 'data', 'key.tsv'),
                              os.path.join(ROOT, 'calib', 'f171r_tx.txt'),
                              os.path.join(ROOT, 'calib', 'f172r_ref.txt')],
                             capture_output=True, text=True, check=True).stdout
        self.assertIn('matched 253', out)

    def test_open_items(self):
        # README の「9か所」と docs/OPEN.md の表の行数がそろう
        with open(os.path.join(ROOT, 'docs', 'OPEN.md'), encoding='utf-8') as f:
            rows = [l for l in f if l.startswith('| r') or l.startswith('| v')]
        self.assertEqual(len(rows), 9)


    def test_table_check(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'check_table.py'),
                              os.path.join(ROOT, 'data', 'key.tsv'),
                              os.path.join(ROOT, 'data', 'tomokiyo_table_signs.tsv')],
                             capture_output=True, text=True, check=True).stdout
        self.assertIn('main value not in table 0', out)


if __name__ == '__main__':
    unittest.main()
