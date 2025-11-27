function direnv_init_pixi
    echo -e 'watch_file pixi.lock\neval "$(pixi shell-hook)"' > .envrc
    direnv allow
end

if status is-interactive
	set -x EDITOR nvim
end

direnv hook fish | source
