#!/bin/bash

file_path=/home/nitin/kaldi/egs/aspire/s5/brightcove/$1.mp4

echo "Input file path is "$file_path

python -m aeneas.tools.execute_task \
	                           $file_path \
				               ${1}_transcript.txt \
							                                                        "task_language=eng|os_task_file_format=json|is_text_type=plain" \
														                                                                            map.json

echo "Alignment Complete"

cat map.json
