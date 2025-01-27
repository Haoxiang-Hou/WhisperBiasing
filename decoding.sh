# . /home/gs534/rds/hpc-work/work/espnet/tools/anaconda/etc/profile.d/conda.sh && conda deactivate && conda activate espnet
expdir=exp/finetune_large_librispeech_lr0.0005_KB100_drop0.3
# exp/finetune_librispeech_lr0.0005_KB200_drop0.1
testset=other
maxKBlen=10
beamsize=50

for testset in clean other; do
    for maxKBlen in 10 50 100 200 1000; do
        for beamsize in 10; do

            decodedir=decode_no_lm_beamsize${beamsize}_KB${maxKBlen}_${testset}_50best
            mkdir -p $expdir/$decodedir
            echo python decode.py --test_json data/LibriSpeech/data_json/test_${testset}_full.json --beamsize $beamsize --eval_batch_size 1 --expdir $expdir/$decodedir --loadfrom $expdir/model.acc.best --biasing --biasinglist data/LibriSpeech/Blist/all_rare_words.txt --dropentry 0.0 --maxKBlen ${maxKBlen} --save_nbest 
                # --use_gpt2 \
                # --lm_weight 0.01 \
                # --ilm_weight 0.005 \

            python decode.py \
                --test_json data/LibriSpeech/data_json/test_${testset}_full.json \
                --beamsize $beamsize \
                --eval_batch_size 1 \
                --expdir $expdir/$decodedir \
                --loadfrom $expdir/model.acc.best \
                --biasing \
                --biasinglist data/LibriSpeech/Blist/all_rare_words.txt \
                --dropentry 0.0 \
                --maxKBlen ${maxKBlen} \
                --save_nbest \
                # --use_gpt2 \
                # --lm_weight 0.01 \
                # --ilm_weight 0.005 \

            wait
        done
    done
done
