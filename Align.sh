
#!/bin/bash

mp4_ile_path=$1
#segmented_transcript_file_path=$2

echo "Input file path is "$mp4_file_path
echo "Transient Transcript file path is "$segmented_transcript_file_path

python -m aeneas.tools.execute_task \
	                           $file_path \
				                 transient_transcript.txt \
							                                                        "task_language=eng|os_task_file_format=json|is_text_type=plain" \
														                                                                           /home/nitin/kaldi/egs/aspire/s5/map.json

echo "Alignment Complete"

cat map.json
