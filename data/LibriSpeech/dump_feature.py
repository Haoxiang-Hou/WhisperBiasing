import sys, os
import json
import tqdm

import torch
import whisper


setname = "train-clean-100"
tokenizer = whisper.tokenizer.get_tokenizer(True, language="en")

# PATH = "/mnt/nlp01/dataset/SER/espnet_data/librispeech/downloads/LibriSpeech"
PATH = './data/LibriSpeech/LibriSpeech'

features = {}
for speaker in tqdm.tqdm(os.listdir(os.path.join(PATH, setname))):
    print(speaker)
    if speaker == ".complete":
        continue
    spkpath = os.path.join(PATH, setname, speaker)
    for project in os.listdir(spkpath):
        fullpath = os.path.join(spkpath, project)
        with open(os.path.join(fullpath, "{}-{}.trans.txt".format(speaker, project))) as fin:
            for line in fin:
                uttname = line.split()[0]
                # print(uttname)
                utt = " " + ' '.join(line.split()[1:])
                utttokens = tokenizer.encode(utt.lower())
                audiopath = os.path.join(fullpath, "{}.flac".format(uttname))
                dumppath = os.path.join(fullpath, "{}_fbank.pt".format(uttname))
                datapiece = {"fbank": dumppath, "words": utt}
                features[uttname] = datapiece
                
                if os.path.exists(dumppath):
                    continue
                audio = whisper.load_audio(audiopath)
                audio = whisper.pad_or_trim(audio)
                mel = whisper.log_mel_spectrogram(audio)
                torch.save(mel, dumppath)

# with open(setname.replace("-", "_")+".json", "w") as fout:
with open(os.path.join('exp/data_json', setname.replace("-", "_")+".json"), "w") as fout:
    json.dump(features, fout, indent=4)
