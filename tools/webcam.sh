#!/usr/bin/env bash

<< 'MULTILINE-COMMENT'

Dependencía necesaria para ejecutar éste script: mplayer

Debian: sudo apt install mplayer
Arch: pacman -S mplayer
Void: sudo xbps-install -S mplayer


MULTILINE-COMMENT


if
	which mplayer &>/dev/null; then
		MPLAYER=$(which mplayer)
else
	echo "MPLAYER no funciona."
	exit 1
fi

$MPLAYER tv:///dev/video0 &>/dev/null
