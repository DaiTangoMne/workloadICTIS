const spawn = require('child_process').spawn;

const process = spawn('python', ['./py/bridge.py', 'sqlalchemy']);

process.stdout.on('data', data => {
    console.log(data.toString());
})

process.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

process.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});

// function sendToPython() {
//     var { PythonShell } = require('python-shell');
  
//     let options = {
//       mode: 'text',
//     };
  
//     PythonShell.run('./py/main.py', options, function (err, results) {
//       if (err) throw err;
//       console.log('results: ', results);
//     //   result.textContent = results[0];
//     });
// }

// sendToPython()