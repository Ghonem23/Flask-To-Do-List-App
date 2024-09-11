const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const path = require('path');

let mainWindow;
let flaskProcess; // Define flaskProcess globally so we can terminate it later

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    // Start the Flask server (handle both python and python3 depending on the system)
    flaskProcess = exec('python app.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error starting Flask: ${error}`);
            return;
        }
        if (stderr) {
            console.error(`Flask error: ${stderr}`);
        }
        console.log(`Flask output: ${stdout}`);
    });

    // Load the Flask app URL in the Electron window
    mainWindow.loadURL('http://127.0.0.1:5000');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

// Close Flask process when Electron quits
app.on('before-quit', () => {
    if (flaskProcess) {
        flaskProcess.kill(); // Kill the Flask process when Electron quits
    }
});

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    }
});