//returns a promise that gets resolved after x milliseconds
module.exports = async function (ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    })
}