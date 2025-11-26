return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  config = function()
    local configs = require("nvim-treesitter.configs")

    configs.setup({
      ensure_installed = { "c", "cpp", "python", "lua", "vim", "vimdoc", "markdown", "rust", "verilog" },
      sync_install = false,
      auto_install = true,
      highlight = { enable = true },
      indent = { enable = true },
      incremental_selection = {
        enable = true,
        keymaps = {
          init_selection = "gsn",
          node_incremental = "gsn",
          scope_incremental = false,
          node_decremental = "gsp",
        },
      },
    })
  end
}
