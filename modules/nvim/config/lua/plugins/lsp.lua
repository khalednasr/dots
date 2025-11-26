return {
    {
        "mason-org/mason-lspconfig.nvim",
        opts = {
            ensure_installed = {
                "rust_analyzer",
                "pylsp",
                "lua_ls",
            },
        },
        dependencies = {
            { "mason-org/mason.nvim", opts = {} },
            "neovim/nvim-lspconfig",
        },
    },
    {
        "neovim/nvim-lspconfig",
        dependencies = { "mason-org/mason.nvim" },
        config = function()
            vim.lsp.config('pylsp', {
                settings = {
                    pylsp = {
                        plugins = {
                            pycodestyle = {
                                ignore = {"E302"},
                                maxLineLength = 120
                            }
                        },
                    }
                }
            })
        end
    },
    {
        'saghen/blink.cmp',
        dependencies = { 'rafamadriz/friendly-snippets' },
        version = '1.*',
        ---@module 'blink.cmp'
        ---@type blink.cmp.Config
        opts = {
            keymap = { preset = 'default' },

            appearance = {
                nerd_font_variant = 'mono'
            },

            completion = { documentation = { auto_show = false } },

            sources = {
                default = { 'lsp', 'path', 'snippets', 'buffer' },
            },

            fuzzy = { implementation = "prefer_rust_with_warning" }
        },
        opts_extend = { "sources.default" }
    }
}
