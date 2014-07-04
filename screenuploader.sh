#!/usr/bin/env bash

path="__WATCH_PATH__"
site="__URL_PREFIX__"
server="__SERVER_NAME__"
dir="__SERVER_DIR__"

if [[ $# == 1 ]]; then
    scp "$1" $server:$dir
    ssh $server "chmod o+r \"$dir/$(basename "$1")\""
    rm "$1"
    echo "$site/$(basename "$1" | sed 's/ /%20/g')" | pbcopy
    /usr/local/bin/terminal-notifier -message "uploaded $(basename $1)" -title screenuploader
else
    file=$(find $path -name "Screen Shot *" -mmin -1 | tail -1)
    if [[ "$file" != "" ]]; then
        /usr/local/bin/terminal-notifier -message "click to upload $(basename $file)" -title screenuploader -execute "$0 \"$file\""
    fi
fi

    

