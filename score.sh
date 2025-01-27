expdir=$1
# /home/gs534/rds/hpc-work/work/espnet/tools/sctk/bin/sclite -r $expdir/ref.wrd.trn trn -h $expdir/hyp.wrd.trn trn -i rm -o all stdout > $expdir/results.txt
/mnt/nlp01/usr/houhaoxiang/FromQuicksilver/espnet/tools/sctk/bin/sclite -r $expdir/ref.wrd.trn trn -h $expdir/hyp.wrd.trn trn -i rm -o all stdout > $expdir/results.txt

cd error_analysis
python get_error_word_count.py ../$expdir/results.txt
