import express from "express";
import cors from "cors";
import { exec } from "child_process";
import bodyParser from "body-parser";
import fs from "fs";
import fetch from "node-fetch";

const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("index", { resultImage: null });
});

app.post("/detect", async (req, res) => {
  const imageUrl = req.body.image_url;
  const inputImagePath = "public/input_image.jpg";
  const outputImage = "public/detected_faces.jpg";

  if (!imageUrl.startsWith("http")) {
    return res.send("❌ Invalid URL! Please provide a valid image link.");
  }

  try {
    const response = await fetch(imageUrl);
    if (!response.ok) throw new Error("Failed to fetch image");

    const buffer = await response.buffer();
    fs.writeFileSync(inputImagePath, buffer);
    console.log("✅ Image downloaded:", inputImagePath);

    exec(`python face_det.py "${inputImagePath}" "${outputImage}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`❌ Error: ${stderr}`);
        return res.send("Error processing image.");
      }

      console.log("✅ Face detection complete:", stdout);
      res.render("index", { resultImage: "detected_faces.jpg" });
    });

  } catch (err) {
    console.error("❌ Error downloading image:", err);
    res.send("Failed to download image.");
  }
});

app.listen(5000, () => {
  console.log("✅ Server running on port http://localhost:5000");
});
