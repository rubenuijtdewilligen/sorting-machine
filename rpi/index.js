const express = require("express");
const { spawn } = require("child_process");

const app = express();

app.get("/trigger", (req, res) => {
  const pythonScript = spawn("python3", ["main.py"]);

  pythonScript.stdout.on("data", (data) => {
    console.log(data);
  });

  pythonScript.stderr.on("data", (data) => {
    console.log(data);
  });

  pythonScript.on("close", async (data) => {
    res.send("done");
  });
});

const PORT = 3000 || process.env.PORT;
app.listen(PORT, () => console.log("Listening on port " + PORT));
