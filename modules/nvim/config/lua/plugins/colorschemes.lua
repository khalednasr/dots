return {
  {
    "rebelot/kanagawa.nvim",
    priority = 1000,
    config = function()
      require("kanagawa").setup({
        transparent = true,
      })
      -- vim.cmd("colorscheme kanagawa-dragon")
    end,
  },
  {
    "rose-pine/neovim",
    name = "rose-pine",
    config = function()
      -- vim.cmd("colorscheme rose-pine")
    end
  },
  {
    'sainnhe/gruvbox-material',
    lazy = false,
    priority = 1000,
    config = function()
      vim.g.gruvbox_material_enable_italic = true
      vim.g.gruvbox_material_background = "hard"
      vim.g.gruvbox_material_foreground = "original"
      vim.g.gruvbox_material_transparent_background = 2
      vim.cmd.colorscheme('gruvbox-material')
    end
  }
}
