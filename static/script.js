let time = 0;
let interval;

// increment timer 
function gamePageTimmer() {    
    const timmer = document.querySelector('.clock');
    
    clearInterval(interval)

    interval = setInterval(() => {
        time++;

        seconds = time % 60;
        minutes = Math.trunc(time / 60);

        timmer.innerHTML = minutes.toString().padStart(2, '0') + ' : ' + seconds.toString().padStart(2, '0');

    }, 1000);

}

// start timer when game page loads 
document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.clock')) {
        gamePageTimmer();
    }
});