#!/bin/bash

export train_cmd="queue.pl"
export decode_cmd="queue.pl --mem 4G"
export mkgraph_cmd="queue.pl --mem 8G"

echo "cmd.sh ran"

export KALDI_ROOT=`pwd`/../../..
export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh
export PATH=$KALDI_ROOT/tools/sctk/bin:$PATH
export LC_ALL=C

echo "path.sh ran"

var1=scp:echo
var2=' '
var3=utterance-id1
var4=$1
var=$var1${var2}$var3${var2}$var4

echo "This is var"$var

cat << EOF | sh

online2-wav-nnet3-latgen-faster \
	  --online=false \
	    --do-endpointing=false \
	      --frame-subsampling-factor=3 \
	        --config=exp/tdnn_7b_chain_online/conf/online.conf \
		  --max-active=7000 \
		    --beam=15.0 \
		      --lattice-beam=6.0 \
		        --acoustic-scale=1.0 \
			  --word-symbol-table=exp/tdnn_7b_chain_online/graph_pp/words.txt \
			    exp/tdnn_7b_chain_online/final.mdl \
			      exp/tdnn_7b_chain_online/graph_pp/HCLG.fst \
			        'ark:echo utterance-id1 utterance-id1|' \
				  '$var|' \
				    'ark:/dev/null' > transcript1.txt 2>&1 

EOF

grep -E -v "LOG \(online2-wav-nnet3-latgen-faster|online2-wav-nnet3-latgen-faster|EOF" transcript1.txt > finalfinal.txt

echo "Transcript Generated"
cat finalfinal.txt | tr ' ' '\n' > transcript.txt

echo "Permission granted for Reading finalfinal"

python -m aeneas.tools.execute_task \
	            ../../../../audio/Change_the_World.mp4 \
		                transcript.txt \
				                    "task_language=eng|os_task_file_format=json|is_text_type=plain" \
						                            ../../../../audio/map.json

echo "Alignment Complete"

cat ../../../../audio/map.json










