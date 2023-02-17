<script>
    const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const path = require('path');

app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'projects')));

// Connect to the MongoDB database
mongoose.connect('', { useNewUrlParser: true });

// Define the schema for the data to be stored
const dataSchema = new mongoose.Schema({
  name: String,
  value: String
});

// Create a model based on the schema
const Data = mongoose.model('Data', dataSchema);

// Endpoint for storing data
app.post('/storeData', (req, res) => {
  const newData = new Data({
    name: req.body.name,
    value: req.body.value
  });
  newData.save((err, data) => {
    if (err) {
      res.send(err);
    } else {
      res.send(data);
    }
  });
});

// Endpoint for displaying the form
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'project', 'test.html'));
});

// Endpoint for displaying data stored in the back end
app.get('/data', (req, res) => {
  Data.find((err, data) => {
    if (err) {
      res.send(err);
    } else {
      res.send(data);
    }
  });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
</script>