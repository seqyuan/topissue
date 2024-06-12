#!/bin/sh -l
python /get_latest_issue.py $1 $2

if [ -f "./output_context.sh" ];then
	sh ./output_context.sh
fi
