const express = require('express');
const router = express().router;
const colors = require('../controllers/color_controller');

router.use('/:color', (req, res, next) => {
    const color = req.inputs.color;
    colors.setColor(color);
    res.json({color: color});
})

router.use('/reset', (req, res, next) => {
    colors.setColor();
    res.json({color: 'white'});
})

router.use('/list', (req, res, next) => {
    res.json(colors.colorList());
})

module.exports = router;