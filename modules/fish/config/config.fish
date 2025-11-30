set -g fish_greeting

alias sdecman="sudo decman"
alias ce="cd ~/dots && nvim"
alias reflector-update=" sudo reflector --country Germany --latest 5 --protocol http --protocol https --sort rate --save /etc/pacman.d/mirrorlist"


function direnv_init_pixi
    echo -e 'watch_file pixi.lock\neval "$(pixi shell-hook)"' > .envrc
    direnv allow
end

if status is-interactive
	set -x EDITOR nvim

    direnv hook fish | source
    starship init fish | source
end
