#!/bin/zsh

find ./ -type f -name "*.sh" -exec basename {} \; | sed 's/\.sh/\\/' | sed 's/_/\\_/'
