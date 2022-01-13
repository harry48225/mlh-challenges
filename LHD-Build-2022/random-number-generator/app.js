const suncalc = require('suncalc')

const generateRandom = () => {
    const now = new Date();
    const lat = 45;
    const long = 45;
    const position = suncalc.getPosition(now, lat, long);
    const product = position.altitude * position.azimuth;
    return parseFloat('0.' + `${product}`.slice(-5)); // Return the last 5 digits normalised
}

setInterval(() => console.log(generateRandom()), 500);