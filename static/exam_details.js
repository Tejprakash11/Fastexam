const clock = document.querySelector('.clock');
let timeLeft = 60 * 60;

const updateClock = () => {
  const hours = Math.floor(timeLeft / 60 / 60);
  const minutes = Math.floor(timeLeft / 60) % 60;
  const seconds = timeLeft % 60;

  clock.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

  if (timeLeft === 0) {
    clearInterval(intervalId);
    alert('Time is up!');
  }

  timeLeft--;
}

const intervalId = setInterval(updateClock, 1000);

updateClock();