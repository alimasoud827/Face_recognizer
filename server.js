import express from "express"
import cors from "cors"
import { exec } from "child_process"
import { error } from "console"
import { stderr, stdout } from "process"

const app = express()
app.use(cors());

app.get("/", (req, res) => {
  exec("python face_det.py", (error, stdout, stderr ) => {
    if (error){
      return res.status(500).json({ error: "Face detection failed "})
    }
    res.json({ message: stdout });
  })
});

app.listen(5000, () => {
  console.log("✅ Server running on port http://localhost:5000")
});