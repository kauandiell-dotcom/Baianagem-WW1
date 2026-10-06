p = 'C:/Users/Usuário/Pictures/Baianagem-WW1/_scratch_uk45/fix_picks.py'
s = open(p, encoding='utf-8').read()
s = s.replace('[("holding_the_continental_line", 5)]', '[("holding_the_continental_line", 5), ("holding_the_continental_line", 7), ("holding_the_continental_line", 8)]')
s = s.replace('("bristol_scout_trials", 1), ("fighter_squadron_instruction", 6)]', '("bristol_scout_trials", 1), ("fighter_squadron_instruction", 7), ("fighter_squadron_instruction", 8), ("the_air_battalion_experiments", 0)]')
s = s.replace(', "demobilisation": [("demob_a", 0)]', '')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
