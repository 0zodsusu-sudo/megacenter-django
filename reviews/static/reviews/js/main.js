document.addEventListener('DOMContentLoaded', () => {
  // создаём двери
  const left = document.createElement('div');
  const right = document.createElement('div');
  left.className = 'lift-door left';
  right.className = 'lift-door right';
  document.body.append(left, right);

  // Открыть двери при старте
  setTimeout(() => {
    left.classList.add('open');
    right.classList.add('open');
  }, 500);

  // Подготовим звук (положи файл /static/reviews/sound/ding.mp3)
  const ding = new Audio('/static/reviews/sound/ding.mp3');

  // При клике на кнопку лифта — закрыть двери, проиграть звук и перейти
  document.querySelectorAll('.elevator-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      const url = this.getAttribute('href');

      // проигрываем звук (catch для бразуеров, требующих событий)
      ding.play().catch(()=>{});

      // закрыть двери
      left.classList.remove('open');
      right.classList.remove('open');

      // перейти через короткое время (должно совпадать с анимацией)
      setTimeout(() => {
        window.location.href = url;
      }, 850);
    });
  });

  // Открытие модалки оставить отзыв
  const reviewModal = new bootstrap.Modal(document.getElementById('reviewModal'), {});
  const openBtn = document.getElementById('open-review-modal');
  if (openBtn) openBtn.addEventListener('click', () => reviewModal.show());

  // Если форма отправляется в модалке — просто штатно (POST). Можно сделать AJAX позже.
  // Здесь можно дополнительно перехватить submit и отправлять fetch (AJAX).
});
