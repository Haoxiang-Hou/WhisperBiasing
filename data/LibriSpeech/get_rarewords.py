import sys, os
import json
import tqdm


setname = "test_other"
# Blist_path = "Blist/rareword_error.txt"
Blist_path = "Blist/all_rare_words.txt"

with open("data_json/{}.json".format(setname)) as fin:
    data = json.load(fin)

with open(Blist_path) as fin:
    rarewords = [word.strip() for word in fin]

for uttname, utt in tqdm.tqdm(data.items()):
    uttKB = []
    for word in utt["words"].split():
        if word in rarewords and word not in uttKB:
            uttKB.append(word)
    data[uttname]["blist"] = uttKB

with open("data_json/{}_full.json".format(setname), "w") as fout:
    json.dump(data, fout, indent=4)
