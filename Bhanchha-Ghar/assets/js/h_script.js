/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
    menuToggle = document.getElementById('nav-toggle'),
    menuClose = document.getElementById('nav-close')

/* Menu show */
menuToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
})

/* Menu hidden */
menuClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu')
})

/*=============== SEARCH ===============*/
const search = document.getElementById('search'),
    searchBtn = document.getElementById('search-btn'),
    searchClose = document.getElementById('search-close')

/* Search show */
searchBtn.addEventListener('click', () => {
    search.classList.add('show-search')
})

/* Search hidden */
searchClose.addEventListener('click', () => {
    search.classList.remove('show-search')
})

/*=============== NAV COLLAPSE TOGGLE ===============*/
const navCollapseToggle = document.getElementById('nav-collapse-toggle');

// Toggle navigation collapse
navCollapseToggle.addEventListener('click', () => {
    navMenu.classList.toggle('collapsed');
    navCollapseToggle.classList.toggle('collapsed');
    // Change the icon based on nav state
    if (navMenu.classList.contains('collapsed')) {
        navCollapseToggle.classList.replace('ri-contract-left-right-line', 'ri-menu-line');
    } else {
        navCollapseToggle.classList.replace('ri-menu-line', 'ri-contract-left-right-line');
    }
});


const toggleDarkMode = () => {
    document.documentElement.classList.toggle('dark-mode');
};

const darkModeButton = document.querySelector('#dark-mode-toggle');
darkModeButton.addEventListener('click', toggleDarkMode);
