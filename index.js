const { app, BrowserWindow, Menu } = require("electron");
const { ipcRenderer } = require("electron");
// for fast startup you should disable  this option
// this is just from devlopping purposes only adv : hot reload neg : slow startup loading
// try {
//   require('electron-reloader')(module)
// } catch (_) {}

const createWindow = () => {
    const win = new BrowserWindow({
        width: 630,
        height: 980,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
        },
    });

    win.loadFile("index.html");
};
Menu.setApplicationMenu(null);

app.whenReady().then(() => {
    createWindow();
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") app.quit();
});