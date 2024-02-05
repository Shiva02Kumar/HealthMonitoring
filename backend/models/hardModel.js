const mongoose = require('mongoose');

const db_link = "mongodb+srv://shiva2002kumar:ckPZR1nHXQEj9N8x@cluster0.wztzexy.mongodb.net/?retryWrites=true&w=majority";
mongoose.connect(db_link)
    .then(function (db) {
        console.log("db connected");
    })
    .catch(function (err) {
        console.log(err);
    })

const hardSchema = mongoose.Schema({
    heart: {
        type: Number,
        require: true
    },
    temp: {
        type: Number,
        require: true
    }
});
const hardModel = mongoose.model('hardware', hardSchema);

module.exports = hardModel;