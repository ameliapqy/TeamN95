var express = require('express');
var router = express.Router();


/* GET test api page page. */
router.get('/', function(req, res, next) {
    res.send("success from express server");
  });
  
  module.exports = router;
  