#!/bin/bash

file_path=/home/nitin/kaldi/egs/aspire/s5/brightcove/$1.mp4

echo "Input file path is "$file_path
cat saperated_text.txt



python -m aeneas.tools.execute_task \
	                                   $file_path \
					                                                  saperated_text.txt \
											                                                                                                                  "task_language=eng|os_task_file_format=json|is_text_type=plain" \
																									                                                                                                                                                                                             map.json

echo "Alignment Complete"
echo "$(pwd)"

cat map.json
