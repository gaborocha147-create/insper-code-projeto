// Carousel controls: next/prev and drag-to-scroll
(function(){
  const carousel = document.getElementById('gestao-carousel');
  if(!carousel) return;

  const btnPrev = document.querySelector('.carousel-btn.prev');
  const btnNext = document.querySelector('.carousel-btn.next');

  const cardWidth = () => {
    const card = carousel.querySelector('.membro-card');
    return card ? card.getBoundingClientRect().width + 20 : 220; // include gap
  };

  btnPrev && btnPrev.addEventListener('click', ()=>{
    carousel.scrollBy({ left: -cardWidth(), behavior: 'smooth' });
  });
  btnNext && btnNext.addEventListener('click', ()=>{
    carousel.scrollBy({ left: cardWidth(), behavior: 'smooth' });
  });

  // Drag to scroll
  let isDown = false;
  let startX, scrollLeft;
  carousel.addEventListener('mousedown', (e)=>{
    isDown = true;
    carousel.classList.add('active');
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
  });
  carousel.addEventListener('mouseleave', ()=>{ isDown = false; carousel.classList.remove('active'); });
  carousel.addEventListener('mouseup', ()=>{ isDown = false; carousel.classList.remove('active'); });
  carousel.addEventListener('mousemove', (e)=>{
    if(!isDown) return;
    e.preventDefault();
    const x = e.pageX - carousel.offsetLeft;
    const walk = (x - startX) * 1; // scroll-fast
    carousel.scrollLeft = scrollLeft - walk;
  });

})();
