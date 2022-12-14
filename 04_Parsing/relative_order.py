import sys
import matplotlib.pyplot as plt
import pyconll
import pyconll.util

inp1 = './ud-treebanks-v2.11/'

file_names = {'ru': 'UD_Russian-GSD/ru_gsd-ud-train.conllu',
              'grc': 'UD_Ancient_Greek-Perseus/grc_perseus-ud-train.conllu',
              'hbo': 'UD_Ancient_Hebrew-PTNK/hbo_ptnk-ud-train.conllu',
              'ar': 'UD_Arabic-NYUAD/ar_nyuad-ud-train.conllu', 'hy': 'UD_Armenian-ArmTDP/hy_armtdp-ud-train.conllu',
              'eu': 'UD_Basque-BDT/eu_bdt-ud-train.conllu', 'be': 'UD_Belarusian-HSE/be_hse-ud-train.conllu',
              'bg': 'UD_Bulgarian-BTB/bg_btb-ud-train.conllu', 'tr': 'UD_Turkish-IMST/tr_imst-ud-train.conllu',
              'ca': 'UD_Catalan-AnCora/ca_ancora-ud-train.conllu', 'ko': 'UD_Korean-GSD/ko_gsd-ud-train.conllu',
              'ja': 'UD_Japanese-GSD/ja_gsd-ud-train.conllu'}

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # proportion of OV
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # proportion of VO
labels = {0: 'ru', 1: 'grc', 2: 'hbo', 3: 'ar', 4: 'hy', 5: 'eu', 6: 'be',
          7: 'bg', 8: 'tr', 9: 'ca', 10: 'ko', 11: 'ja'}


def find_verb_w_obj(tree):
    v = ''
    o = ''
    if tree.data.upos == "VERB":
        v = tree.data.form
        o = find_obj(tree)
        if o == '':
            v = ''
        else:
            return v, o
    for child in tree:
        next = find_verb_w_obj(child)
        if next != '':
            return next
    return ''


def find_obj(tree):
    if tree.data.deprel == 'obj':
        return tree.data.form
    for child in tree:
        a = find_obj(child)
        if a != '':
            return a
    return ''


for label in labels:
    print(str(label + 1) + '/12')
    curr_code = labels[label]
    file = inp1 + file_names[curr_code]
    train = pyconll.load_from_file(file)
    OV_counter = 0
    VO_counter = 0
    other_count = 0
    tot = 0
    for sentence in train:
        tree = sentence.to_tree()
        out = find_verb_w_obj(tree)
        if out == '':
            continue
        tot += 1
        v = out[0]
        o = out[1]
        for word in sentence:
            if word.form == v:
                VO_counter += 1
                break
            elif word.form == o:
                OV_counter += 1
                break
    x[label] = OV_counter / tot
    y[label] = VO_counter / tot

plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0, 1])  # Set the x and y axis ranges
plt.ylim([0, 1])
plt.xlabel('OV')  # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i] - 0.03, y[i] - 0.03, labels[i], fontsize=9)
plt.savefig(sys.argv[1])
plt.show()
