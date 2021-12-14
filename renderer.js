function sendToPython() {

    var python = require('child_process').spawn('python', ['./Engine/runner.py', document.getElementById("fileuploaded").files[0].path, document.getElementById("one").value]);
    var sucess = document.getElementById("Result")
    if (sucess.style.visibility = "visible") {
        sucess.style.visibility = "hidden"
    }
    document.getElementById("loader").style.visibility = "visible";

    python.stdout.on('data', function(data) {



        // console.log("Python response: ", data.toString('utf8'));
        console.log(data.toString("utf8"))
        var Success = "report generated successfully"
        if (data.toString("utf8").trim() == Success.trim()) {
            document.getElementById("Result").style.visibility = "visible";
            document.getElementById("Success").innerHTML = Success + " As GeneratedOutput.xlsx";
        } else if (data.toString("utf8").trim() == "Day is not existed ...".trim()) {
            alert(data.toString("utf8"))
        } else {
            alert(data.toString("utf8"))
        }

        // result.textContent = data.toString('utf8');


    });

    python.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);

    });

    python.on('close', (code) => {
        // console.log(`child process exited with code ${code}`);
        document.getElementById("loader").style.visibility = "hidden";
        // require('child_process').exec(`explorer.exe "${winPath}"`);
        ;


    });

}

btn.addEventListener('click', () => {

    sendToPython();

});

btn.dispatchEvent(new Event('click'));




function Openoutput() {
    const { shell } = require('electron') // deconstructing assignment
    shell.openPath("C:/Users/Hamza/Documents/Automation/") // Open the given file in the desktop's default manner.
}