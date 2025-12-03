set -g fish_greeting

alias sdecman="sudo decman"

alias cedit="cd ~/dots && nvim"
alias cstatus="cd ~/dots && git status && cd -"
alias cpush="cd ~/dots && git add --all && git commit -m 'update' && git push && cd -"
alias cpull="cd ~/dots && git pull && cd -"

alias reflector-update=" sudo reflector --country Germany --latest 5 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist"


function direnv_init_pixi
    echo -e 'watch_file pixi.lock\neval "$(pixi shell-hook)"' > .envrc
    direnv allow
end

function y
	set tmp (mktemp -t "yazi-cwd.XXXXXX")
	yazi $argv --cwd-file="$tmp"
	if read -z cwd < "$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
		builtin cd -- "$cwd"
	end
	rm -f -- "$tmp"
end

if status is-interactive
	set -x EDITOR nvim

    direnv hook fish | source
    starship init fish | source
end
