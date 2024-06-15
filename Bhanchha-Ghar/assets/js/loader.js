document.addEventListener("DOMContentLoaded", function() {
    // Show loader
    const loader = document.querySelector('.loader');
    const mainContent = document.querySelector('#main-content');
  
    // Minimum loading time in milliseconds
    const minLoadingTime = 2000;
    const startTime = new Date().getTime();
  
    window.addEventListener("load", function() {
      const loadTime = new Date().getTime() - startTime;
      const delay = Math.max(minLoadingTime - loadTime, 0);
  
      setTimeout(function() {
        // Hide loader and show main content after the delay
        loader.style.display = 'none';
        if (mainContent) {
          mainContent.style.display = 'block';
        }
      }, delay);
    });
  });
  