return {
  {
    "mg979/vim-visual-multi",
    event = "VeryLazy",
  },
  {
    "folke/flash.nvim",
    event = "VeryLazy",
    ---@type Flash.Config
    opts = {
      modes = {
        char = {
          enabled = false,
        },
      },
    },
    -- stylua: ignore
    keys = {
      { "f",     mode = { "n", "x", "o" }, function() require("flash").jump() end,              desc = "Flash" },
      { "F",     mode = { "n", "x", "o" }, function() require("flash").treesitter() end,        desc = "Flash Treesitter" },
    },
  },
  {
    'echasnovski/mini.nvim',
    version = false,
    config = function()
      require("mini.ai").setup({})
      require("mini.pairs").setup({})
      require("mini.surround").setup({})
      require("mini.move").setup({
        mappings = {
          -- Move visual selection in Visual mode. Defaults are Alt (Meta) + hjkl.
          left = '<C-h>',
          right = '<C-l>',
          down = '<C-j>',
          up = '<C-k>',

          -- Move current line in Normal mode
          line_left = '<C-h>',
          line_right = '<C-l>',
          line_down = '<C-j>',
          line_up = '<C-k>',
        },

        -- Options which control moving behavior
        options = {
          -- Automatically reindent selection during linewise vertical move
          reindent_linewise = true,
        },
      })
    end
  }

}
