const { BrowserWindow } = require('electron')

function closeWindow() {
  let win = BrowserWindow.getFocusedWindow()
  win.close()
}