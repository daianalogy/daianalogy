#Variables {{{
video_pref="720p"
##scrape 1 video link per channel instead of the default 2
sub_link_count=1
show_thumbnails=1
#}}}

#Functions {{{
external_menu () {
    #use rofi instead of dmenu
    rofi -dmenu -width 1500 -p "$1"
}

FZF_PLAYER="mpv"


