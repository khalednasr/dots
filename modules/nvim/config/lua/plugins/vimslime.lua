return {
    {
        "klafyvel/vim-slime-cells",
        dependencies = {
            "jpalardy/vim-slime",
        },
        keys = {
            { "<leader>rc", "<cmd>SlimeConfig<cr>",            desc = "Slime Config" },
            { "<leader>rr", "<Plug>SlimeCellsSendAndGoToNext", desc = "Slime send cell and go to next" },
            { "<leader>rR", "<Plug>SlimeSendCell",             desc = "Slime send cell" },
            { "<leader>rl", "<Plug>SlimeLineSend",             desc = "Slime send line" },
            { "<leader>rm", "<Plug>SlimeMotionSend",           desc = "Slime send motion" },
            { "<leader>rr", ":<C-u>'<,'>SlimeSend<CR>",        mode = "v",                             desc = "Slime send selection" },
            { "<leader>rj", "<Plug>SlimeCellsNext",            desc = "Slime go to next cell" },
            { "<leader>rk", "<Plug>SlimeCellsPrev",            desc = "Slime go to previous cell" },
        },
        config = function()
            vim.g.slime_target = "wezterm"
            vim.g.slime_no_mappings = 1
            vim.g.slime_cell_delimiter = "^\\s*##"
            vim.g.slime_bracketed_paste = 1
        end,
    }
}
