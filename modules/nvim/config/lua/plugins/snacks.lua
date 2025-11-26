return {
  {
    "folke/snacks.nvim",
    priority = 1000,
    lazy = false,
    opts = {
      dashboard = { enabled = true },
      explorer = { enabled = true },
      picker = {
        enabled = true,
        sources = {
          explorer = {
            enabled = true,
            jump = {
              close = true,
            },
            layout = {
              preset = "default",
            },
          },
        },
      },
      indent = { enabled = true },
      input = { enabled = true },
      notifier = { enabled = true },
      bigfile = { enabled = true },
      quickfile = { enabled = true },
      scroll = { enabled = true },
      statuscolumn = { enabled = true },
      bufdelete = { enabled = true },
      git = { enabled = true },
      lazygit = { enabled = true },
      gitbrowse = { enabled = true },
    },
  },
}
