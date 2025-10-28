function openDoors() {
  const doors = document.getElementById('elevator-doors');
  if (doors) {
    setTimeout(() => doors.classList.add('open'), 600);
  }
}

function closeDoors() {
  const doors = document.getElementById('elevator-doors');
  if (doors) doors.classList.remove('open');
}

function goToFloor(url, currentFloor, targetFloor) {
  const arrow = document.getElementById('arrow-indicator');
  if (arrow) {
    arrow.textContent = targetFloor > currentFloor ? '▲' : '▼';
  }
  closeDoors();
  setTimeout(() => {
    window.location.href = url;
  }, 1200);
}

/* Звук “Дзинь” при открытии дверей */
const ding = new Audio('/static/reviews/sounds/ding.mp3');
window.addEventListener('load', () => {
  setTimeout(() => ding.play().catch(() => {}), 700);
});
