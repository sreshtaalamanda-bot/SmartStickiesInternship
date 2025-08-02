const express = require('express');
const cors = require('cors');
const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

app.post('/api/prompt', (req, res) => {
  const { prompt } = req.body;

  const response = {
    category: "respond",
    header: "Responce",
    description: `Generated info based on your prompt: "${prompt}".`,
  };

  res.json(response);
});

app.listen(port, () => {
  console.log(`Mock LLaMA API listening at http://localhost:${port}`);
});
