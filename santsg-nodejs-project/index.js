const express = require('express')
const path = require('path')
var cors = require('cors')
const app = express()
const PORT = 3000

var corsOptions = {
    origin: 'http://localhost:3000',
    optionsSuccessStatus: 200 // For legacy browser support
}

app.use(cors(corsOptions));

app.set('view engine', 'pug')

app.get('/',(req,res)=>{
    res.sendFile(path.join(__dirname+'/index.html'))
})

app.get('/login.js',(req,res)=>{
    res.sendFile(path.join(__dirname+'/login.js'))
})

app.get('/data-monitoring/:passed_url', (req,res)=>{
    const data_url = decodeURIComponent(req.params.passed_url)
    console.log(data_url)
    res.render('data-monitoring', {data_path : `${data_url}` })
})

app.listen(PORT, ()=>{
    console.log("Server is running")
})

// solution of routing the javascript file in the html page
// https://stackoverflow.com/questions/48050666/node-js-serve-html-but-cant-load-script-files-in-served-page/48050718

// solution of dynamic html file with using pug
// https://stackoverflow.com/questions/37991995/passing-a-variable-from-node-js-to-html

// html to pug
// https://html-to-pug.com/

// solution to passing variable to script in pug page
// https://stackoverflow.com/questions/49238052/how-to-pass-variables-to-pugs-script-block