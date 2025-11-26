local wk = require("which-key")

wk.add({
  -- buffers 
  { "H", "<cmd>bp<cr>", desc = "Previous buffer", mode = "n" },
  { "L", "<cmd>bn<cr>", desc = "Next buffer", mode = "n" },
  { "<leader>x", function() Snacks.bufdelete() end, desc = "Delete Buffer" },

   -- top pickers & explorer
  { "<leader>e", function() Snacks.explorer() end, desc = "File Explorer" },
  { "<leader>n", function() Snacks.picker.notifications() end, desc = "Notification History" },

  -- find
  { "<leader>f", group = "Find" },
  { "<leader>fb", function() Snacks.picker.buffers() end, desc = "Buffers" },
  { "<leader>fc", function() Snacks.picker.files({ cwd = vim.fn.stdpath("config") }) end, desc = "Find Config File" },
  { "<leader>ff", function() Snacks.picker.files() end, desc = "Find Files" },
  { "<leader>fg", function() Snacks.picker.git_files() end, desc = "Find Git Files" },
  { "<leader>fr", function() Snacks.picker.recent() end, desc = "Recent" },

  -- git
  { "<leader>g", group = "Git" },
  { "<leader>gg", function() Snacks.lazygit() end, desc = "Lazygit" },
  { "<leader>gb", function() Snacks.picker.git_branches() end, desc = "Git Branches" },
  { "<leader>gl", function() Snacks.picker.git_log() end, desc = "Git Log" },
  { "<leader>gL", function() Snacks.picker.git_log_line() end, desc = "Git Log Line" },
  { "<leader>gs", function() Snacks.picker.git_status() end, desc = "Git Status" },
  { "<leader>gS", function() Snacks.picker.git_stash() end, desc = "Git Stash" },
  { "<leader>gd", function() Snacks.picker.git_diff() end, desc = "Git Diff (Hunks)" },
  { "<leader>gf", function() Snacks.picker.git_log_file() end, desc = "Git Log File" },
  { "<leader>gR", function() Snacks.gitbrowse.open() end, desc = "Open Repository Page" },

  -- search
  { "<leader>s", group = "Search" },
  { "<leader>sb", function() Snacks.picker.lines() end, desc = "Buffer Lines" },
  { "<leader>sB", function() Snacks.picker.grep_buffers() end, desc = "Grep Open Buffers" },
  { "<leader>sg", function() Snacks.picker.grep() end, desc = "Grep" },
  { "<leader>sw", function() Snacks.picker.grep_word() end, desc = "Visual selection or word", mode = { "n", "x" } },
  { '<leader>s/', function() Snacks.picker.search_history() end, desc = "Search History" },
  { "<leader>sc", function() Snacks.picker.commands() end, desc = "Commands" },
  { "<leader>sd", function() Snacks.picker.diagnostics() end, desc = "Diagnostics" },
  { "<leader>sD", function() Snacks.picker.diagnostics_buffer() end, desc = "Buffer Diagnostics" },
  { "<leader>sh", function() Snacks.picker.help() end, desc = "Help Pages" },
  { "<leader>sk", function() Snacks.picker.keymaps() end, desc = "Keymaps" },
  { "<leader>su", function() Snacks.picker.undo() end, desc = "Undo History" },
  { "<leader>sC", function() Snacks.picker.colorschemes() end, desc = "Colorschemes" },

  -- LSP Mappings
  { "<leader>c", group = "LSP" },
  { "<leader>cf", "<cmd>lua vim.lsp.buf.format({async = true})<cr>", desc = "Format code" },
  { "<leader>ck", "<cmd>lua vim.lsp.buf.hover()<cr>", desc = "Hover Info" },
  { "<leader>cd", "<cmd>lua vim.lsp.buf.definition()<cr>", desc = "Go to definition" },
  { "<leader>cD", "<cmd>lua vim.lsp.buf.declaration()<cr>", desc = "Go to declaration" },
  { "<leader>cr", "<cmd>lua vim.lsp.buf.references()<cr>", desc = "Find references" },
  { "<leader>cs", "<cmd>lua vim.lsp.buf.signature_help()<cr>", desc = "Signature help" },
  { "<leader>cR", "<cmd>lua vim.lsp.buf.rename()<cr>", desc = "Rename" },
  { "<leader>ca", "<cmd>lua vim.lsp.buf.code_action()<cr>", desc = "Code actions" },
  { "<leader>ct", "<cmd>lua vim.diagnostic.open_float()<CR>", desc = "Show line diagnostics" },
})
