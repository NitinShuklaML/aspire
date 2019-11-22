#!/bin/bash

file_path=$(pwd)/$1.mp4

echo "Input file path is "$file_path

python -m aeneas.tools.execute_task \
	                           $file_path \
				               ${1}_saperated_text.txt \
							                                                        "task_language=eng|os_task_file_format=json|is_text_type=plain" \
														                                                                           $1_map.json

echo "Alignment Complete"

#cat $1_map.json
