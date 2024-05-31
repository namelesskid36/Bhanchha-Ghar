const draggables = document.querySelectorAll('.draggable');
const container = document.querySelector('.draggable-container');

draggables.forEach(draggable => {
  // Get container dimensions
  const containerWidth = container.offsetWidth;
  const containerHeight = container.offsetHeight;

  // Get random positions within container
  const randomX = Math.floor(Math.random() * (containerWidth - draggable.offsetWidth));
  const randomY = Math.floor(Math.random() * (containerHeight - draggable.offsetHeight));

  // Set initial position for each draggable
  draggable.style.left = `${randomX}px`;
  draggable.style.top = `${randomY}px`;

  draggable.addEventListener('mousedown', onMouseDown);

  function onMouseDown(e) {
    e.preventDefault();

    const initialX = e.clientX;
    const initialY = e.clientY;
    const initialLeft = draggable.offsetLeft;
    const initialTop = draggable.offsetTop;

    draggable.style.cursor = 'grabbing';

    function onMouseMove(e) {
      const dx = e.clientX - initialX;
      const dy = e.clientY - initialY;

      draggable.style.left = `${initialLeft + dx}px`;
      draggable.style.top = `${initialTop + dy}px`;
    }

    function onMouseUp() {
      document.removeEventListener('mousemove', onMouseMove);
      document.removeEventListener('mouseup', onMouseUp);
      draggable.style.cursor = 'grab';
    }

    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  }
});

//Slider

const swiper = new Swiper('.blog-slider', {
    spaceBetween: 30,
    effect: 'fade',  //slide
    loop: true,  //eslai false ma rakda herneyy ok
    mousewheel: {
      invert: false, 
    },
    pagination: {
      el: '.blog-slider__pagination',
      clickable: true,
    }
  });
  
  