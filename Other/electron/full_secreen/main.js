const { app, BrowserWindow } = require('electron')
const { screen } = require('electron')


function createWindow () {
  // Create the browser window.
  
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  
  });

//kiosk mode

 win.fullScreen=true;
 win.autoHideMenuBar=true;
 win.kiosk=true;

win.loadURL('http://google.com');





  // and load the index.html of the app.
  
}

app.whenReady().then(createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})







function closeWindow(){
  console.log("abc");
  win.close()
}

