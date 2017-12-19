now="$(date +'%Y-%m-%d')"
file="./_posts/$now-$1.md"
touch $file
/bin/cat <<EOM >$file
---
layout: post
title: ""
category: 
tags: []
---
EOM